

import numpy as np


class Satellite:

	def __init__(self, m, p, v=[0, 0], a=[0, 0], name=None):
		self.m = float(m)       # mass
		self.p = np.asarray(p, dtype=float)  # position
		self.v = np.asarray(v, dtype=float)  # velocity
		self.a = np.asarray(a, dtype=float)  # acceleration
		self.name = str(name)

	def __repr__(self):
		return f'Satellite(m={self.m}, p={self.p}, v={self.v}, a={self.a})'


class SolarSystem:
	g = 6.674e-11  # universal graviational constant

	def __init__(self, sats):
		self.sats = sats  # np array of satellites
		self.time = 0.0

	@classmethod
	def force(cls, sat_a, sat_b, g=None):
		if g is None:
			g = cls.g
		r = np.linalg.norm(sat_b.p - sat_a.p)  # euclidian distance
		diff_uv = (sat_b.p - sat_a.p) / r
		f = (g * sat_a.m * sat_b.m / r ** 2) * diff_uv
		return f

	def update(self, dt):
		forces = []

		for sat_a in self.sats:
			f = 0
			for sat_b in self.sats:
				if sat_a is sat_b:
					continue
				f += self.force(sat_a, sat_b)
			forces.append(f)

		for f, sat in zip(forces, self.sats):
			sat.a = f / sat.m
			sat.v = sat.v + sat.a * dt
			sat.p = sat.p + sat.v * dt
		self.time += dt


def vec(a, b):
	return np.array([a, b])


def main():
	a = Satellite(1, vec(0, 0))
	b = Satellite(1, vec(3, 4))
	s = SolarSystem(np.array([a, b]))
	
	res = SolarSystem.force(a, b)
	print(res)
	print(np.linalg.norm(res))


if __name__ == '__main__':
	main()
