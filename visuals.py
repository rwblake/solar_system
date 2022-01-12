

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import numpy as np


import solar_system as ss


style.use('dark_background')

satellites = [
	ss.Satellite(1.989e30, (0, 0), name='sun'),
	ss.Satellite(3.301e23, (5.791e10, 0), (0, 4.736e4), name='mercury'),
	ss.Satellite(4.868e24, (1.082e11, 0), (0, 3.502e4), name='venus'),
	ss.Satellite(5.972e24, (1.520e11, 0), (0, 2.977e4), name='earth'),
	ss.Satellite(6.417e23, (2.279e11, 0), (0, 2.401e4), name='mars'),
	#ss.Satellite(1.898e27, (7.786e11, 0), (0, 1.307e4), name='jupiter'),
	#ss.Satellite(5.683e26, (1.434e12, 0), (0, 9.680e3), name='saturn'),
	#ss.Satellite(8.681e25, (2.875e12, 0), (0, 6.800e3), name='uranus'),
	#ss.Satellite(1.024e26, (4.504e12, 0), (0, 5.430e3), name='neptune'),

	#ss.Satellite(825.5, (1.830e13, 0), (1.534e4, 0), name='voyager 2')
]
s = ss.SolarSystem(satellites)
points = [[] for i in satellites]


def animate(i):
	for i in range(1):
		s.update(250000)
	plt.cla()  # clear plot
	for idx, satellite in enumerate(satellites):
		points[idx].append(list(satellite.p))
		plt.plot([i[0] for i in points[idx]], [i[1] for i in points[idx]])
		plt.plot(satellite.p[0], satellite.p[1], marker='o')
		plt.annotate(satellite.name, (satellite.p[0], satellite.p[1]), textcoords='offset points', xytext=(0,10), ha='center')

ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.show()
