import math
import matplotlib.pyplot as plt

def process_function(func):
	# add more transformations here

	func = func.replace('sin', 'math.sin')
	func = func.replace('cos', 'math.cos')
	func = func.replace('exp', 'math.exp')
	func = func.replace('sqrt', 'math.sqrt')
	func = func.replace('factorial', 'math.factorial')
	func = func.replace('pi', 'math.pi')
	func = func.replace('e', 'math.e')

	return func

def create_y_values(func, xvals):
	# create function ordinate values

	yvals = []
	for x in xvals:
		yval = eval(func)
		yvals.append(yval)
	return yvals

def plot(func, xstart, xend, step):
	# show plot summary

	print '***** Plot Summary *****'
	print 'Funtion: {}'.format(func)
	print 'starting abcissa: {}'.format(xstart)
	print 'ending abcissa: {}'.format(xend)
	print 'step size: {}'.format(step)

	# preprocess function

	func = process_function(func)

	xvals = []
	i = xstart
	while i <= xend:
		xvals.append(i)
		i += step
	yvals = create_y_values(func, xvals)

	plt.plot(xvals, yvals, linewidth=2.0)
	plt.grid(True)
	plt.show()
