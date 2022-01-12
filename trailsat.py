

from solar_system import Satellite


class TrailSat(Satellite):
	"""satellite class with a history (trail) of locations"""

	def __init__(self, *args, **kwargs):
		self.trail_len = 100  # max length of trail
		self.trail = []
		super().__init__(*args, **kwargs)
		self.trail = [self.p]

	def __setattr__(self, prop, val):
		if prop == 'p':
			if len(self.trail) == self.trail_len:
				self.trail.pop(0)
			self.trail.append(val)
		super().__setattr__(prop, val)
	"""
	@property
	def p(self):
		return self.p

	@p.setter
	def p(self, new_p):
		if len(self.points) == self.trail_len:
			self.points.pop(0)
		self.points.append(self.p)

		self.p = new_p"""
