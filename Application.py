#dummy. dummy

import matplotlib.pyplot as plt
import numpy as np
from Base_code import LagrangeInterpolation 

#(a)
#Funktion nach beginn von (b) angepasst
def gen_support_nodes(n, a, b):
    return np.linspace(a, b, n + 1)


def gen_func_values(func, x):
    return func(np.array(x))


n_values_a = [1, 2, 3, 4]
plot_arr = np.linspace(0, np.pi, 100)
real_vals = np.sin(plot_arr)
sinus = np.sin

#plotten der Interpolationspolynome
for current_n in n_values_a:
    current_nodes = gen_support_nodes(current_n, 0, np.pi)
    current_vals = gen_func_values(sinus, current_nodes)

    pol = LagrangeInterpolation(current_nodes, current_vals)
    pol_vals = pol(plot_arr)

    plt.plot(plot_arr, pol_vals, label=f"n={current_n}")


plt.plot(plot_arr, real_vals, label=f"f(x) = sin(x)", color='black', linestyle='--')
plt.legend()
plt.show()

#(b)
#(i) sin(x)
test_nodes = np.linspace(-5, 5, 1001)
sin_errors = []
real_test_vals = np.sin(test_nodes)
n_values_b = range(1, 101)

for current_n in n_values_b:
    current_nodes = gen_support_nodes(current_n, -5, 5)
    current_vals = gen_func_values(sinus, current_nodes)
    
    pol = LagrangeInterpolation(current_nodes, current_vals)
    pol_vals = pol(test_nodes)
    
    #diskrete maximumsnorm
    current_error = np.max(np.abs(real_test_vals - pol_vals))
    sin_errors.append(current_error)


plt.figure() 
plt.plot(n_values_b, sin_errors, marker='o', markersize=2, label='Max. Fehler ||f - pn||')
#logarithmische skalierung der fehler
plt.yscale('log') 
plt.xlabel('Grad des Polynoms n')
plt.ylabel('Maximaler Fehler (log)')
plt.title('Fehlerentwicklung der Lagrange-Interpolation auf [-5, 5]')
plt.grid(True, which="both", ls="-", alpha=0.5) 
plt.legend()
plt.show()

#(ii) (1 + x^2)^(-1)
def new_func(x):
    return (1 / (1 + x**2))

new_test_vals = new_func(test_nodes)
new_errors = []

for current_n in n_values_b:
    current_nodes = gen_support_nodes(current_n, -5, 5)
    current_vals = gen_func_values(new_func, current_nodes)
    
    pol = LagrangeInterpolation(current_nodes, current_vals)
    pol_vals = pol(test_nodes)
    
    current_error = np.max(np.abs(new_test_vals - pol_vals))
    new_errors.append(current_error)

plt.figure() 
plt.plot(n_values_b, new_errors, marker='o', markersize=2, label='Max. Fehler ||f - pn||')
plt.yscale('log') 
plt.xlabel('Grad des Polynoms n')
plt.ylabel('Maximaler Fehler (log)')
plt.title('Fehlerentwicklung der Lagrange-Interpolation auf [-5, 5]')
plt.grid(True, which="both", ls="-", alpha=0.5) 
plt.legend()
plt.show()