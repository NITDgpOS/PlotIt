from lib import plotutil as plu
import optparse
import signal

#Defaults
xstart = 0
xend = 100
stepsize = 1.0
color = "blue"
xlabel = "X-axis"
ylabel = "Y-axis"

# handle case if user presses Ctrl + C, show proper message while shutting down

def sigint_handler(signum, frame):
    print('shutting down PlotIt...')
    exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# parse command line arguments and switches

parser = optparse.OptionParser()
parser.add_option('-f', '--function', dest='func', help='Enter function to visualise')
parser.add_option('-s', '--xstart', dest='xstart', help='Enter starting x-value')
parser.add_option('-e', '--xend', dest='xend', help='Enter ending x-value')
parser.add_option('-z', '--stepsize', dest='stepsize', help='Enter step size')
parser.add_option('-c', '--color', dest='color', help='Enter the color for plot')
parser.add_option('-x', '--xlabel',dest='xlabel', help='Enter the x-label for plot')
parser.add_option('-y', '--ylabel',dest='ylabel', help='Enter the y-label for plot')
parser.add_option('-l', '--line', dest='line', help='Enter 2 Arrays of X and Y Coordinates like [x1,x2,x3,...,xn],[y1,y2,y3,...,yn]')
parser.add_option('-t', '--theme', dest='theme', help='Enter theme for displaying plot (dark or light possible)')

(options, args) = parser.parse_args()

if not options.func and not options.line:
    print('Please enter a function or 2 arrays of x and y coordinates to visualise')
    exit(0)

if options.color:
    color = str(options.color)

if options.xlabel:
    xlabel = str(options.xlabel)

if options.ylabel:
    ylabel = str(options.ylabel)


if options.theme:
    theme = str(options.theme)
else:
    theme = 'default'

if options.func:
    func = options.func

    if options.xstart:
        xstart = int(options.xstart)

    if options.xend:
        xend = int(options.xend)

    if options.stepsize:
        stepsize = int(options.stepsize)

    plu.plot(func, xstart, xend, stepsize, color, xlabel, ylabel, theme, False)

else: #no function try to take points for line
    xypoints = options.line
    plu.plot_line(xypoints, color, xlabel, ylabel, theme, False)

# visualise using matplotlib
