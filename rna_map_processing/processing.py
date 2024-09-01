import pandas as pd
from pathlib import Path
from typing import List

from seq_tools import has_5p_sequence, to_rna
from seq_tools import SequenceStructure
from seq_tools.structure import find as seq_ss_find
from rna_secstruct import SecStruct, MotifSearchParams

from rna_map_processing.paths import get_resources_path
from rna_map_processing.logger import get_logger

log = get_logger("processing")


def get_preprocessed_data(path: str, sets: List[str]) -> pd.DataFrame:
    dfs = []
    for run_name in sets:
        full_path = Path(path) / run_name / "analysis" / "summary.json"
        if not full_path.exists():
            raise FileNotFoundError(f"File {full_path} does not exist")
        df = pd.read_json(full_path)
        dfs.append(df)
    return pd.concat(dfs)


def trim(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    """
    Trims the 'sequence', 'structure', and 'data' columns of the DataFrame to the
    given start and end indices.

    Args:
        df (pd.DataFrame): A DataFrame with 'sequence', 'structure', and 'data'
                           columns, where 'data' contains lists of numbers.
        start (int): The start index for trimming.
        end (int): The end index for trimming.

    Returns:
        pd.DataFrame: A trimmed DataFrame with the 'sequence', 'structure', and
                      'data' columns adjusted to the specified indices.
    """

    def trim_column(column: pd.Series, start: int, end: int) -> pd.Series:
        if start == 0 and end == 0:
            return column
        if end == 0:
            return column.str[start:]
        elif start == 0:
            return column.str[:-end]
        else:
            return column.str[start:-end]

    df = df.copy()
    for col in ["sequence", "structure", "data"]:
        if col in df.columns:
            if col == "data":
                df[col] = df[col].apply(
                    lambda x: x[start:-end] if end != 0 else x[start:]
                )
            else:
                df[col] = trim_column(df[col], start, end)

    return df


def trim_p5_and_p3(
    df: pd.DataFrame, is_rna: bool = True, p3_length: int = 20
) -> pd.DataFrame:
    """
    Trims the 5' and 3' ends of the data in the DataFrame.

    This function reads a CSV file containing p5 sequences, converts these
    sequences to RNA, checks for a common p5 sequence in the given DataFrame,
    and trims the DataFrame based on the length of this common p5 sequence and
    a fixed 3' end length.

    Args:
        df (pd.DataFrame): A DataFrame with a 'data' column containing
                           sequences as strings.
        is_rna (bool): Flag indicating if the sequences are RNA. Default is True.
        p3_length (int): Length of the 3' end to trim. Default is 20.

    Returns:
        pd.DataFrame: A trimmed DataFrame with the 5' and 3' ends trimmed.

    Raises:
        ValueError: If no common p5 sequence is found or the sequence is not
                    registered in the CSV file.
    """
    df_p5 = pd.read_csv(get_resources_path() / "p5_sequences.csv")
    if is_rna:
        df_p5 = to_rna(df_p5)
    common_p5_seq = ""
    for p5_seq in df_p5["sequence"]:
        if has_5p_sequence(df, p5_seq):
            common_p5_seq = p5_seq
    if len(common_p5_seq) == 0:
        raise ValueError("No common p5 sequence found")
    log.debug(f"common p5 sequence: {common_p5_seq}")
    return trim(df, len(common_p5_seq), p3_length)
