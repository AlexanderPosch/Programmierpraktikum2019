
# coding: utf-8

# In[142]:


import pygame
import numpy as np
import math

pygame.init()
pygame.event.set_blocked([1,3,6,4])

tilesize=25
size=np.array((10,10))
screen = pygame.display.set_mode((size+np.array((10,10))*tilesize))


# In[222]:


Minefield=np.zeros(size)# a large nupy matrix with 0,1,..8 indication neibouring bombs, 9 means bomb
##### 1. means flaged
##### 2. means visble


def flag(pos):
    if Minefield[pos]<10: 
        Minefield[pos]+=10
    elif Minefield[pos]<20:
        Minefield[pos]-=10

        
def openup(pos):
    if Minefield[pos]<10:
        if Minefield[pos]==9:
            fail()
        else:
            Minefield[pos]+=20
            floodfill()
            
def fail(): #some Function that shows you that you have lost
    print(None)

    
def floodfill():
    repeat=True
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


# In[223]:


pygame.display.set_caption("MineSweeper")
screen.fill((255,255,255))


# In[145]:


done=False
while not done:
    pygame.display.flip()
    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        break 
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos=np.floor(np.array(event.pos)/100)
        changedpos=pos/tilesize
        if event.button==1:
            openup(event.pos)
        if event.button==2:
            flag(event.pos)
             

pygame.quit()




# In[245]:


Minefield


# In[217]:


flag((1,1))


# In[242]:


Minefield[(1,3)]=2


# In[244]:


floodfill()

