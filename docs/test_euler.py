import matplotlib.pyplot as plt
import numpy as np

# Configurar estética básica si es posible
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    pass

# Solución exacta para la visualización
def y_exact(x):
    return np.sin(x) + 0.5*x - 0.5

# Derivada y'(x) = f(x, y) => y' = cos(x) + 0.5
def f_ode(x, y):
    return np.cos(x) + 0.5

# Grilla continua para la solución exacta
x = np.linspace(0, 4, 400)
y = y_exact(x)

# Configuración del Método de Euler
x0 = 0
y0 = y_exact(x0)
h = 1.0  # Paso grande para evidenciar el error
steps = 4

x_euler = [x0]
y_euler = [y0]

# Calcular pasos de Euler
cx, cy = x0, y0
for _ in range(steps):
    slope = f_ode(cx, cy)
    cy += slope * h
    cx += h
    x_euler.append(cx)
    y_euler.append(cy)

# Graficar
plt.figure(figsize=(10, 6))

# Solución exacta
plt.plot(x, y, label='Solución Exacta $y(x)$', color='#007acc', linewidth=2)

# Aproximación de Euler
plt.plot(x_euler, y_euler, 'o-', label='Aproximación de Euler', color='#d62728', linewidth=1.5, markersize=6)

# Dibujar vectores de pendiente o líneas tangentes fantasmas para ilustrar
for i in range(len(x_euler)-1):
    xi, yi = x_euler[i], y_euler[i]
    slope = f_ode(xi, yi)
    # Dibujar una pequeña línea tangente real en el punto (xi, yi) de la curva (si estuviéramos sobre la curva)
    # Pero Euler usa la pendiente en (xi, yi) actual.
    # El segmento rojo YA ES la tangente desde (xi, yi)
    pass

plt.axhline(0, color='black', linewidth=0.5, alpha=0.5)
plt.axvline(0, color='black', linewidth=0.5, alpha=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Método de Euler: Aproximación por Recta Tangente', fontsize=14)
plt.legend(frameon=True, fancybox=True, framealpha=0.9)

# plt.show()
print("Euler plot generated successfully")
