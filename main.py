# a ideia é pegar os nomes e os cursos e relacionar-los.

# get names and courses

# get names and grades

# first: build a csv file with the course and the minimum grade used to pass

# %%
import pandas as pd
# %%
courseDF = pd.read_json('jsons/nomecurso.json')
courseDF.head()
# %%
gradeDF = pd.read_json('jsons/nomenota.json')
gradeDF.head()
