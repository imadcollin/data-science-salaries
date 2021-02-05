#%%
import pandas as pd
df = pd.read_csv('sample.csv')
print(df.head(10))


# %% Cleanup salaries, remove $
def clean_salary(row):
    salary = row['Salary'].replace('$', '')
    return float(salary)


# %% Add a new row for cleaned salaries
df['cleaned_salary'] = df.apply(clean_salary, axis=1)

# %% Print
print(df.head(10))

#%% Salaries mean
salaries_mean = df['cleaned_salary'].mean()
print(salaries_mean)

# %% Salaries mean Grouped By Gender
salaries_by_gender = df.groupby('gender')['cleaned_salary'].mean()
print(salaries_by_gender)