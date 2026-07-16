import mmdatasdk as md
import numpy as np
import pandas as pd
from pathlib import Path


def load_csd(filepath: str) -> dict:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} not found")

    data = md.mmdataset(str(filepath))
    print(f"Loaded: {filepath.name}")
    return data


def inspect_csd(data: dict) -> None:
    for key, val in data.items():
        if isinstance(val, np.ndarray):
            print(f"  {key}: shape={val.shape}, dtype={val.dtype}")
        elif isinstance(val, list):
            print(f"  {key}: len={len(val)}, type={type(val[0]).__name__ if val else 'N/A'}")
        else:
            print(f"  {key}: type={type(val).__name__}")


def csd_to_dataframe(data: dict, label: str | None = None) -> pd.DataFrame:
    rows = []
    for key, val in data.items():
        rows.append({"key": key, "type": type(val).__name__, "shape": str(getattr(val, "shape", "N/A"))})
    df = pd.DataFrame(rows)
    if label:
        print(f"\n--- {label} ---")
    return df


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Load and inspect CMU-MOSEI .csd files")
    parser.add_argument("file", help="Path to .csd file")
    parser.add_argument("--df", action="store_true", help="Print summary as DataFrame")
    args = parser.parse_args()

    csd = load_csd(args.file)
    inspect_csd(csd)

    if args.df:
        print(csd_to_dataframe(csd, args.file))
