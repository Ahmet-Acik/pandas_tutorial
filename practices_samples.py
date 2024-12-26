import pandas as pd

# Sample data for Series
series_data = [1, 2, 3, 4, 5]
series_index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(series_data, index=series_index)
print("Series:")
print(series)

# Sample data for DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data, index=['x', 'y', 'z'])
print("\nDataFrame:")
print(df)

# Reading data from a CSV file 
cs_csv_file_path = './warm_up_data/coffee_sales.csv'
df_csv = pd.read_csv(cs_csv_file_path)
print("\nDataFrame from CSV:")
print(df_csv.head())

# Reading data from an Excel file 
excel_file_path = './data/coffee_shop_sales.xlsx'
df_excel = pd.read_excel(excel_file_path)
print("\nDataFrame from Excel:")
print(df_excel.head())

# Displaying information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Displaying summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Selecting a single column
print("\nColumn A:")
print(df['A'])

# Selecting multiple columns
print("\nColumns A and B:")
print(df[['A', 'B']])

# Selecting rows by label
print("\nRow 'x':")
print(df.loc['x'])

# Selecting rows by position
print("\nFirst row:")
print(df.iloc[0])

# Filtering rows based on a condition
print("\nRows where column A > 1:")
print(df[df['A'] > 1])

# Checking for missing values
print("\nMissing Values:")
print(df.isnull())

# Dropping rows with missing values
print("\nDataFrame after dropping rows with missing values:")
print(df.dropna())

# Filling missing values
print("\nDataFrame after filling missing values:")
print(df.fillna(0))

# Grouping data and applying aggregate functions
print("\nGrouped Data (sum):")
print(df.groupby('A').sum())

# Merging DataFrames (example with dummy data)
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
merged_df = pd.merge(df1, df2, on='key', how='outer')
print("\nMerged DataFrame:")
print(merged_df)

# Joining DataFrames (example with dummy data)
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]}).set_index('key')
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]}).set_index('key')
joined_df = df1.join(df2, how='outer')
print("\nJoined DataFrame:")
print(joined_df)

# Pivoting data (example with dummy data)
pivot_data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': [1, 2, 3, 4, 5, 6]
}
df_pivot = pd.DataFrame(pivot_data)
pivoted_df = df_pivot.pivot(index='A', columns='B', values='C')
print("\nPivoted DataFrame:")
print(pivoted_df)

# Melting data (example with dummy data)
melted_df = pd.melt(df_pivot.reset_index(), id_vars=['A'], value_vars=['one', 'two'])
print("\nMelted DataFrame:")
print(melted_df)

# Reshaping data (example with dummy data)
reshaped_df = df_pivot.stack()
print("\nReshaped DataFrame:")
print(reshaped_df)

# Sorting data
print("\nSorted DataFrame (by column A):")
print(df.sort_values(by='A'))

# Applying a function to the DataFrame
def square(x):
    return x ** 2

print("\nDataFrame with values squared:")
print(df.apply(square))

# Applying a function element-wise
print("\nDataFrame with values squared (element-wise):")
print(df.applymap(square))

# Creating a new column based on existing columns
df['D'] = df['A'] + df['B']
print("\nDataFrame with new column D:")
print(df)

# Dropping columns
df_dropped = df.drop(columns=['B', 'C'])
print("\nDataFrame after dropping columns B and C:")
print(df_dropped)

# Renaming columns
df_renamed = df.rename(columns={'A': 'Column1', 'B': 'Column2'})
print("\nDataFrame with renamed columns:")
print(df_renamed)

# Saving DataFrame to a CSV file
df.to_csv('./output_data/output.csv', index=False)

# Saving DataFrame to an Excel file
df.to_excel('./output_data/output.xlsx', index=False)

# Displaying the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Displaying the last few rows of the DataFrame
print("\nLast few rows of the DataFrame:")
print(df.tail())


















