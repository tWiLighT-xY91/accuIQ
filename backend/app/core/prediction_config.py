"""
Prediction Engine Configuration

All tunable parameters for the prediction engine live here.
Future versions can modify these values without changing
the prediction algorithm itself.
"""

# ---------------------------------------------------------------------
# Feature Weights
# ---------------------------------------------------------------------

FREQUENCY_WEIGHT = 0.35

YEAR_COVERAGE_WEIGHT = 0.25

RECENCY_WEIGHT = 0.40

# ---------------------------------------------------------------------
# Confidence Thresholds
# ---------------------------------------------------------------------

HIGH_CONFIDENCE_THRESHOLD: float = 0.80
MEDIUM_CONFIDENCE_THRESHOLD: float = 0.60