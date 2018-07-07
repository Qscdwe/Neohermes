from render_controller import Render_Controller
import numpy as np

rc = Render_Controller(400, 0, 10)
while True:
	rc.render([np.random.uniform()*10 for _ in range(1)])
	