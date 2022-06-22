from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes

def DFSaux(G,u,explorados,g):
        """
        DFSaux: Funcion auxiliar para el algoritmo Depth First Search (DFS) recursivo
        G: grafo
        u: id del grafo inicial
        explorados: nodos explorados
        g: grafo DFS parcial
	return g: grafo DFS parcial
        """
        explorados.append(u)
        #g = Graph()
        g.addNode(u)
        D = G.getNode(u).neighboors 
        #print(D)
        for v in D:
                if v not in explorados:
                        g.addEdge(u + '->' + v,u,v)
                        g = DFSaux(G,v,explorados,g)
        #print(explorados)
        return g

def DFS_R(G,u):
        """
        Depth First Search recursivo
        G:  Grafo
        u:  Nodo inicial
	return g: Grafo DFS
        """
        explorados = []
        g = Graph() 
        g = DFSaux(G,u,explorados,g)
        return g


#g1 = randomErdosRenyi(500,1000)
#g1.show(nombre='erdosRenyi500_1000')


#g1 = randomGilbert(500,0.2)
#g1.show(nombre='gilbert500_02')

#g1 = randomGeographic(500,0.5)
#g1.show(nombre='geographic_500_0_5')

#g1 = randomBarabasiAlbert(500,4)
#g1.show(nombre='barabasiAlbert_500_4')

#g1 = grid(20,25)
#g1.show(nombre='grid20_25')

g1 = dorogovtsevMendes(500)
g1.show(nombre='dorogovtsevMendes500')

g2 = DFS_R(g1,'1')
g2.show(nombre='DFS_R_dorogovtsevMendes500')

