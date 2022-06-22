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

g1 = randomGeographic(30,2)
g1.show(nombre='geographic_30_2_0')

#g1 = randomBarabasiAlbert(30,3)
#g1.show(nombre='barabasiAlbert_30_3')

#g1 = grid(50,10)
#g1.show(nombre='grid50_10')

#g1 = dorogovtsevMendes(500)
#g1.show(nombre='dorogovtsevMendes500')

g2 = g1.KruskalI()
g2.show(nombre='KruskalI_geographic_30_2_0')

g3 = g1.KruskalD(posiciones=True)
g3.show(nombre='KruskalD_geographic_30_2_0')

g4 = g1.Prim(posiciones=True)
g4.show(nombre='Prim_geographic_30_2_0')
