import pygame
import random
import math
import time
import numpy as np
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes

L = 500
W = 500
t = 15

window = pygame.display.set_mode((L,W))
red = (200,0,0)

def distance(a,b,c,d):
   """
   distancia del punto (a,b) al punto (c,d)
   """
   return math.sqrt( (a-c)**2 + (b-d)**2)
   

g = randomErdosRenyi(100,300)
#g = randomErdosRenyi(500,800)
#g = randomGilbert(100,0.1)
#g = randomGilbert(500,0.05)
#g = randomGeographic(100,0.4)
#g = randomGeographic(500,0.2)
#g = randomBarabasiAlbert(100,3)
#g = randomBarabasiAlbert(500,3)
#g = dorogovtsevMendes(100)
#g = dorogovtsevMendes(500)

modo = 1

#g = grid(20,5)
#g = grid(50,10)

nodos = g.nodes.keys()

# Inicializar en posiciones aleatorias


for node in nodos:
   #print(g.getNode(node).x)
   if modo == 1:
      g.getNode(node).x = random.random()*L
      g.getNode(node).y = random.random()*W
   else: 
      g.getNode(node).x = int(g.getNode(node).x)*L / 5.  #random.random()*L
      g.getNode(node).y = int(g.getNode(node).y)*W / 5.  #random.random()*W

#print(AG)

active = True
radius = 2
c1 = 100
c2 = 0.4
area = W*L
V = g.nodes.keys()
V = list(V)
k = math.sqrt(area/len(V))

def fr(x):
   return k**2 / x

def fa(x):
   return x**2 / k

def dibujar(g,t):
   """
   dibujar: ejecuta el algoritmo de Fruchterman-Reingold.
   g: grafo de entrada
   t: factor de enfriamiento
   """

   nodos = g.nodes.keys()
   V = g.nodes.keys()
   V = list(V)

   E = g.edges.keys()
   E = list(E)

   for nodeName in nodos:
      node = g.getNode(nodeName)
      x = node.x
      y = node.y
      node.disp = np.zeros(2)
      A = np.array([x,y])
      #F = np.zeros(2)
      #N = node.neighboors
      #s = np.zeros(2)
      for n0name in nodos:
         n0 = g.getNode(n0name)
         x0 = n0.x
         y0 = n0.y
         #d = distance(x,y,x0,y0)
         #print(d)
         #gamma = c2*math.log(d / c1)
         B = np.array([x0,y0])

         if nodeName != n0name:
            Delta = A-B # comentar
            norma = np.linalg.norm(Delta)
            node.disp += (Delta / norma)*fr(norma)


   #for node in nodos:
   #   node = g.getNode(node)
   #   node.x = node.gx
   #   node.y = node.gy

   for edge in E:
      edge1 = g.getEdge(edge)
      node0 = edge1.n0
      node1 = edge1.n1
      x1 = node0.x
      y1 = node0.y
      x2 = node1.x
      y2 = node1.y

      A = np.array([x1,y1])
      B = np.array([x2,y2])

      Delta = A - B
      norma = np.linalg.norm(Delta)
      d1 = (Delta / norma)*fa(norma)
      node0.disp -= d1
      node1.disp += d1

   for nodeName in nodos:
      node = g.getNode(nodeName)
      x = node.x
      y = node.y
      node.disp
      A = np.array([float(x),float(y)])
      norma = np.linalg.norm(node.disp)
      #print(A,node.disp, norma)
      A += (node.disp / norma)*min(norma,t)
      node.x = min(W,max(0,A[0]))
      node.y = min(L,max(0,A[1]))

   for edge in E:
      edge1 = g.getEdge(edge)
      node0 = edge1.n0
      node1 = edge1.n1
      x1 = node0.x
      y1 = node0.y
      x2 = node1.x
      y2 = node1.y


      pygame.draw.circle(window,red,(int(x1),int(y1)),radius)
      pygame.draw.circle(window,red,(int(x2),int(y2)),radius)
      pygame.draw.line(window, 'white', (int(x1), int(y1)), (int(x2), int(y2)), 1)


   t = 0.9*t
   return t

for i in range(6):
   print(i+1)
   time.sleep(1)


while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   t = dibujar(g,t)

   pygame.display.update()
   window.fill('black')
