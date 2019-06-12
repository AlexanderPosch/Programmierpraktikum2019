import numpy as np
import random 
import tkinter as tk 
from PIL import Image, ImageTk


class Minesweeper:
    def __init__(self,owner,fsize,bombs,pos):
        self.owner=owner
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
        self.owner.paint(pos)
        
    def openup(self,pos):# Used to open up/ unvocer a square
        vp=self.Mf[pos]
        if vp<10:
            if vp==9:
                self.Mf[pos]+=20
                self.fail(pos)
            else:
                self.Mf[pos]+=20
                self.owner.paint(pos)
                if vp==0:
                    self.floodfill([np.array(pos)])
                self.checkifwon()
                
    def floodfill(self,plist):# Currently blocks tkinters mainlooop :(
        nplist=[]
        for pos in plist:
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    cp=pos+np.array((k,l))
                    if np.all(cp>=0) and np.all(cp<self.fsize):
                        v=self.Mf[cp[0],cp[1]]
                        if v==0:
                            nplist.append(cp)
                        if v<10:
                            self.Mf[cp[0],cp[1]]+=20
                            self.owner.paint(cp)
                            self.owner.owner.update()###################Decide how much indent#####################
        if len(nplist)>0:
            self.floodfill(nplist)

        
    def fail(self,pos):
        Bls=sorted(self.Bl,key=lambda x:np.linalg.norm(np.array(x)-np.array(pos)))
        for b in Bls:
            self.Mf[b]=29
            self.owner.paint(b)
            self.owner.owner.update()
        print("#######Fail############")
        globals()['done'] = True
        
    def checkifwon(self):
        if  np.min(self.Mf)==9:
            print("Congrtats")
        


# In[2]:


class StartScreen(tk.Frame):
    def __init__(self, parent,owner):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.owner=owner
        
        self.bind("<Configure>",self.owner.resizewindow)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.Mfsize=tk.IntVar()
        self.bombs=12
        self.draw()
        
    def draw(self,evnet=None):
        #print("2")
        fontsize=min(40,int(min(self.owner.fh,self.owner.fw)/16)+1)
        self.owner.resizestuff(1)
        ######Destroy all########
        for widget in self.winfo_children():
            widget.destroy()    
        ###### Draw new  ########
        self.Header=tk.Label(self,image=self.owner.headerim)
        self.rb1 = tk.Radiobutton(self ,text="Beginner",variable=self.Mfsize , value=8,font=("Courier", fontsize)) 
        self.rb2 = tk.Radiobutton(self ,text="Advanced",variable=self.Mfsize , value=12,font=("Courier", fontsize)) 
        self.rb3 = tk.Radiobutton(self ,text="Expert  ",variable=self.Mfsize , value=20,font=("Courier", fontsize)) 
        self.button = tk.Button(self,text='Play', command=self.pass1,font=("Courier", fontsize))
        
        
        self.Header.grid(row=0,column=1,pady=(0,int(self.owner.fh/100)))
        self.rb1.grid(row=2,column=1)
        self.rb2.grid(row=3,column=1)
        self.rb3.grid(row=4,column=1)
        self.button.grid(row=5,column=1,pady=int(self.owner.fh/100))
        
        
        
    def pass1(self):
        self.owner.firstmove=True
        s=self.Mfsize.get()
        self.owner.Mfsize=np.array((s,s))
        self.owner.bombs=self.bombs
        self.owner.frames[GameScreen].draw()
        
        self.owner.show_frame(GameScreen)
        
        
        


# In[3]:


