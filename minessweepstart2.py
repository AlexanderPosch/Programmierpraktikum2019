import pygame
import numpy as np
import random 
pygame.init()
pygame.event.set_blocked([1,3,6,4])

tilesize=50
size=np.array((10,10))
screen = pygame.display.set_mode(((size+0*np.array((10,10)))*tilesize))




class Minesweeper():
    def __init__(self,fsize,bombs,pos=None):
        self.fsize=fsize
        self.Mf=np.zeros(fsize, dtype=int)
        #Array with 0,1,..8 indicating neibouring bombs, 9 means bomb
        ##### 1-. means flaged
        ##### 2-. means visble
        self.Mf,self.Bl=self.bombplacment(bombs)
        self.Mf=self.nnb()
        
        

    def bombplacment(self,bombs):
        c=self.Mf.reshape(self.Mf.size)
        bombpositions=random.sample(range(self.Mf.size),bombs)
        for i in bombpositions:
            c[i]=9
        c=c.reshape(fsize)
        return c,list(zip(*np.where(c==9)))
        


        
    def nnb(self):#number fields next to bombs
        for i in self.Bl:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if self.Mf[tuple(np.array(i)+np.array((j,k)))]!=9:
                        self.Mf[tuple(np.array(i)+np.array((j,k)))]+=1
                    


        
    def flag(self,pos):
        if Minefield[pos]<10:
            Minefield[pos]+=10
        elif Minefield[pos]<20:
            Minefield[pos]-=10


        
    def open(self,pos):
        if self.Mf[pos]<10:
            if self.Mf[pos]==9:
                fail()
            else:
                self.Mf[pos]+=20
                floodfill()

            
    def floodfill(self):# Maybee make more fast
        while repeat:
            repeat=False
            for i in range(size[0]):
                for j in range(size[1]):
                    if Minefield[i,j]==20:
                        for k in [-1,0,1]:
                            for l in [-1,0,1]:
                                if ((i+k>=0)and(j+l)>=0)and ((i+k<size[0])and(j+l<size[1])):
                                    if Minefield[i+k,j+l]<20:
                                        Minefield[i+k,j+l]+=20
                                        repeat=True
        
        
