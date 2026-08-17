import matplotlib.pyplot as plt
import pandas as pd


# ------------------------------------------------------------------------------
# PANDAS PLOTTING :Pandas uses the plot() method to create diagrams. 
# ------------------------------------------------------------------------------
# 1. Integration: Pandas uses Matplotlib under the hood via the .plot() method.
# 2. Key Arguments:
#    - kind : Specifies plot type ('line', 'scatter', 'hist', 'bar', 'box').
#    - x, y : Column names for horizontal and vertical axes.
# 3. Execution: Call plt.show() from matplotlib.pyplot to display the generated graph.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 1. Basic Line Plot 
# ------------------------------------------------------------------------------
# Used for showing trends over time or continuous sequences.

data_line = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 45],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 361.0, 240.0],
}
df_line = pd.DataFrame(data_line)

# Plotting line chart
df_line.plot(kind='line', title='Duration vs Calories')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()


# ------------------------------------------------------------------------------
# 2. Scatter Plot 
# ------------------------------------------------------------------------------
# Used to visualize the relationship/correlation between two numeric variables.

df_line.plot(
    kind='scatter', x='Duration', y='Calories', title='Scatter: Duration vs Calories'
)
plt.show()


# ------------------------------------------------------------------------------
# 3. Histogram 
# ------------------------------------------------------------------------------
# Used to show the distribution of a single numerical column (frequency).

df_line['Calories'].plot(
    kind='hist', bins=5, title='Distribution of Calories'
)
plt.xlabel('Calories')
plt.show()


# ------------------------------------------------------------------------------
# 4. Bar Chart 
# ------------------------------------------------------------------------------
# Used for comparing discrete categories or summary values.

data_bar = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Employees': [12, 25, 8, 15],
}
df_bar = pd.DataFrame(data_bar)

df_bar.plot(
    kind='bar',
    x='Department',
    y='Employees',
    legend=False,
    title='Employee Count per Department',
)
plt.ylabel('Count')
plt.show()




# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - df.plot(kind='...'): Main interface for plotting in Pandas.
# - 'line'   : Default plot type, best for trends.
# - 'scatter': Requires x and y parameters, best for correlations.
# - 'hist'   : Best for seeing data distribution (frequency).
# - 'bar'    : Best for categorical comparisons.
# - plt.show(): Displays the rendered plot window.
# ==============================================================================

# ------------------------------------------------------------------------------
# PANDAS PLOTTING: WHY, WHEN, AND HOW
# ------------------------------------------------------------------------------
# WHY : Visualizing raw dataframe numbers to instantly spot patterns & trends.
# WHEN:
#   - 'line'   : Best for continuous sequence/time trends.
#   - 'scatter': Best for comparing 2 numerical columns (finding correlation).
#   - 'hist'   : Best for checking frequency distribution of a single column.
#   - 'bar'    : Best for comparing discrete categories.
# HOW : Call df.plot(kind='...', x='...', y='...') followed by plt.show().
# ------------------------------------------------------------------------------