# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
DFc = pd.read_json('jsons/nomecurso.json')
DFc = DFc.rename(columns={'Id': 'IDs'})
dfc = DFc.sort_values(by='IDs')

# %%
DFg = pd.read_json('jsons/nomenota.json')
dfg = DFg.sort_values(by='IDs')

# %%
IDscourses = dfc['IDs']
DF = dfg.query("IDs in @IDscourses")

# %%
DF['Course'] = list(dfc['Course'])
DF = DF.set_index('IDs')
