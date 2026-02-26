"""
Combine swing path (bat tracking) data with batting stats like wRC+ for analysis.

Run: python analysis.py
"""

import pandas as pd
from pybaseball import batting_stats, playerid_reverse_lookup

SWING_PATH_FILE = "bat-tracking-swing-path.csv"
OUTPUT_FILE = "swing-path-with-stats.csv"
START_SEASON = 2023
END_SEASON = 2025
MIN_PA = 50  # Minimum plate appearances across the period (lower = more players matched)


def main():
    # Load swing path data
    swing_path = pd.read_csv(SWING_PATH_FILE)
    swing_path["id"] = swing_path["id"].astype(int)
    print(f"Loaded {len(swing_path)} players from swing path data")

    # Map MLBAM IDs to FanGraphs IDs
    mlbam_ids = swing_path["id"].unique().tolist()
    id_lookup = playerid_reverse_lookup(mlbam_ids)
    id_lookup = id_lookup[["key_mlbam", "key_fangraphs"]].dropna(subset=["key_fangraphs"])
    id_lookup = id_lookup[id_lookup["key_fangraphs"] > 0]  # Exclude -1 (no FG ID)
    id_lookup["key_mlbam"] = id_lookup["key_mlbam"].astype(int)
    id_lookup["key_fangraphs"] = id_lookup["key_fangraphs"].astype(int)
    print(f"Mapped {len(id_lookup)} players to FanGraphs IDs")

    # Fetch aggregate batting stats 2023-2025 to match swing path period
    print(f"Fetching {START_SEASON}-{END_SEASON} batting stats (min {MIN_PA} PA)...")
    batting = batting_stats(
        START_SEASON,
        end_season=END_SEASON,
        qual=MIN_PA,
        split_seasons=False,  # Aggregate across years
    )
    batting["IDfg"] = batting["IDfg"].astype(int)
    print(f"Retrieved stats for {len(batting)} players")

    # Join: swing_path -> id_lookup -> batting
    merged = swing_path.merge(id_lookup, left_on="id", right_on="key_mlbam", how="left")
    merged = merged.merge(batting, left_on="key_fangraphs", right_on="IDfg", how="inner")
    merged = merged.drop(columns=["key_mlbam", "key_fangraphs", "IDfg"], errors="ignore")

    # Save combined data
    merged.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(merged)} players to {OUTPUT_FILE}")

    # Quick preview: swing path metrics vs wRC+
    if "wRC+" in merged.columns:
        print("\nSample (top 5 by wRC+):")
        cols = ["name", "avg_bat_speed", "attack_angle", "swing_tilt", "wRC+"]
        cols = [c for c in cols if c in merged.columns]
        print(merged[cols].head().to_string(index=False))


if __name__ == "__main__":
    main()
