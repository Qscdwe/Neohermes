import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()
ax = fig.add_subplot(111)

class Render_Controller:
	def __init__(self, fixed_size, max_value = 1, min_value = 0):
		self.fixed_size = fixed_size
		self.x = np.arange(fixed_size)
	
		self.y = np.ones(fixed_size) * min_value
		self.y[-1:] = max_value

		self.li, = ax.plot(self.x, self.y)
		ax.relim() 
		ax.autoscale_view(True,True,True)
		fig.canvas.draw()
		plt.show(block=False)
		self.render(self.y)

	def render(self, new_values):
		size = len(new_values)

		self.y[:-size] = self.y[size:]
		self.y[-size:] = new_values

		self.li.set_ydata(self.y)
		fig.canvas.draw()


if __name__ == "__main__":
	rc = Render_Controller(400, 0, 10)
	while True:
		rc.render([np.random.uniform()*10 for _ in range(1)])
	