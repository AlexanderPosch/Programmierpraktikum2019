import sys
sys.path.append('D:\Python\site-packages') #so i have access to sympy (saved to my memorystick)
import sympy as sy
n=1 #Number of Pendulums
g=9.8 #Acceleration of Gravity

#Defining sympy Variables
#m=mass,l=lenght, y=angle of pendel, v=speed, a=acceleration, t=time
m=list(sy.symbols('m0:%d'%(n)))
l=list(sy.symbols('l0:%d'%(n)))
y=list(sy.symbols('y0:%d'%(n)))
v=list(sy.symbols('v0:%d'%(n)))
a=list(sy.symbols('a0:%d'%(n)))
t=sy.symbols('t')

#The differential Equations of a Multipendulum can be calulated using the Lagrange Formalism (In short it states that d/dt*(dL/dy')-dL/dy=0)
#L=T-V where T is Kinetik Energy, V is Potential Energy. For more information see: https://de.wikipedia.org/wiki/Multipendel
V=g*sum(map(lambda k: m[k]*sum(map(lambda i:-l[i]*sy.cos(y[i]),list(range(k+1)))),list(range(n))))
def ugly1(k):
    return sum(map(lambda i: l[i]*v[i]*sy.cos(y[i]),list(range(k+1))))
def ugly2(k):
    return sum(map(lambda i: l[i]*v[i]*sy.sin(y[i]),list(range(k+1))))
T=1/2*sum(map(lambda k: m[k]*(ugly1(k)**2+ugly2(k)**2),list(range(n))))
L=T-V 

#Differentiating L as nessersary for the Lagrangeformalism
Ldy = sy.Matrix([*map(lambda x:L.diff(x),y)])
Tdv = sy.Matrix([*map(lambda x:T.diff(x),v)]) #Since V is indipentent of the v's, only T has to be differentiated


#Substituting variables with Derivatives sothat I can differentiate Tdv by t
Tdv=Tdv.subs(list(map(lambda k:(v[k],y[k](t).diff(t)),range(n)))) #v=y'(t)
Tdv=Tdv.subs(list(map(lambda k:(a[k],y[k](t).diff(t,t)),range(n)))) #a=y''(t)
Tdv=Tdv.subs(list(map(lambda k:(y[k],y[k](t)),range(n)))) #y=y(t)

#Differentiate Tdv by t
Tdvdt=sy.Matrix([*map(lambda x:x.diff(t),Tdv)])
print(Tdvdt)
Lagrangev=Tdvdt-Ldy #This is Matrix holds a list of n linear equations in a0,a1,a2,... (here still in the form of second derivatives)

#Substituting Derivatives with Variables for clarity
Lagrangev=Lagrangev.subs(list(map(lambda k:(y[k](t).diff(t,t),a[k]),range(n)))) #y''(t)=a   
Lagrangev=Lagrangev.subs(list(map(lambda k:(y[k](t).diff(t),v[k]),range(n)))) #y'(t)=v
Lagrangev=Lagrangev.subs(list(map(lambda k:(y[k](t),y[k]),range(n)))) #y(t)=y

###This part takes ages but technically this function only has to be called once anyway and having a nice form speeds up further computation
print("This part takes ages but technically this function only has to be called once anyway and having a nice form speeds up fruther computation")
Lagrangev=sy.simplify(Lagrangev)

#Lagrangev holds a list of n (in regard to a) linear equations.
#If we substitute numerical constants in for l,m,v,y they can be solved quite quickly.

#Saving Lagrangev to file 
f = open('eqations'+str(n)+'.txt', 'w' )
f.write(str(Lagrangev))
f.close()
