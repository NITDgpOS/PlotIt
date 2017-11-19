import os
import re
from math import *
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def create_y_values(func, xvals):
	# create function ordinate values

	yvals = []
	for x in xvals:
		try:
			yval = eval(func)
			yvals.append(yval)
		except:
			print "Function cannot be evaluated for x =",x
			return
	return yvals

def plot(func, xstart, xend, step, color_name, xlabel, ylabel, gui):
	# show plot summary

	print '***** Plot Summary *****'
	print 'Funtion: {}'.format(func)
	print 'starting abcissa: {}'.format(xstart)
	print 'ending abcissa: {}'.format(xend)
	print 'step size: {}'.format(step)
	print 'Color: {}'.format(color_name)
	print 'X-label: {}'.format(xlabel)
	print 'Y-label: {}'.format(ylabel)

	xvals = []
	i = xstart
	while i <= xend:
		xvals.append(i)
		i += step
	yvals = create_y_values(func, xvals)

	try:
		#check if color is hex code
		is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_name)
		if not is_hex:
			colors = mcolors.cnames
			if not color_name in colors:
				print color_name,": Color not found."
				color_name = 'blue'
		plt.plot(xvals, yvals, color=color_name, linewidth=2.0)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
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

def plot_line(arrays, color_name, xlabel, ylabel, gui):
	# show plot summary

	print '***** Plot Summary *****'
	print 'Arrays: {}'.format(arrays)
	print 'Color: {}'.format(color_name)
	print 'X-label: {}'.format(xlabel)
	print 'Y-label: {}'.format(ylabel)

	try:
		#check if color is hex code
		is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_name)
		if not is_hex:
			colors = mcolors.cnames
			if not color_name in colors:
				print color_name,": Color not found."
				color_name = 'blue'
		xvals = list(map(float, arrays[1:arrays.find(']')].split(','))) #extract numbers from X-array
		yvals = list(map(float,arrays[arrays.find(']')+3:len(arrays)-1].split(','))) #extract numbers from Y-array
		if len(xvals) == len(yvals):
			plt.plot(xvals, yvals, color=color_name, linewidth=2.0)
			plt.xlabel(xlabel)
			plt.ylabel(ylabel)
		else:
			print('Error: You need same number of X and Y values')
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
