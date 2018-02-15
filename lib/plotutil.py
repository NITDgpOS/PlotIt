import os
import re
from math import *
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from matplotlib import colors as mcolors
import traceback


def create_y_values(func, xvals):

    # Create function ordinate values
    yvals = []
    for x in xvals:
        try:
            yval = eval(func)
            yvals.append(yval)
        except Exception:
            print("Function cannot be evaluated for x =", x)
            return
    return yvals


def plot(func, xpoints, color_name, xlabel, ylabel, theme, gui, line_style, file_path, discrete=False):

    # Show plot summary
    print('***** Plot Summary *****')
    print("Funtion: {}".format(func))

    if discrete:
        print("Plotting funcion for points: {}".format(', '.join(map(str, xpoints))))
    else:
        print("Starting abcissa: {}".format(xpoints[0]))
        print("Ending abcissa: {}".format(xpoints[-1]))
        if (len(xpoints) > 1):
            print("Stepsize: {}".format(xpoints[1] - xpoints[0]))

    print("Color: {}".format(color_name))
    print("X-label: {}".format(xlabel))
    print("Y-label: {}".format(ylabel))
    print()

    if theme == 'dark':
        mplstyle.use('dark_background')
    else:
        mplstyle.use('default')

    xvals = xpoints
    yvals = create_y_values(func, xvals)

    try:
        # Check if color is hex code
        is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_name)
        if not is_hex:
            colors = mcolors.cnames
            if color_name not in colors:
                print(color_name, ": Color not found.")
                color_name = 'blue'
        plt.plot(xvals, yvals, color=color_name, linewidth=2.0, linestyle=line_style)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(r'$ ' + func + ' $')

    except Exception:
        print("An error occured.")
        print(traceback.format_exc())
    
    if file_path != "":
        plt.savefig(file_path)

    plt.grid(True)

    if not gui:
        plt.show()
    else:
        if not os.path.exists('.temp/'):
            os.mkdir('.temp/')
        plt.savefig(".temp/generated_plot.png")

    plt.cla()
    plt.clf()


def plot_line(arrays, color_name, xlabel, ylabel, theme, gui, line_style, file_path):

    # Show plot summary
    print('***** Plot Summary *****')
    print('Arrays: {}'.format(arrays))
    print('Color: {}'.format(color_name))
    print('X-label: {}'.format(xlabel))
    print('Y-label: {}'.format(ylabel))

    if theme == 'dark':
        mplstyle.use('dark_background')
    else:
        mplstyle.use('default')

    try:
        # Check if color is hex code
        is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_name)
        if not is_hex:
            colors = mcolors.cnames
            if color_name not in colors:
                print(color_name, ": Color not found.")
                color_name = 'blue'

        # Extract numbers from X-array
        xvals = list(map(float, arrays[1:arrays.find(']')].split(',')))
        # Extract numbers from Y-array
        yvals = list(map(float,
                         arrays[arrays.find(']') + 3:len(arrays) - 1].split(',')))

        if len(xvals) == len(yvals):
            plt.plot(xvals, yvals, color=color_name, linewidth=2.0, linestyle=line_style)
            plt.savefig(file_path)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(r'$ ' + 'Line:' + str(xvals) +','+ str(yvals) + ' $')
            
            if file_path != "":
                plt.savefig(file_path)
        
        else:
            print("Error: You need same number of X and Y values")

    except Exception:
        print("An error occured.")
    
    if file_path != "":
        plt.savefig(file_path)
    
    plt.grid(True)

    if not gui:
        plt.show()
    else:
        if not os.path.exists('.temp/'):
            os.mkdir('.temp/')
        plt.savefig(".temp/generated_plot.png")


    plt.cla()
    plt.clf()

def plot_dot(xyval, color_name, xlabel, ylabel, theme, gui, dot_style, file_path):

    # Show plot summary
    print('***** Plot Summary *****')
    print('X,Y Value: {}'.format(xyval))
    print('Color: {}'.format(color_name))
    print('X-label: {}'.format(xlabel))
    print('Y-label: {}'.format(ylabel))

    if theme == 'dark':
        mplstyle.use('dark_background')
    else:
        mplstyle.use('default')

    try:
        # Check if color is hex code
        is_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_name)
        if not is_hex:
            colors = mcolors.cnames
            if color_name not in colors:
                print(color_name, ": Color not found.")
                color_name = 'blue'

        xy=xyval.split(',')
        l=len(xy)
        #Check if even number of arguments are given
        if (l%2==0):
            #Extract x-values from xyval string
            xval=[float(xy[i]) for i in range(0,l,2)]
            #Extract y-values from xyval string
            yval=[float(xy[i]) for i in range(1,l+1,2)]
        
            plt.scatter(xval, yval, color=color_name, marker=dot_style)
            plt.savefig(file_path)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(r'$ ' + xyval + ' $')

            if file_path != "":
                plt.savefig(file_path)
            
            plt.grid(True)

            if not gui:
                plt.show()
            else:
                if not os.path.exists('.temp/'):
                    os.mkdir('.temp/')
                plt.savefig(".temp/generated_plot.png")           
        else:
            print("Cannot plot odd Number of Coordinates")
        
    except Exception as e:
        print("An error occured.",e)
    
    plt.cla()
    plt.clf()