## Getting involved

**PlotIt** is presently at its initial stages of development and we would love to have
contributors. So if you have found a bug or have a cool feature in mind which you want to
add, then please follow the steps given below to contribute to this project.

### Making your first pull request

Please open a **new issue** before making any pull request. **Every pull request should
have a reference to an issue.**

- First, fork this repository
- Clone it using ``` git clone https://github.com/[username]/PlotIt.git ```
- It is always recommended to make your changes in a new branch rather than master.
  So create a new branch using ``` git branch mybug ```
- Checkout into your new branch using ``` git checkout mybug ```
- Hack the code, kill the bug or introduce the new feature you had in mind,
  do all kinds of awesome stuff.
- After you are done add your changes using ``` git add --all```
- Commit your changes using ``` git commit ``` and provide a commit message.
- After you have committed your changes push your changes to your forked repository
  using ``` git push origin mybug ```
- Finally create a pull request from github.
- If everything is alright then soon your changes will get merged or else you will
  be asked to make changes.

There should be **only one commit per pull request**.

Please try to make sure that your commit message and body follows the
guidelines below.

- Commit message should be of the form : ``` fixes issue #[issue_number] - what you solved in one line ```
- After Commit message there should follow a commit body where you can mention what you
  did in short or in detail

Please try to follow this format as it will be helpful for maintainers as well as co-developers/contributors
to stay aligned.

## Resources

- This project uses Matplotlib as a core library to generate visualisations. Find more information on Matplotlib [here](https://matplotlib.org/users/pyplot_tutorial.html)

- The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images. Find more information on ImageTk [here](http://pillow.readthedocs.io/en/3.1.x/reference/ImageTk.html)

- Pillow is the library that adds support for opening, manipulating, and saving many different image file formats. Find more information on Pillow [here](http://www.pythonforbeginners.com/gui/how-to-use-pillow)

- Tkinter is the standard GUI library. Find more information on ImageTk [here](http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html)
