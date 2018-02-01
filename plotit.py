from lib import plotutil as plu
import optparse
import signal

# Defaults
xstart = 0
xend = 100
stepsize = 1.0
color = "blue"
xlabel = "X-axis"
ylabel = "Y-axis"
line_style = "-"
dot_style = "o"
dot_size = 5
file_path = ""


# Handle case if user presses Ctrl+C, show proper message while shutting down
def sigint_handler(signum, frame):
    print('shutting down PlotIt...')
    exit(0)


signal.signal(signal.SIGINT, sigint_handler)

# Parse command line arguments and switches

parser = optparse.OptionParser()
parser.add_option('-f', '--function', dest='func',
                  help='Enter function to visualise')
parser.add_option('-s', '--xstart', dest='xstart',
                  help='Enter starting x-value')
parser.add_option('-e', '--xend', dest='xend',
                  help='Enter ending x-value')
parser.add_option('-z', '--stepsize', dest='stepsize',
                  help='Enter step size')
parser.add_option('-c', '--color', dest='color',
                  help='Enter the color for plot')
parser.add_option('-x', '--xlabel', dest='xlabel',
                  help='Enter the x-label for plot')
parser.add_option('-y', '--ylabel', dest='ylabel',
                  help='Enter the y-label for plot')
parser.add_option('-p', '--points', dest='xpoints',
                  help='Enter discrete x values for which the \
                  function will be plotted like [x1,x2,x3,...,xn]')
parser.add_option('-d', '--dot', dest='dot', help='Enter comma separated X and Y points like\
                   5,9 to plot a dot at x=5,y=9 coordinates.')
parser.add_option('-l', '--line', dest='line',
                  help='Enter 2 Arrays of X and Y Coordinates like \
                  [x1,x2,x3,...,xn],[y1,y2,y3,...,yn]')
parser.add_option('-t', '--theme', dest='theme',
                  help='Enter theme for displaying plot (dark or light)')
parser.add_option('--symbol', dest='line_style', 
                  help='Enter linestyle for plot, accepted linestyles "-", ":", "-.", "--"', 
                  choices=["-",":","-.","--"])
parser.add_option('--save', dest='file_path',
                  help='Enter file path eg: path/filename.png')

(options, args) = parser.parse_args()

if not options.func and not options.line and not options.dot:
    print('Please enter a function or 2 arrays of x and y coordinates or Coordinates of a single dot')
    exit(0)

if options.color:
    color = str(options.color)

if options.xlabel:
    xlabel = str(options.xlabel)

if options.ylabel:
    ylabel = str(options.ylabel)

if options.line_style:
    line_style = str(options.line_style)

if options.theme:
    theme = str(options.theme)
else:
    theme = 'default'

if options.file_path:
    file_path = str(options.file_path)


if options.func:
    func = options.func

    if options.xpoints and (options.xstart or options.xend or options.stepsize):
        parser.error("Can't use either of xstart, xend or stepsize \
                     with the option xpoints")
    elif options.xpoints:
        xpoints = list(map(float, options.xpoints[1:-1].split(',')))
        discrete = True
    else:
        if options.xstart:
            xstart = int(options.xstart)
        else:
            xstart = 0

        if options.xend:
            xend = int(options.xend)
        else:
            xend = 100

        if options.stepsize:
            stepsize = int(options.stepsize)
        else:
            stepsize = 1

        xpoints = range(xstart, xend + 1, stepsize)
        discrete = False

    plu.plot(func, xpoints, color, xlabel, ylabel, theme, False, line_style, file_path, discrete)

elif options.dot:
    xyval = options.dot
    plu.plot_dot(xyval, color, xlabel, ylabel, theme, False, dot_style, dot_size, file_path)

elif options.line:
    xypoints = options.line
    plu.plot_line(xypoints, color, xlabel, ylabel, theme, False, line_style, file_path)

# Visualise using matplotlib
