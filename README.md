# Swing Path + Batting Stats Analysis

Combine bat-tracking swing path data with FanGraphs batting stats (wRC+, etc.) for analysis.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

## Run

```bash
python analysis.py
```

Output: `swing-path-with-stats.csv` — swing path columns plus batting stats (wRC+, wOBA, OPS, AVG, etc.).

## Customize

Edit `analysis.py` to change:
- `SEASON` — year for batting stats (default: 2024)
- `MIN_PA` — minimum plate appearances (default: 50)
