import pandas as pd
from pathlib import Path

from rna_map_processing.titration import compute_mg_1_2

RESOURCE_PATH = Path(__file__).parent / "resources"


def test_compute_mg_1_2():
    df = pd.read_json(RESOURCE_PATH / "CCUACAC_GAUGG_titration.json")
    pfit, perr = compute_mg_1_2(df["mg_conc"], df["gaaa_avg"])
    print(pfit)
