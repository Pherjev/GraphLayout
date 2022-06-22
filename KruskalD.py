from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes
from queue import PriorityQueue


#g1 = randomErdosRenyi(500,700)
#g1.show(nombre='erdosRenyi500_700')

#g1 = randomGilbert(500,0.1)
#g1.show(nombre='gilbert500_01')

g1 = randomGeographic(15,1.5)
g1.show(nombre='geographic_15_1_5')

#g1 = randomBarabasiAlbert(30,3)
#g1.show(nombre='barabasiAlbert_30_3')

#g1 = grid(50,10)
#g1.show(nombre='grid50_10')

#g1 = dorogovtsevMendes(500)
#g1.show(nombre='dorogovtsevMendes500')

g2 = g1.KruskalD(posiciones=True)
g2.show(nombre='KruskalD_geographic_15_1_5')

g3 = g1.KruskalI()
g3.show(nombre='KruskalI_geographic_15_1_5')
