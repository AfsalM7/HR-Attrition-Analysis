import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../HR_Attrition.csv')

# 1. Basic shape - rows and columns
print("Shape of dataset:", df.shape)

# 2. Column names
print("\nColumn names:")
print(df.columns.tolist())

# 3. First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 4. Data types and non-null counts
print("\nInfo:")
print(df.info())

# 5. Missing values check
print("\nMissing values:")
print(df.isnull().sum())

# 6. Statistical summary for numeric columns
print("\nStatistical summary:")
print(df.describe())

# Attrition count and percentage
print("\nAttrition value counts:")
print(df['Attrition'].value_counts())

print("\nAttrition percentage:")
print(df['Attrition'].value_counts(normalize=True) * 100)

# Attrition by Department
print("\nAttrition by Department:")
print(pd.crosstab(df['Department'], df['Attrition']))

# Attrition by OverTime
print("\nAttrition by OverTime:")
print(pd.crosstab(df['OverTime'], df['Attrition']))

# Attrition by JobRole
print("\nAttrition by JobRole:")
print(pd.crosstab(df['JobRole'], df['Attrition']))

# Combined analysis - JobRole + OverTime
print("\nAttrition by JobRole and OverTime:")
print(pd.crosstab([df['JobRole'], df['OverTime']], df['Attrition']))

# Chart 1: Overall Attrition
df['Attrition'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Overall Attrition Count')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 2: Attrition by OverTime
pd.crosstab(df['OverTime'], df['Attrition']).plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Attrition by OverTime')
plt.xlabel('OverTime')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()

# Chart 3: Attrition by JobRole
pd.crosstab(df['JobRole'], df['Attrition']).plot(kind='bar', color=['skyblue', 'salmon'], figsize=(10,6))
plt.title('Attrition by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()