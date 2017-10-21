from lib import plotutil as plu
import optparse
import signal

#Defaults
xstart = 0
xend = 100
stepsize = 1.0
color = "blue"

# handle case if user presses Ctrl + C, show proper message while shutting down

def sigint_handler(signum, frame):
    print 'shutting down PlotIt...'
    exit(0)
 
signal.signal(signal.SIGINT, sigint_handler)

# parse command line arguments and switches

parser = optparse.OptionParser()
parser.add_option('-f', '--function', dest='func', help='Enter function to visualise')
parser.add_option('-s', '--xstart', dest='xstart', help='Enter starting x-value')
parser.add_option('-e', '--xend', dest='xend', help='Enter ending x-value')
parser.add_option('-z', '--stepsize', dest='stepsize', help='Enter step size')
parser.add_option('-c', '--color', dest='color', help='Enter the color for plot')

(options, args) = parser.parse_args()

if not options.func:
	print 'Please enter a function to visualise'
	exit(0)

func = options.func

if options.xstart:
	xstart = int(options.xstart)

if options.xend:
	xend = int(options.xend)

if options.stepsize:
	stepsize = int(options.stepsize)

if options.color:
	color = str(options.color)

# visualise using matplotlib

plu.plot(func, xstart, xend, stepsize, color,False)