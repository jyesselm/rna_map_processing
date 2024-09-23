import pandas as pd
from pathlib import Path

RESOURCE_PATH = Path(__file__).parent / "resources"


def generate_sample_df():
    json_path = RESOURCE_PATH / "2024_07_24_nextseq_run14.json"
    df = pd.read_json(json_path)
    df = df.query("construct == 'pd_map_AC_AA_104_109'").reset_index(drop=True)
    df.to_json(RESOURCE_PATH / "pd_map_AC_AA_104_109.json", orient="records")


def generate_sample_titration_df():
    json_path = RESOURCE_PATH / "mttr6_data_full.json"
    df = pd.read_json(json_path)
    df = df.query("name == 'CCUACAC_GAUGG'").reset_index(drop=True)
    df.to_json(RESOURCE_PATH / "CCUACAC_GAUGG_titration.json", orient="records")


def main():
    generate_sample_df()
    generate_sample_titration_df()


if __name__ == "__main__":
    main()
