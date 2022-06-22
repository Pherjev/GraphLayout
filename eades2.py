import pygame
import random
import math
import numpy as np
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes
import time
window = pygame.display.set_mode((500,500))
red = (200,0,0)


def distance(a,b,c,d):
   """
   distancia del punto (a,b) al punto (c,d)
   """
   return math.sqrt( (a-c)**2 + (b-d)**2)
   


#g = randomErdosRenyi(100,300)
g = randomErdosRenyi(500,3000)

nodos = g.nodes.keys()

# Initialize positions

for node in nodos:
   g.getNode(node).x = random.random()*500
   g.getNode(node).y = random.random()*500

active = True
radius = 2
c1 = 150
c2 = 0.4

print('Iniciando')

for i in range(10):
   print(i+1)
   time.sleep(1)



def dibujar(g):

   nodos = g.nodes.keys()
   nodos = list(nodos)


   E = g.edges.keys()
   E = list(E)

   for nodeName in nodos: 
      node = g.getNode(nodeName)
      x = node.x
      y = node.y
      A = np.array([x,y])
      F = np.zeros(2)
      N = node.neighboors
      s = np.zeros(2)
      for n0name in N:
         n0 = g.getNode(n0name)
         x0 = n0.x
         y0 = n0.y
         d = distance(x,y,x0,y0)
         #print(d)
         gamma = c2*math.log(d / c1)
         B = np.array([x0,y0])
         name =  nodeName + '->' + n0name
         #if name not in g.edges.keys():
         #   v = B - A
         #else: 
         #   v = A - B
         v = B - A # comentar
         norma = np.linalg.norm(v)
         v = v / norma
         v = gamma*v
         s += v
      A += s
      nx = A[0]
      ny = A[1]
      node.gx = nx # crear elemento 
      node.gy = ny

   for node in nodos:
      node = g.getNode(node)
      node.x = node.gx
      node.y = node.gy

   for edge in E:
      edge1 = g.getEdge(edge)
      node0 = edge1.n0
      node1 = edge1.n1
      x1 = node0.x
      y1 = node0.y
      x2 = node1.x
      y2 = node1.y

      d = distance(x1,y1,x2,y2)

      #x1 += c1*math.log(d)
      #x2 += c1*math.log(d)
      #y1 += c1*math.log(d)
      #y2 += c1*math.log(d)

      #print(x1,y1,x2,y2)

      pygame.draw.circle(window,red,(int(x1),int(y1)),radius)
      pygame.draw.circle(window,red,(int(x2),int(y2)),radius)
      pygame.draw.line(window, 'white', (int(x1), int(y1)), (int(x2), int(y2)), 1)


while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   dibujar(g)

   pygame.display.update()
   window.fill('black')