class GameScreen(tk.Frame):
    def __init__(self, parent,owner):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.owner=owner
        self.bind("<Configure>",self.owner.resizewindow)
        
        
    def draw(self,event=None):
        ######Destroy all########
        for widget in self.winfo_children():
            widget.destroy()
        ###### Draw new  ########
        if self.owner.firstmove:
            self.m=Minesweeper(self,self.owner.Mfsize,self.owner.bombs,(0,0)) #make provisoric minefield new one is created at fist click

        #Keep Minefield in the middel of the window
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(self.owner.Mfsize[0]+2, weight=1)
        self.grid_columnconfigure(self.owner.Mfsize[1]+2, weight=1)
        
        self.owner.resizestuff(2)
        #self.Header=tk.Label(self,image=self.owner.headerim2)
        #self.Header.grid(row=0,column=1)
        [[self.buttonmaker(i,j) for i in range(self.owner.Mfsize[0])] for j in range(self.owner.Mfsize[1])]

    def buttonmaker(self,i,j):
        pos=(i,j)
        field = tk.Button(self ,image = self.owner.tileimages[self.valtoim(self.m.Mf[i,j])],highlightthickness=1)
        field.bind('<Button-1>', lambda x, pos=pos,f=field:self.onclick(f,pos,1))
        field.bind('<Button-3>', lambda x, pos=pos,f=field:self.onclick(f,pos,2))
        field.bind('<ButtonRelease-3>', lambda x,f=field:f.configure(relief="raised"))
        field.grid(row=i+2, column=j+1)
        return field
    
    def onclick(self,button,pos,lr):
        if lr==1:
            if self.owner.firstmove:
                self.owner.firstmove=False
                self.m=Minesweeper(self,self.owner.Mfsize,self.owner.bombs,pos) 
            self.m.openup(pos)
        elif lr==2:
            button.configure(relief="sunken")
            self.m.flag(pos)
            
    def paint(self,pos):
        (i,j)=pos
        self.buttonmaker(i,j).grid(row=i+2, column=j+1)
            
    def valtoim(self,c):
        if c<10:
            return 0
        elif c<20:
            return 11
        elif c>20:
            return int(c-20)
        elif c==20:
            return 10


# In[4]:


class Pagemaneger(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.firstmove=True
        self.time1=0
        self.time2=0
        self.counter=0
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        
        self.setvariables()
        self.geometry('%sx%s' % (self.fw, self.fh))
        self.getimages()
        self.frames = {}
        
        for screen in [StartScreen,GameScreen]:
            frame = screen(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[screen] = frame
            
        
        #self.bind("<Enter>",self.resizewindow)
        self.show_frame(StartScreen)
        
    def setvariables(self):
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.fw=int(self.screenwidth/1.5)
        self.fh=int(self.screenheight/1.3)
        
        #self.Mfsize=(12,12)
        self.bombs=12
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.currentscreen=cont
        
    def getimages(self):
        #Images For GameScreen
        self.himage = Image.open('/home/alexander/Pictures/test/Header.png')
        #self.headerim= ImageTk.PhotoImage(self.himage)
        
        #Images For GameScreen
        self.himage2 = Image.open('/home/alexander/Pictures/test/Header2.png')
        #self.headerim2= ImageTk.PhotoImage(self.himage2)
            
        self.images=[Image.open('/home/alexander/Pictures/test/Msw'+str(x)+'.png') for x in range(12)]
        #self.tileimages=[ImageTk.PhotoImage(img) for img in self.images]
            
    def resizestuff(self,t):
        #Images For GameScreen
        if t==1:
            self.himager = self.himage.resize((self.fw, int(self.fh/2)), Image.ANTIALIAS)
            self.headerim= ImageTk.PhotoImage(self.himager)
        
        #Images For GameScreen 
        elif t==2:
            print("hello")
            self.ss=int(np.min((self.fw/self.Mfsize[0]-3,self.fh/self.Mfsize[1]-3))/1.25)
            self.imagesresized=[img.resize((self.ss,self.ss), Image.ANTIALIAS) for img in self.images]
            self.tileimages=[ImageTk.PhotoImage(img) for img in self.imagesresized]
            
            self.himage2r = self.himage2.resize((self.fw, int(self.fh/10)), Image.ANTIALIAS)
            self.headerim2= ImageTk.PhotoImage(self.himage2r)

            
    def resizewindow(self,event):
        a,b=(self.winfo_width(),self.winfo_height())
        if a>100 and b>100:
            self.fw ,self.fh =a,b
        fontsize=min(40,int(min(self.fh,self.fw)/16)+1)
        self.frames[self.currentscreen].draw()
        
        
        
app=Pagemaneger()
app.mainloop()
