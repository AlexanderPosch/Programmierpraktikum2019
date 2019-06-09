import tkinter as tk 

class Spiel:
    def __init__(self , parent): 
        self.parent=parent
        self.images=[tk.PhotoImage(file='/home/alexander/Pictures/test/Msw'+str(x)+'.png') for x in range(12) ]
        
    def newgame(self):# Maybee make frame for this center and all
        self.Mfsize=(12,12)
        self.bombs=35
        
        self.Header=tk.Label(root,text="#### Minesweeper ####")
        self.rb1 = tk.Radiobutton(root ,text="Beginner",variable=self.Mfsize , value=(5,5)) 
        self.rb2 = tk.Radiobutton(root ,text="Advanced",variable=self.Mfsize , value=(12,12)) 
        self.rb3 = tk.Radiobutton(root ,text="Expert",variable=self.Mfsize , value=(20,20))
        self.rb2.select()
        self.Header.grid(row=0, column=0)
        self.rb1.grid(row=1, column =0)
        self.rb2.grid(row=2, column =0)
        self.rb3.grid(row=3, column =0)
        
        self.button = tk.Button(self.parent,text='Play', command=self.play)
        self.button.grid(row=4, column =0)#pack()

    def onclick(self,button,pos,lr):
        if lr==1:
            if not self.real:
                self.real=True
                self.m=Minesweeper(self,self.Mfsize,self.bombs,pos) 
            self.m.openup(pos)
        elif lr==2:
            button.configure(relief="sunken")
            self.m.flag(pos)
    def valtoim(self,c):
        if c<10:
            return 0
        elif c<20:
            return 11
        elif c>20:
            return int(c-20)
        elif c==20:
            return 10
    #def v2(self):
    #    np.array([self.vatoim(s) for s in self.m.Mf]).respape(self.Mfsize)
    #    
    
    def play(self):
        
        #delete old wigets (using frames is probably nicer dont know if frame does that though)
        self.rb1.grid_remove()
        self.rb2.grid_remove()
        self.rb3.grid_remove()
        self.button.grid_remove()
        self.Header.grid_remove()       
        
        self.m=Minesweeper(self,self.Mfsize,self.bombs,(0,0)) #make provisoric minefield new one is created at fist click
        self.real=False
        for i in range(self.Mfsize[0]):
            for j in range(self.Mfsize[1]):
                pos=(i,j)
                tk.field = tk.Button(self.parent,image = self.images[self.valtoim(self.m.Mf[i,j])])
                
                tk.field.bind('<Button-1>', lambda x, pos=pos,f=tk.field:self.onclick(f,pos,1))
                tk.field.bind('<Button-3>', lambda x, pos=pos,f=tk.field:self.onclick(f,pos,2))
                tk.field.bind('<ButtonRelease-3>', lambda x,f=tk.field:f.configure(relief="raised"))
                tk.field.grid(row=i, column=j)
        

        
root = tk.Tk() 
s=Spiel(root)
s.newgame()
root.mainloop()
