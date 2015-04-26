import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *


years = range(1880, 2014)

dirName = '/Users/gabrielaliquo/pythongame/names/'

pieces = []
columns = ['name','sex','births']

for year in years:
    path = dirName + 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    frame['age'] = 2015 - year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)


NameList = ['Matthew', 'Erica', 'Francis', 'Zachary', 'Emily', 'Gabriel', 'Audrey', 'Judith', 'Erin', 'James']

Hoovers = names[names.name.isin(NameList)]

agepivot = Hoovers.pivot_table('births', index='age', columns='name')
print agepivot.head(n=10)

agepivot.plot(title='Hoovers/Aliquo Age').legend(loc='center left', bbox_to_anchor=(1, 0.5))


newfile = open("/Users/gabrielaliquo/Desktop/hoover_aliq.txt", 'a')
#s = str(names.name),str(names.sex), str(names.births), str(names.year), str(names.age)
newfile.write(str(agepivot))
newfile.close()