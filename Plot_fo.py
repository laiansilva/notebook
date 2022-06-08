import numpy as np
import sympy as sp

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

niter=20
f_obj1 = np.zeros((niter, 1))
f_obj2 = np.zeros((niter, 1))
f_obj3 = np.zeros((niter, 1))

aux = open("fhistory_viscoacoustic_multi_parameter_CG_r10x10.txt", "r")
f_obj1=aux.read()
aux.close()

aux = open("fhistory_viscoacoustic_multi_parameter_CG_r20x20.txt", "r")
f_obj2=aux.read()
aux.close()

aux = open("fhistory_viscoacoustic_multi_parameter_CG_r40x40.txt", "r")
f_obj3=aux.read()
aux.close()

a=[]
b=[]

c=[]
d=[]

e=[]
f=[]

for i in f_obj1.split():
     a.append(float(i))
     
for i in f_obj2.split():
     c.append(float(i))
     
for i in f_obj3.split():
     e.append(float(i))     

b=a[1]
d=c[1]
f=e[1]

for i in range(niter):
#    a[i]=np.log(a[i])/np.log(b)
#    c[i]=np.log(c[i])/np.log(d)
#    e[i]=np.log(e[i])/np.log(f)
# Normalizado
    a[i]= a[i]/b
    c[i]= c[i]/d
    e[i]= e[i]/f
      
plt.figure()
x=np.linspace(2, 20, 19)
plt.plot(x, a[1:])
plt.plot(x, c[1:])
plt.plot(x, e[1:])
plt.xlabel('Number of iterations')
plt.ylabel('Normalized data residual')
plt.title('Convergence plots for erros in $\\tau$')
plt.legend(['$\epsilon=17\%$', '$\epsilon=23\%$','$\epsilon=27\%$'],fontsize=15)
# # plt.title('Convergence')
plt.savefig('FO_multpar_comparative.pdf', dpi=200) 











