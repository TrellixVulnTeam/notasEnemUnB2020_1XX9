# %%
import pandas as pd

# %%
courseDF = pd.read_json('jsons/nomecurso.json')
courseDF = courseDF.rename(columns={'Id': 'IDs'})

# %%
gradeDF = pd.read_json('jsons/nomenota.json')
gradeDF.head()

# %%
passed = courseDF['IDs']
condition = gradeDF['IDs'].isin(passed)
passedgrades = gradeDF.loc[condition]

# %%
passedgrades['Courses'] = courseDF['Course']
passedgrades.head()
