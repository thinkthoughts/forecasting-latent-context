from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
REPORTS = ROOT / "reports"

for p in [FIGURES, RESULTS, REPORTS]:
    p.mkdir(exist_ok=True)
