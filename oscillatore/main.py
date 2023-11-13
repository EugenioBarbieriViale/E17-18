# Oscillatore armonico


import matplotlib.pyplot as plt
import numpy as np
import pandas


N = 1000

# Costants
m = 0.5 # kg
Dt = 0.01 # s
g = 9.81 # m/s2
k = 10 # N/m
A = 10 # m
vi = 0 # m/s

# Arrays
n = range(0,N)
axis = range(0,N+1)

t = [x * Dt for x in axis]
x_in = [A]
v_in = [vi]
F = [-k*A]
a = [F[0]/m]
x_fin = []
v_fin = []

ki = [0.5*m*vi**2]
u = [0.5*k*A**2]
em = [ki[0]+u[0]]

# Variables
T = round(2 * np.pi * np.sqrt(m/k),4)
v_ang = np.sqrt(k/m)
x_th = [A]


for i in n:
    x_fin.append(x_in[i] + v_in[i] * Dt + 0.5 * a[i] * Dt**2)
    v_fin.append(v_in[i] + a[i] * Dt)

    F.append(-k * x_in[i])
    a.append(F[i]/m)

    x_in.append(x_fin[i])
    v_in.append(v_fin[i])

    x_th.append(A * np.cos(v_ang*t[i]))

    ki.append(0.5 * m * v_in[i]**2)
    u.append(0.5 * k * x_in[i]**2)
    em.append(ki[i] + u[i])


# Position graph
plt.figure()
plt.plot(axis,x_in, label="x_in")
plt.hlines(0,0,N,colors="black")

plt.title("Periodo: {}s".format(str(T)))
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(visible=True)
plt.legend()

# Position graph (and theoric)
plt.figure()

plt.plot(axis,x_in, label="x_in")
plt.plot(axis,x_th, label="x_th")

plt.hlines(0,0,N,colors="black")

plt.title("Periodo: {}s".format(str(T)))
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(visible=True)
plt.legend()

# Mechanical energy
plt.figure()
plt.plot(axis,em, label="em")
plt.hlines(0,0,N,colors="black")

plt.title("Energia meccanica")
plt.xlabel("t(s)")
plt.ylabel("e(J)")
plt.grid(visible=True)
plt.legend()

plt.show()
