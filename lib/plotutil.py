import os
from math import *
import matplotlib.pyplot as plt

def create_y_values(func, xvals):
	# create function ordinate values

	yvals = []
	for x in xvals:
		yval = eval(func)
		yvals.append(yval)
	return yvals

def plot(func, xstart, xend, step, gui):
	# show plot summary

	print '***** Plot Summary *****'
	print 'Funtion: {}'.format(func)
	print 'starting abcissa: {}'.format(xstart)
	print 'ending abcissa: {}'.format(xend)
	print 'step size: {}'.format(step)

	xvals = []
	i = xstart
	while i <= xend:
		xvals.append(i)
		i += step
	yvals = create_y_values(func, xvals)

	try:
		plt.plot(xvals, yvals, linewidth=2.0)
  	except:
		print('An error occured.')
	plt.grid(True)
	if not gui:
		plt.show()
	else:
		if not os.path.exists('.temp/'):
			os.mkdir('.temp/')
		plt.savefig(".temp/generated_plot.png")
	plt.cla()
	plt.clf()
