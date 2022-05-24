from minds.data import Data
from minds.options import Options
from minds.minds1 import MinDS1Rules
from minds.check import ConsistencyChecker

import six
import math
import numpy as np
import pandas as pd

# IMPLEMENTAÇÃO DAS PARTIÇÕES -------------------------------------------
def split_partitions(data, nlp_partition=16):
    n_partition = int(math.ceil(data.shape[0]/nlp_partition))

    partitions = [
        pd.DataFrame(
            data=partition, 
            columns=data.columns
        )
        for partition in np.array_split(data.values, n_partition)
    ]

    return partitions

df_data = pd.read_csv('./tests/blood_pictures_1.csv')
df_data_partitions = split_partitions(df_data) # dados particionados

# -----------------------------------------------------------------------

# INSTANCIANDO UM DATA PARA CADA PARTIÇÃO -------------------------------
ls_datas = [
    Data(dataframe=df_data_partition)
    for df_data_partition in df_data_partitions
]

# -----------------------------------------------------------------------

# DEFININDO QUAL MODELO -------------------------------------------------
options = Options()
options.approach = 'minds1'

# -----------------------------------------------------------------------

# APLICANDO O MODELO EM CADA PARTIÇÃO---- -------------------------------
for data in ls_datas:   # iterando sobre as partições
    checker = ConsistencyChecker(data, options)
    if checker.status and checker.do() == False:
        checker.remove_inconsistent()

    solver = MinDS1Rules(data, options)
    covers = solver.compute()

# -----------------------------------------------------------------------

# MOSTRANDO AS REGRAS OBTIDAS -------------------------------------------
# for label in covers:
#     for rule in covers[label]:
#         print('rule:', rule)

# -----------------------------------------------------------------------
# print('')

# print('c2 cover size: {0}'.format(sum([len(p) for p in six.itervalues(covers)])))
# print('c2 cover wght: {0}'.format(solver.cost))

# if hasattr(solver, 'accy'):
#     print('c2 accy filtr: {0:.2f}%'.format(solver.accy))
# if hasattr(solver, 'accy_tot'):
#     print('c2 accy total: {0:.2f}%'.format(solver.accy_tot))

# print('c2 cover time: {0:.4f}'.format(solver.time))
