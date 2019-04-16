import sympy as sy
import numpy as np
from mpmath import nsum
from sympy import sin,cos

n=1 #Number of Pendulums-1
g=9.8 #Acceleration of Gravity

#Defining sympy Variables
#m=mass,l=lenght, y=angle of pendel, v=speed, a=acceleration, t=time
m=list(sy.symbols('m0:%d'%(n+1)))
l=list(sy.symbols('l0:%d'%(n+1)))
y=list(sy.symbols('y0:%d'%(n+1)))
v=list(sy.symbols('v0:%d'%(n+1)))
a=list(sy.symbols('a0:%d'%(n+1)))
t=sy.symbols('t')


#The differential Equations of a Multipendulum can be calulated using the Lagrange Formalism (In short it states that d/dt*(dL/dy')-dL/dy=0)
#L=T-V where T is Kinetik Energy, V is Potential Energy. For more information see: https://de.wikipedia.org/wiki/Multipendel

###nsum iterates over mpf (instead of integers) and mpf cant be used as List indices. Rather ugly code :( fix if possible # Does not seem to be possible
V=g*nsum(lambda k: m[int(k)]*nsum(lambda i:-l[int(i)]*sy.cos(y[int(i)]),[0,k]),[0,n])
def ugly1(k):
    return nsum(lambda i: l[int(i)]*v[int(i)]*sy.cos(y[int(i)]),[0,k])
def ugly2(k):
    return nsum(lambda i: l[int(i)]*v[int(i)]*sy.sin(y[int(i)]),[0,k])
T=1/2*nsum(lambda k: m[int(k)]*(ugly1(k)**2+ugly2(k)**2),[0,n])
L=T-V 


#Differentiating L as nessersary for the Lagrangeformalism
Ldy = np.array([*map(lambda x:L.diff(x),y)])
Tdv = np.array([*map(lambda x:T.diff(x),v)]) #Since V is indipentent of the v's, only T has to be differentiated


#Substituting variables with Derivatives sothat I can differentiate Tdv by t
for i in range(len(Tdv)):
    s=Tdv[i]
    #v=y'(t)
    s=s.subs(list(map(lambda k:(v[k],y[k](t).diff(t)),range(n+1))))
    #a=y''(t)
    s=s.subs(list(map(lambda k:(a[k],y[k](t).diff(t,t)),range(n+1))))
    #y=y(t)
    s=s.subs(list(map(lambda k:(y[k],y[k](t)),range(n+1))))
    Tdv[i]=s

#Differentiate Tdv by t
Tdvdt=np.array([*map(lambda x:x.diff(t),Tdv)])

Lagrangev=Tdvdt-Ldy #This is Matrix holds a list of n+1 linear equations in a0,a1,a2

#Substituting Derivatives back into Variables 
for i in range(len(Lagrangev)):
    s=Lagrangev[i]
    #y''(t)=a    
    s=s.subs(list(map(lambda k:(y[k](t).diff(t,t),a[k]),range(n+1))))
    #y'(t)=v
    s=s.subs(list(map(lambda k:(y[k](t).diff(t),v[k]),range(n+1))))
    #y(t)=y
    s=s.subs(list(map(lambda k:(y[k](t),y[k]),range(n+1))))
    Lagrangev[i]=s
    

###This part takes ages but technically this function only has to be called once anyway and having a nice form speeds up fruther computation
print("This part takes ages but technically this function only has to be called once anyway and having a nice form speeds up fruther computation")
Lagrangev=sy.simplify(sy.Matrix(Lagrangev))
#Lagrangev holds a list of n+1 (in regard to a) linear equations.
#If we substitute numerical constants in for l,m,v,y they can be solved quite quickly.

#Saving Lagrangev to file 
f = open('eqations'+str(n+1)+'.py', 'w' )
f.write(str(Lagrangev))
f.close()
