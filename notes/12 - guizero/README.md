# Introduction to guizero

guizero is a Python 3 library for creating simple GUIs. Before following the steps below read the [Getting Started](https://lawsie.github.io/guizero/start/) section of the guizero [documentation](https://lawsie.github.io/guizero/about/).

## Step 1

Download the [starter code](https://github.com/pguse/ics3u-python/blob/master/notes/12%20-%20guizero/myGlossary.py).  Save the starter code in an appropriately name folder on your computer.

## Step 2

### Using Visual Studio Code

From within **Visual Studio Code**, open the folder with the starter code that you downloaded in Step 1.  Open up a **terminal** and type the following,

```
pip3 install guizero
```

You should now be able to use the **guizero** library.

### Using Thonny

Go to the **Tools** menu and choose **Manage Packages**.  Search for the **guizero** package and install it.

![](https://github.com/pguse/ics3u-python/blob/master/images/GuiZeroManagePackages.png)

## Step 3

We are going to make a glossary application that uses a Python dictionary. Here is what the application will look like.

![](https://github.com/pguse/ics3u/blob/master/images/myGlossaryWindow.png)

In this step we will just add to the starter code so that the basic elements of the application are present.  Modify the first line to look like this,

```python3
from guizero import App, Text, TextBox, PushButton
```
and add the following lines, where indicated,

```python3
# create a Text widget
text1 = Text(app, text="Enter the word you want defining:")

# create a TextBox widget
input_box = TextBox(app)

# create a PushButton widget
button = PushButton(app, text="SUBMIT")
```

This should add text, a text box, and a push button to the application.  Run your application ... *(use python3 if you are on a Mac)*

```
python myGlossary.py
```

A window should appear that looks like this:

![](https://github.com/pguse/ics3u/blob/master/images/myGlossaryPart1.png)

You can click on the SUBMIT button but nothing will happen.  Now add the following to the starter code, where indicated,
```python3
# create another Text widget
text2 = Text(app, text="Definition:")

# create a TextBox widget
output_box = TextBox(app)
```
Your window will now look like this.

![](https://github.com/pguse/ics3u/blob/master/images/myGlossaryPart2.png)

## Step 4

We will now add functionality to the PushButton.  By adding commands to widgets, the user can create changes in the GUI when they interact with the widget.  Add the following to the starter code where indicated,

```python3
# create a button press function
def click():
    entered_text = input_box.value
    output_box.clear()
    output_box.value = entered_text
```

Then, edit line 25 where the PushButton is created,

```python3
button = PushButton(app, text="SUBMIT", command=click)
```
Notice that in this line, we refer to the function defined above, but **do not include the parentheses**.

Run the program.  Type something in the upper TextBox and press the SUBMIT PushButton.  You should see the text appear in the lower TextBox.

## Step 5

Look at the ```click()``` function.  Note that the upper TextBox is called ```input_box``` and the lower text box is called ```output_box```.  Can you follow what the function is doing?

We are now going to modify the ```click()``` function so that it uses the dictionary given in the starter code.  Edit the code so that the function looks like this,

```python3
# create a button press function
def click():
    entered_text = input_box.value
    output_box.clear()
    output_box.value = myGlossary[entered_text]
```

Run the program and type in a word from the given dictionary.  If you spell it correctly, you should see a definition appear in the lower text box.

## Step 6

You have probably noticed that the formating of our application does not match the formatting of the example shown above.  We are going to correct that now.  Here is the final code.

```python3
from guizero import App, Text, TextBox, PushButton

myGlossary = {
    'algorithm': 'Step by step instructions to perform a task that a computer can understand.',
    'bug': 'A piece of code that is causing a program to fail to run properly or at all.',
    'binary number': 'A number represented in base 2.'
    }

bgcolor = (0,200,100)

# create a button press function
def click():
    entered_text = input_box.value
    output_box.clear()
    output_box.value = myGlossary[entered_text]


app = App(title="My Computer Science Glossary", layout="grid", bg = (225,225,225), height=350)

# create a Text widget
text1 = Text(app, text="Enter the word you want defining:\n", grid=[0,0], align="left")

# create a TextBox widget
input_box = TextBox(app, grid=[0,1], align="left", width=50)
input_box.bg = bgcolor

# create a PushButton widget
button = PushButton(app, text="SUBMIT", command=click, grid=[0,2], align="left")

# create another Text widget
text2 = Text(app, text="\nDefinition:", grid=[0,3], align="left")

# create a TextBox widget
output_box = TextBox(app, grid=[0,4], align="left", multiline=True, width=60, height=10)
output_box.bg = bgcolor

app.display()
```

To more fully understand how the formatting is done, check out the following sections of the guizero documentation:

* [Layouts](https://lawsie.github.io/guizero/layout/)
* [Grid and Alignment](https://lawsie.github.io/guizero/layout/#grid-layout)
* [Colours](https://lawsie.github.io/guizero/colors/)
* [App](https://lawsie.github.io/guizero/app/)
* [Text](https://lawsie.github.io/guizero/text/)
* [TextBox](https://lawsie.github.io/guizero/textbox/)
* [PushButton](https://lawsie.github.io/guizero/pushbutton/)

## Step 7

In this step we are going to learn a new concept in Python.  Up to this point, we have not attempted to handle errors in any of our programs.  Here we are going to handle errors using the **try:  except:** block.  Modify the click() function as follows,

```python3
# create a button press function
def click():
    entered_text = input_box.value
    output_box.clear()
    try:
        definition = myGlossary[entered_text]
    except:
        definition = "There is no entry for this word"
    output_box.value = definition
```
If an error occurs in the ```try:``` block, then the ```except:``` block executes.

## Step 8

Add 3 more definitions to the Python dictionary.  Run your code.  If everything seems to be working fine, submit your program.
