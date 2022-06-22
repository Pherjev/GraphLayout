from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes

def BFS(G,u):
        """
        Algoritmo Breadth First Search (BFS)
        G: Grafo de entrada
	u: Nodo inicial
        return: Arbol BFS
        """
        L = []
        discovered = dict()
        discovered[u] = True
        nodos = list(G.nodes.keys())
        for n in nodos:
                if u != n:
                        discovered[n] = False
        
        g = Graph()
        g.addNode(u)
        L0 = [u]
        g.addNode(u)
        L.append(L0)
        Li = L0*1
        while len(Li) != 0:
                Lii = []
                for u in Li:
                        D = G.getNode(u).neighboors 
                        for v in D:
                                if discovered[v] == False:
                                        discovered[v] = True
                                        g.addNode(v)
                                        g.addEdge(u + '->' + v,u,v)
                                        Lii.append(v)
                L.append(Lii)
                Li = Lii*1

        return g

def desconectado(G,u):#,edge0):
        """
        Algoritmo Breadth First Search (BFS)
        G: Grafo de entrada
        u: Nodo inicial
        return: True si está desconectado
        """
        L = []
        discovered = dict()
        discovered[u] = True
        nodos = list(G.nodes.keys())
        for n in nodos:
                if u != n:
                        discovered[n] = False

        g = Graph()
        g.addNode(u)
        L0 = [u]
        g.addNode(u)
        L.append(L0)
        Li = L0*1
        while len(Li) != 0:
                Lii = []
                for u in Li:
                        D = G.getNode(u).neighboors
                        #print(D)
                        for v in D:
                                if discovered[v] == False:
                                        discovered[v] = True
                                        g.addNode(v)
                                        g.addEdge(u + '->' + v,u,v)
                                        Lii.append(v)
                L.append(Lii)
                Li = Lii*1

        for n in nodos:
                if discovered[n] == False:
                        return False

        return True

def conectado(G,u):
        """
        Componente conectado
        Algoritmo Breadth First Search (BFS)
        G: Grafo de entrada
        u: Nodo inicial
        return: lista de nodos en el componente conectado
        """
        L = []
        CC = []
        discovered = dict()
        discovered[u] = True
        nodos = list(G.nodes.keys())
        for n in nodos:
                if u != n:
                        discovered[n] = False

        g = Graph()
        g.addNode(u)
        CC.append(u)
        L0 = [u]
        L.append(L0)
        Li = L0*1
        while len(Li) != 0:
                Lii = []
                for u in Li:
                        D = G.getNode(u).neighboors
                        for v in D:
                                if discovered[v] == False:
                                        discovered[v] = True
                                        g.addNode(v)
                                        CC.append(v)
                                        g.addEdge(u + '->' + v,u,v)
                                        Lii.append(v)
                L.append(Lii)
                Li = Lii*1

        return g,CC


g1 = randomErdosRenyi(30,40)
g1.show(nombre='erdosRenyi30_40')

#g1 = randomGilbert(500,0.2)
#g1.show(nombre='gilbert500_02')

#g1 = randomGeographic(500,0.5)
#g1.show(nombre='geographic_500_0_5')

#g1 = randomBarabasiAlbert(500,3)
#g1.show(nombre='barabasiAlbert_500_3')

#g1 = grid(20,5)
#g1.show(nombre='grid20_25')

#g1 = dorogovtsevMendes(500)
#g1.show(nombre='dorogovtsevMendes500')

#print(desconectado(g1,'1'))
g2,CC = conectado(g1,'1')
print(CC)
g2.show(nombre='BFS_erdosRenyi30_40')
