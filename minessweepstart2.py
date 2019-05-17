import pygame
import numpy as np
import random 
pygame.init()
pygame.event.set_blocked([1,3,6,4])

tilesize=50
size=np.array((10,10))
#screen = pygame.display.set_mode(((size+0*np.array((10,10)))*tilesize))




class Minesweeper:
    def __init__(self,fsize,bombs,pos=None):
        self.fsize=np.array(fsize)
        self.Mf=np.zeros(fsize, dtype=int)
        #Array with intergers the first digit denotes the number of neighbouring bombs where 9 denotes that thes a bomb at the location
        #The second digit denotes whether a tile is 1. Flaged or 2. uncovered.
        
        self.Mf, self.Bl = self.bombplacment(bombs)
        self.nnb()
        
    def bombplacment(self,bombs):
        c=self.Mf.reshape(self.Mf.size)
        bombpositions=random.sample(range(self.Mf.size),bombs)
        c[bombpositions]=9
        c=c.reshape(self.fsize)
        return c,list(zip(*np.where(c==9)))
        


        
    def nnb(self):#number fields next to bombs
        for i in self.Bl:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if all((np.array(i)+np.array((j,k)))>=0) and all((np.array(i)+np.array((j,k)))<self.fsize):
                        if self.Mf[tuple(np.array(i)+np.array((j,k)))]!=9:
                            self.Mf[tuple(np.array(i)+np.array((j,k)))]+=1
                     
    def flag(self,pos):
        if self.Mf[pos]<10:
            self.Mf[pos]+=10
        elif self.Mf[pos]<20:
            self.Mf[pos]-=10


        
    def openup(self,pos):
        if self.Mf[pos]<10:
            if self.Mf[pos]==9:
                a.fail()
            else:
                self.Mf[pos]+=20
                a.floodfill()

            
    def floodfill(self):# Maybee make more fast
        repeat=True
        while repeat:
            repeat=False
            for i in range(self.fsize[0]):
                for j in range(self.fsize[1]):
                    if self.Mf[i,j]==20:
                        for k in [-1,0,1]:
                            for l in [-1,0,1]:
                                if ((i+k>=0)and(j+l)>=0)and ((i+k<self.fsize[0])and(j+l<self.fsize[1])):
                                    if self.Mf[i+k,j+l]<20:
                                        self.Mf[i+k,j+l]+=20
                                        repeat=True
    def fail(self):
        print("........Fail...........")
        globals()['done'] = True
