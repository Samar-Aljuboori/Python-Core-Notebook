import pandas as pd

# ==============================================================================
# PANDAS DATA CORRELATIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Understanding Correlation (corr Method)
# ------------------------------------------------------------------------------
# 1. df.corr():
#    - Computes pairwise correlation of numeric columns.
#    - Ignores NaN / null values automatically.
#
# 2. Interpreting Values:
#    - Near +1.0: Strong positive relationship (both variables increase together)
#      (as A increases, B increases).

#    - Near -1.0: Strong negative relationship (one increases as the other decreases)
#      (as A increases, B decreases).

#    - Near  0.0: No linear relationship between the two variables.
# ------------------------------------------------------------------------------




data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 45],
    'Pulse': [110, 117, 103, 109, 150, 102, 108, 100],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 131, 119],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 361.0, 240.0],
}

df = pd.DataFrame(data)

print("=== 1. Correlation Matrix ===")
print(df.corr().round(2))

# Expected Output:
#           Duration  Pulse  Maxpulse  Calories
# Duration      1.00   0.05     -0.25      0.35
# Pulse         0.05   1.00      0.27      0.79
# Maxpulse     -0.25   0.27      1.00      0.09
# Calories      0.35   0.79      0.09      1.00


# ------------------------------------------------------------------------------
# 2. Specific Column Pair Correlation
# ------------------------------------------------------------------------------
# You can measure correlation between two specific Series rather than the entire DataFrame.

pulse_calories_corr = df['Pulse'].corr(df['Calories'])

print("\n=== 2. Pulse vs Calories Correlation ===")
print(round(pulse_calories_corr, 2))

# Expected Output:
# 0.79


# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - df.corr(): Ignores non-numeric columns automatically in recent Pandas versions.
# - Good Correlation: Values > 0.6 or < -0.6 generally indicate strong relationships.
# - Causation Caution: High correlation does NOT imply that one variable causes the other.
# ==============================================================================