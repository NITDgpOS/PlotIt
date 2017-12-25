# PlotIt


![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg "Made with Python")


**A terminal based tool to visualise mathematical functions.**<br>

![alt text](images/GUImani.png "main GUI")

![alt text](images/GUI.png "GUI interface")

## Dependencies

- Matplotlib
- Pillow
- ImageTk
- Tkinter

## Installation

- Clone the repository using ``` git clone https://github.com/djmgit/PlotIt.git ```
- Enter into the repository and open in terminal
- Run ``` pip install -r requirements.txt ``` This will install the only dependency (as of now) that is
  matplotlib, a python librarty to visualise graphs and PIL. If it is not working and is showing
  permission denied error, then try ``` sudo pip install -r requirements.txt ```.
- Tkinter library is required for GUI components, if it is not already installed then install it
  using
  ```
  sudo apt-get install python-tk
  ```
- The project requires ImageTk. If it is not already installed then install it using
  ```
  sudo apt-get install python-imaging-tk
  ```

Thats it, you are all set to go !!

## Using PlotIt

At present PlotIt takes 4 command line arguments and can be executed as shown below.

```
python plotit.py -f '[function]' -s [starting_abcissa] -e [ending_abcissa] -z [step_size]

```

It is to be noted that if function contains more than one term for eg ``` x**2 + x ``` then function
should be under single quotes.
Default values of starting abcissa, ending abcissa and step size are 0, 100  and 1.0 respectively

### Some examples

```
python plotit.py -f 'sin(x)'

python plotit.py -f 'x**2 + x'

python plotit.py -f cos(x)

python plotit.py -f 'x**3 + x**2 + x'

python plotit.py -f 'exp(x)'

```

### PlotIt GUI

PlotIt also provides a simple GUI to enter your function and visualise it. In order to use GUI instead
of terminal use the command given below.

```
python gui_main.py

```

Before going for GUI mode, make sure you have installed Tkinter, PIL and ImageTk as mentioned above.

## For contributors

If you want to contribute to this project then have a look [here](https://github.com/NIT-dgp/PlotIt/blob/master/CONTRIBUTING.md)

**PlotIt** uses Flake8 as a code-linter. Before you commit your code, check the code against the linter rules by running the following command from the `root` of the project.

```
flake8 .

```

If there are no violations, you are good to go! Otherwise you need to solve the violations before creating a pull request.

## Future Milestones

- Allowing user to customise plot
- Allowing user to plot multiple functions
- Adding a config (perhaps json) file to configure the app and visualisations
- Creating an interactive shell
- Enhancing GUI and adding more options
