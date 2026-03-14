# Swing Path & Contact Quality: Analysis Report

**Date:** February 2026  
**Project:** MLB Bat Tracking × FanGraphs Analysis  
**Data:** 2023–2025 (aggregated)

---

## Executive Summary

This report summarizes an analysis of MLB bat-tracking swing path data and its relationship to contact quality. The main finding is that **swing path metrics explain roughly 70% of Barrel% variance** and 69% of HardHit% variance, indicating a strong link between how a player swings and the quality of contact they produce.

---

## Data

### Sources

- **Swing path (bat tracking):** Bat-tracking metrics for 189 MLB players (2023–2025)
- **Contact / outcome stats:** FanGraphs (2023–2025 aggregate, min 50 PA), via pybaseball
- **Sample size:** 188 players (one player excluded due to ID mapping issue)

### Swing Path Metrics

| Metric | Description |
|--------|-------------|
| **avg_bat_speed** | Average bat speed (mph) |
| **swing_tilt** | Vertical angle of the swing path (°) |
| **attack_angle** | Angle at contact (°) |
| **attack_direction** | Horizontal angle (°) |
| **ideal_attack_angle_rate** | Share of swings at “ideal” angle |

### Contact Quality Metrics

- **Barrel%** – Share of batted balls with optimal exit velo & launch angle
- **HardHit%** – Share of batted balls > 95 mph
- **ISO** – Isolated power
- **xwOBA** – Expected wOBA from contact quality

---

## Methods

1. **Data merge:** MLBAM ID mapping (Chadwick register) to join swing path and FanGraphs data
2. **OLS regression:** Barrel%, HardHit%, ISO, and xwOBA regressed on the 5 swing path metrics
3. **Swing path grades:** Players split into A/B/C/D by predicted Barrel% (quartiles)
4. **Over/underperformers:** Residuals (actual − predicted Barrel%) identify those exceeding or falling short of their swing path

---

## Findings

### 1. Swing path explains contact quality much better than outcomes

| Target | R² |
|--------|-----|
| Barrel% | **0.73** |
| HardHit% | **0.69** |
| ISO | 0.57 |
| xwOBA | 0.27 |

Swing path predicts Barrel% and HardHit% far better than it predicts xwOBA or other outcome-based metrics, which are also shaped by plate discipline, sequencing, and defense.

### 2. Bat speed and swing tilt are the main drivers

In the Barrel% model, the strongest predictors are:

- **Bat speed** – Higher bat speed is associated with more barrels
- **Swing tilt** – More vertical tilt is associated with more barrels
- **Attack angle** – Also significant; higher angles support better contact

### 3. Swing path grades (A/B/C/D)

Players are graded A–D by predicted Barrel%. Grade A corresponds to the best swing path for producing barrels. Example Grade A swing-path players: Stanton, Judge, Cruz, Schwarber, Greene, Ohtani, Alvarez.

### 4. Overperformers and underperformers

- **Overperformers:** Actual Barrel% above predicted (e.g., Judge, Ward, Ohtani) – likely aided by pitch selection, contact point, or other factors beyond swing path
- **Underperformers:** Actual Barrel% below predicted (e.g., Varsho, Arenado, Peña) – possible issues with approach, pitch mix, or timing

---

## Limitations

- **Sample:** Qualified hitters with bat-tracking and 50+ PA in 2023–2025
- **Associations only:** Correlations, not causal links
- **Multicollinearity:** Swing metrics are related; coefficients can be sensitive
- **Missing player:** One player (Andy Pages) excluded due to FanGraphs ID mapping

---

## Conclusions

1. Swing path is strongly associated with Barrel% and HardHit%; it explains most of the variance in these contact-quality stats.
2. Bat speed and swing tilt are the most important swing path predictors.
3. A swing path grade (A–D) plus residual-based over/underperformance offers a simple way to evaluate swing path and identify “overperformers” and “underperformers” relative to swing path.

---

## Reproducibility

- **Scripts:** `analysis.py` (data merge), `exploration.ipynb` (analysis)
- **Requirements:** `requirements.txt` (pybaseball, pandas, matplotlib, seaborn, statsmodels, jupyter)
- **Repo:** https://github.com/bgaucf/mlb-swing-path-analysis
