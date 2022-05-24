from minds.data import Data
from minds.options import Options
from minds.minds1 import MinDS1Rules
from minds.check import ConsistencyChecker

import six

# instancia Data
data = Data(filename='./tests/tabela_depressao.csv', separator=',')

# escolhe o modelo
options = Options()
options.approach = 'minds1'

# verificação de consistencia
checker = ConsistencyChecker(data, options)
if checker.status and checker.do() == False:
    checker.remove_inconsistent()

# instancia modelo
solver = MinDS1Rules(data, options)

# aplica a modelagem
covers = solver.compute()

# mostra as regras
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
