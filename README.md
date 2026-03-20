# NHL-scoring-analysis
Analyzes NHL player statistics from the 2024–2025 season to identify which metrics best correlate with point production. Compares traditional stats like shots and ice time with advanced NHL EDGE metrics such as skating bursts and shot speed using correlation analysis and linear regression.
## Objective

The goal of this project is to answer:

**What factors actually drive NHL scoring?**

The analysis compares traditional statistics (shots, ice time, power-play points) with advanced performance metrics (skating speed, bursts, shot speed) to evaluate their impact on scoring.

## Methods

- Data collected using the NHL API (`nhlpy`)
- Advanced tracking data loaded from a dataset (`data.csv`)
- Filtered players with at least 60 games played
- Computed correlations using `pandas`
- Ranked metrics by correlation magnitude
- Created scatter plots with lines of best fit
- Evaluated relationships using R² (coefficient of determination)

## Visualizations

The project includes:

- **Horizontal bar chart** showing the top metrics correlated with point production
- **Scatter plot:** Points vs bursts over 22 mph
- **Scatter plot:** Points vs max shot speed

## Key Findings

- Opportunity-based metrics (power-play points, ice time) show the strongest relationship with scoring
- Shot volume has a moderate impact on point production
- Advanced performance metrics such as skating bursts and shot speed show weaker correlations than expected

## Conclusion

Scoring in the NHL is driven more by player usage and opportunity than by raw physical performance metrics.

Players tend to accumulate points through deployment and offensive role rather than solely through speed or shot power.

## Files

- `nhl_data.py` — main analysis script
- `data.csv` — NHL EDGE advanced stats dataset

## Technologies Used

- Python
- pandas
- NumPy
- matplotlib
- scikit-learn
- NHL API (`nhlpy`)

## Notes

- Correlation does not imply causation
- Analysis is limited to available player data
- Results focus on relationships, not predictive modeling
