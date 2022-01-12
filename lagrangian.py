

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import numpy as np
from shapely.geometry import LineString


import solar_system as ss
import trailsat as ts


style.use('dark_background')

sun   = ts.TrailSat(1.989e30, (0, 0), name='sun')
earth = ts.TrailSat(5.972e24, (1.520e11, 0), (0, 2.977e4), name='earth')
moon  = ts.TrailSat(7.342e22, (1.520e11, 3844e5), (-1.022e3, 2.977e4), name='moon')

satellites = [sun, earth, moon]

s = ss.SolarSystem(satellites)


def intersected(obj, past_obj):
	if len(obj.trail) <= 2:
		return False
	a_line = LineString([obj.p, obj.trail[-2]])
	b_line = LineString(past_obj.trail)
	"""for i in range(len(past_obj.trail)-1):
		b_line = LineString([past_obj.trail[i], past_obj.trail[i+1]])
		if a_line.intersection(b_line):
			return True
	return False"""
	return a_line.intersection(b_line)

last_time = 0
times = []

def animate(i):
	global last_time
	s.update(25000)  # move time forward
	plt.cla()  # clear plot

	for sat in satellites:
		trailx, traily = zip(*reversed(sat.trail))
		plt.plot(trailx, traily)
		plt.plot(sat.p[0], sat.p[1], marker='o')
		plt.annotate(sat.name, (sat.p[0], sat.p[1]), textcoords='offset points', xytext=(0,10), ha='center')
	#plt.xlim(satellites[1].p[0]-1e9, satellites[1].p[0]+1e9)
	#plt.ylim(satellites[1].p[1]-1e9, satellites[1].p[1]+1e9)
	plt.axis('off')

	if intersected(moon, earth):
		if last_time != 0:
			time = s.time-last_time
			if time < 2000000:
				time = time * 2
			times.append(time)
			print(sum(times) / len(times))
		last_time = s.time


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.show()
