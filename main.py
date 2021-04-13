# a ideia é pegar os nomes e os cursos e relacionar-los.

# get names and courses

# get names and grades

# first: build a csv file with the course and the minimum grade used to pass

# %%
import nomenota as nn
import nomecurso as nc
import pandas as pd

df = pd.DataFrame(nc.idEcourses())
df.head()
