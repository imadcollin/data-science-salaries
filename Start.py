#%%
import pandas as pd
df = pd.read_csv('sample.csv').dropna()
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


# %%
def female_salary(row):
    if row['gender'] == 'Female':
        return row['cleaned_salary']


def male_salary(row):
    if row['gender'] == 'Male':
        return row['cleaned_salary']


# %%
df['female_salaries'] = df.apply(female_salary, axis=1)
df['male_salaries'] = df.apply(male_salary, axis=1)

df.head(10)
# %%
#print(df.groupby('Job Title')['female_salaries','male_salaries'].mean());
# %% Remove dulicates ......
df2 = df.drop_duplicates()
#print(df2.shape)

# %% Where city is staring with "S"
df['Start_with'] = df['City'].str.startswith(
    'S')  # map(lambda x : x.startswith('S'), df['City'])
print(df)

# %%
