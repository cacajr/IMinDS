from minds.data import Data
from minds.options import Options
from minds.minds1 import MinDS1Rules

import six

data = Data(filename='./tests/tabela_depressao.csv', separator=',')

options = Options()
options.approach = 'minds1'

solver = MinDS1Rules(data, options)

covers = solver.compute()

for label in covers:
    for rule in covers[label]:
        print('rule:', rule)

print('')

print('c2 cover size: {0}'.format(sum([len(p) for p in six.itervalues(covers)])))
print('c2 cover wght: {0}'.format(solver.cost))

if hasattr(solver, 'accy'):
    print('c2 accy filtr: {0:.2f}%'.format(solver.accy))
if hasattr(solver, 'accy_tot'):
    print('c2 accy total: {0:.2f}%'.format(solver.accy_tot))

print('c2 cover time: {0:.4f}'.format(solver.time))
