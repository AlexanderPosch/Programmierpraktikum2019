import sympy as sy
import numpy as np
from mpmath import nsum
from sympy import sin,cos

n=0# Number of pendels -1
dt=0.025
time=5
timesteps=int(time/dt)

g=9.8 #Acceleration of Gravity
t=sy.symbols('t') #time

#Defining Variables
#m=mass,l=lenght, y=angle of pendel, v=speed, a=acceleration
m=list(sy.symbols('m0:%d'%(n+1)))
l=list(sy.symbols('l0:%d'%(n+1)))
y=list(sy.symbols('y0:%d'%(n+1)))
v=list(sy.symbols('v0:%d'%(n+1)))
a=list(sy.symbols('a0:%d'%(n+1)))

#L=T(...)-V(...) (lagrange Formalism)
#T is kinetik Energy, V is Potential Energy
V=g*nsum(lambda k: m[int(k)]*nsum(lambda i:-l[int(i)]*sy.cos(y[int(i)]),[0,k]),[0,n])
def ugly1(k):
    return nsum(lambda i: l[int(i)]*v[int(i)]*sy.cos(y[int(i)]),[0,k])
def ugly2(k):
    return nsum(lambda i: l[int(i)]*v[int(i)]*sy.sin(y[int(i)]),[0,k])
T=1/2*nsum(lambda k: m[int(k)]*(ugly1(k)**2+ugly2(k)**2),[0,n])
L=T-V 

#Here I differentiate L and T as nessersary for the Lagrangeformalism
Ldy = np.array([*map(lambda x:sy.simplify(L.diff(x)),y)])
Tdv = np.array([*map(lambda x:sy.simplify(T.diff(x)),v)])
               

#Redefing variables so I can differentiate Tdv by t (todo: allow n variables)
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
#This works but is kinda bad code
Tdvdt=np.array([*map(lambda x:x.diff(t),Tdv)])

#This is ugly simpify for n variables
Lagrangev=Tdvdt-Ldy
for i in range(len(Lagrangev)):
    s=Lagrangev[i]
    #y''(t)=a
    s=s.subs(list(map(lambda k:(y[k](t).diff(t,t),a[k]),range(n+1))))
    
    #y'(t)=v
    s=s.subs(list(map(lambda k:(y[k](t).diff(t),v[k]),range(n+1))))

    #y(t)=y
    s=s.subs(list(map(lambda k:(y[k](t),y[k]),range(n+1))))
    Lagrangev[i]=s


Lagrangev=sy.Matrix(Lagrangev)
print("hi")
