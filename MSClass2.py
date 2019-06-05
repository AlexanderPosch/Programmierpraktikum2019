import numpy as np
import random 

class Minesweeper:
    def __init__(self,parent,fsize,bombs,pos):
        self.parent=parent
        self.fsize=np.array(fsize)
        self.Mf=np.zeros(fsize, dtype=int)
        #Array with intergers the first digit denotes the number of neighbouring bombs where 9 denotes that thes a bomb at the location
        #The second digit denotes whether a tile is 1. Flaged or 2. uncovered.
        
        self.Mf, self.Bl = self.bombplacment(bombs,pos) #Places bombs on minefield and puts their Locations in a list
        self.nnb() #determines the amount of bombs next to a field and writes it into Mf  
        
    def bombplacment(self,bombs,pos): #bombs denotes the amount of bombs placed no bombs placed around pos.
        c=self.Mf.reshape(self.Mf.size) 
        Upos=[(pos[0]-i)*self.fsize[0]+pos[1]+j for i in [-1,0,1] for j in [-1,0,1]]
        l=[i for i in range(self.Mf.size) if i not in Upos]
        bombpositions=random.sample(l,bombs) #random.sapmle(A,t) gives t different random elements from A  
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
                     
    def flag(self,pos):# Used to Flag a square
        if self.Mf[pos]<10:
            self.Mf[pos]+=10
        elif self.Mf[pos]<20:
            self.Mf[pos]-=10
        self.paint(pos)
        
    def openup(self,pos):# Used to open up/ unvocer a square
        if self.Mf[pos]<10:
            if self.Mf[pos]==9:
                self.fail()
                self.paint(pos)
            else:
                self.Mf[pos]+=20
                self.paint(pos)
                self.floodfill()
                
            
    def floodfill(self):# Maybee make more fast
        repeat=True
        while repeat:
            repeat=False
            for i in range(self.fsize[0]):
                for j in range(self.fsize[1]):
                    if self.Mf[i,j]==20:
                        for k in [0,-1,1]:
                            for l in [0,-1,1]:
                                if ((i+k>=0)and(j+l)>=0)and ((i+k<self.fsize[0])and(j+l<self.fsize[1])):
                                    if self.Mf[i+k,j+l]<20:
                                        self.Mf[i+k,j+l]+=20
                                        self.paint((i+k,j+l))
                                        repeat=True
                                        
    def paint(self,pos):
        i,j=pos
        tk.field = tk.Button(self.parent.parent,image = self.parent.images[self.parent.valtoim(self.Mf[i,j])])
        tk.field.bind('<Button-1>', lambda x, pos=pos,f=tk.field:self.parent.onclick(f,pos,1))
        tk.field.bind('<Button-3>', lambda x, pos=pos,f=tk.field:self.parent.onclick(f,pos,2))
        tk.field.bind('<ButtonRelease-3>', lambda x,f=tk.field:f.configure(relief="raised"))
        tk.field.grid(row=i, column=j)
    def fail(self):
        for b in self.Bl:
            self.Mf[b]=29
            self.paint(b)
        print("#######Fail############")
globals()['done'] = True
