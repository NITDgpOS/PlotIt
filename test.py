import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from matplotlib import colors as mcolors
import os
import re
from math import *
xstart = 0
xend = 100
stepsize = 1.0
color = "blue"
xlabel = "X-axis"
ylabel = "Y-axis"
line_style = "-"
dot_style="o"
dot_size=5
file_path = ""
theme='default'
# [img]https://i.imgur.com/U1nXSOL.png[/img]



def plot_dot(xyval, color_name, xlabel, ylabel, theme, gui, dot_style, dot_size,file_path):

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

        # # Extract numbers from X-array
        # xvals = list(map(float, arrays[1:arrays.find(']')].split(',')))
        # # Extract numbers from Y-array
        # yvals = list(map(float,
        #                  arrays[arrays.find(']') + 3:len(arrays) - 1].split(',')))

        #Extract x-value from xyval string
        xval=float(xyval.split(',')[0])
        #Extract y-value from xyval string
        yval=float(xyval.split(',')[1])

        
        plt.plot(xval, yval, color=color_name, markersize=dot_size, marker=dot_style)
        plt.savefig(file_path)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(r'$ ' + xyval + ' $')
        
        if file_path != "":
            plt.savefig(file_path)
        

    except Exception as e:
        print("An error occured.",e)
    
    # if file_path != "":
    #     plt.savefig(file_path)
    
    plt.grid(True)

    if not gui:
        plt.show()
    else:
        if not os.path.exists('.temp/'):
            os.mkdir('.temp/')
        plt.savefig(".temp/generated_plot.png")


    plt.cla()
    plt.clf()
# 3 things cjanged
plot_dot('5.3,9', color, xlabel, ylabel, theme, False, dot_style, dot_size, file_path)