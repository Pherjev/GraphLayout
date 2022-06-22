from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes

def DFS_Iaux(G,inicial,g,stack,visited):
        """
        DFSaux: Funcion auxiliar para el algoritmo Depth First Search (DFS) recursivo
        G: grafo
        inicial: id del grafo inicial
	g: grafo DFS parcial
	stack: pila auxiliar
        visited: nodos explorados
        return g: grafo DFS parcial
        """
        stack.append(inicial)
        while len(stack) != 0:
                u = stack[-1]
                stack.pop()
                visited.append(u)
                g.addNode(u)
                D = G.getNode(u).neighboors
                #print(D)
                for v in D:
                        if v not in visited:
                                g.addEdge(u + '->' + v,u,v)
                                g = DFS_Iaux(G,v,g,stack,visited)

        return g

def DFS_I(G,u):
        """
        Depth First Search recursivo
        G:  Grafo
        u:  Nodo inicial
        return g: Grafo DFS
        """
        stack = []
        visited = []
        g = Graph()
        g = DFS_Iaux(G,u,g,stack,visited) 
        return g                               


#g1 = randomErdosRenyi(30,70)
#g1.show(nombre='erdosRenyi30_70')

#g1 = randomGilbert(30,0.2)
#g1.show(nombre='gilbert30_02')

#g1 = randomGeographic(30,1.5)
#g1.show(nombre='geographic_30_1_5')

#g1 = randomBarabasiAlbert(30,3)
#g1.show(nombre='barabasiAlbert_30_3')

#g1 = grid(6,5)
#g1.show(nombre='grid6_5')

g1 = dorogovtsevMendes(30)
g1.show(nombre='dorogovtsevMendes30')

g2 = DFS_I(g1,'1')
g2.show(nombre='DFS_I_dorogovtsevMendes30')
