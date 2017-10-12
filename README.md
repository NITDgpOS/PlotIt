# PlotIt

A terminal based tool to visualise mathematical functions.

## Installation

- Clone the repository using ``` git clone https://github.com/djmgit/PlotIt.git ```
- Enter into the repository and open in terminal
- Run ``` pip install -r requirements.txt ``` This will install the only dependency (as of now) that is
  matplotlib, a python librarty to visualise graphs.

Thats it, you are all set to go !!

## Using PlotIt

At present PlotIt takes 4 command line arguments and can be executed as shown below.

```
python plotit.py -f '[function]' -s [starting_abcissa] -e [ending_abcissa] -z [step_size]

```

It is to be noted that if function contins more than one term for eg ``` x**2 + x ``` then function
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

## Future Milestones

- Allowing user to customise plot
- Allowing user to plot multiple functions
- Adding a config (perhaps json) file to configure the app and visualisations
- Creating an interactive shell
- Creating a GUI

