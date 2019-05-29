import tkinter as tk 

class Spiel:
    def __init__(self , parent): 
        wert=1
        self.rb1 = tk.Radiobutton(root ,text="Beginner",variable=wert , value=1) 
        self.rb2 = tk.Radiobutton(root ,text="Advanced",variable=wert , value=2) 
        self.rb3 = tk.Radiobutton(root ,text="Expert",variable=wert , value=3)
        self.rb2.select()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        self.button = tk.Button(root ,text='Play', command=self.z)
        self.button.pack()
    def z(self):
        pass
    def play(self, size):
        ##draw Minefield
        ## get fist position to create mf
        ##
        
        #for i in (matrix)
        #   mach eine Buton mit richtigen bild an stelle position
        #   
       


img = tk.PhotoImage(file='Z:\Programmierpraktikum\Bilder\\test2.png')
panel = tk.Label(image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()




root = tk.Tk() 
frame=tk.Frame(root, 100, 100)
s=Spiel(root)
