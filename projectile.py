import numpy as np
import matplotlib.pyplot as plt

v = 10
angle = 45 * np.pi / 180
g = 0

t = np.linspace(0, 3, 100)

x = v * np.cos(angle) * t
y = v * np.sin(angle) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel("Distance")
plt.ylabel("Height")
plt.title("Projectile Motion")
plt.show()
end
