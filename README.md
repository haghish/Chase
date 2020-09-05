Chase Experiment Manual
=======================

This is a evolutionary psychology experiment designed in a 2D video game form. I used [pygame](https://www.pygame.org/) to develop the experiment because common tools for designing psychology experiment could not offer that much of flexibility for developing a videogame-like experiment. The experiment was developed for a scientific collaboration with [Prof. Robert Biegler](https://www.ntnu.edu/employees/robert.biegler)'s lab at the department of psychology at Norwegian University of Science and Technology. 

Among several moving circles, one circle chases the participant based on a variety. This vide of algorithms. The participant has to move its circle with the mouse to stay away from the chasing circle, if the it is detected. If the chasing circle arrives within a particular distance from the player's circle, the game (trial) is over. 

There is a configuration file that allows you to specify the number of trials, algorithms, and all of the decisions needed for configuring the trials. 

License
-------

MIT

Installation
------------

you need the following software packages:

- [Python 2.7 32bit](http://www.python.org)
- [PyGame 1.9.1](http://pygame.org)
- [requests](http://docs.python-requests.org)
- [numpy](http://www.numpy.org/)


If you are a complete newbie, installing the packages required for running this
experiment will keep you busy for a little while. I try to explain it "as basic as possible",
assuming you are a biggener user.

First of all, you __want to make sure that you install Python 32bit 2.7.12 or higher__. Notice that I said __32bit__, even if your machine is __64bit__ you still must install the __32bit__ Python 2.7.12 or higher. You must not install Python 3!

Next, you want to make sure that __python is defined in your environment__. This means that anytime you type __`python`__ in your command line, python should be executed. However, if python is not in the `Path`, the command line will not recognize it. This is particularly a problem for Microsoft Windows users (_as usual, whenever we talk about problems, Microsoft shines like a diamond_!).
There is two ways you can add python to the environment. The simplest way **is to pay attention** when you install Python 2.7. As shown in the image below, make sure `add python.exe to path` is selected. This option makes your life much easier but is not selected by default in the installation.

![](https://github.com/haghish/Chase/raw/master/Chase/resources/image/installer.png)

The second way is trickier. Microsoft users should open the __System Properties__ and go to __Advanced__ tab, and click on __Environment Variables__. A new windows will open, in the __system variables__ click on __`Path`__ and add the path to your Python directory which is something like:

    C:\Python27

[This tutorial might be helpful!](http://pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/). Then, also add the path to the `Scripts` Python directory which is something like:

    C:\Python27\Scripts


Next, you will need to install a few required packages. The easiest way to install packages is using __`pip`__, which itself, needs an installation. [See this tutorial about how to install `pip` script](https://pip.pypa.io/en/latest/installing/). Since you have previously added the `Scripts` directory to the path environment, now you can use the __`pip`__ command to install other packages. If you have installed Python 2.7.12, it already includes __pip__ but you should update it. To do so, run the __cmd__ and paste the following code in it:

    python -m pip install --upgrade pip

Now, you can install `requests` from the command line:

    pip install requests

You also will need __`pygame`__. Visit [http://www.pygame.org/download.shtml](http://www.pygame.org/download.shtml) and download the correct version of python for your OS.

In addition, you also need __`numpy`__ for doing some numeric manipulations on the trial numbers. The installation is just as before:

    pip install numpy




Settings.cfg
------------

The experiment's settings can be adjusted by updating the __`settings.cfg`__ file. The file can change the following settings:

**Configuration Argument** | **Description**
-------------------------- | -----------------------------
__`screen_width`__   | takes an integer which defines the width of the screen in pixels
__`screen_height`__  | takes an integer which defines the height of the screen in pixels
__`FullScreen`__  | can be `True` or `False`. If set to `True` it makes the game fullscreen. Otherwise, the screen will appear with the specified width and height.__If you set the game to full screen without increasing the width and height, the display will stretch__.
__`backgroundColor`__  | takes a vector of __3 integers, separated by comma__ which represent an RGB values for defining the background color of the game. The default values are `100,100,100` which is light gray.
__`fontColor`__  | takes a python color name which can be `black`, `white`, or any of the colors mentioned later in the documentation.
__`mouseCursor`__  | can be `True` or `False`. If set to `True` the mouse curser appears during the trial. Otherwise it will be hidden during the trial.
__`showTimer`__      | can be `True` or `False`. The experiment has a timer for tracking how long each trial lasts in terms of seconds. The timer can also be shown in the top-right corner of the screen if the value is set to `True`.
__`gameover_sound`__ | The value can be `True` or `False`. When the trial ends, a buzz sound is played if the value is `True`.
__`playerSpeed`__    |  takes an integer which defines the movement speed of the player based on number of pixels. The default is __5__ pixels
__`wolfSpeed`__   | takes a real number and defines the movement speed of the wolf and sheep.
__`trialType`__      | a vector of "0" and "1" showing the overall number of trials (counting 0 & 1) and whether a wolf exists or not (1 or 0 respectively). For example, if the experiment has 4 trials and only the first 2 trials have a wolf, the vector should be `1,1,0,0`. This option only specifies whether Wolf actually exists or not. It doesn't provide any information about the wolf's strategy.
__`duration`__       | a vector of number of seconds that each trial lasts. For example, 30,10, ... __the integers should be separated by comma__.
__`chaseRate`__       | a vector of chase probability per `turnRate`. __the integer should be between 0 to 100 and separated by comma__.  
__`chaseAngle`__      | a vector of chase angles for each trial. the integer can be between `1` ro `180`. __the integers should be separated by comma__. (`1` is practically straightline chase, given the size of the game objects and screen)
__`scapeAngle`__      | a vector of escape angles for each trial, only used when `randomPlayer` is `True`. the integer can be between `1` ro `180`. __the integers should be separated by comma__. (`1` is practically straightline chase, given the size of the game objects and screen)
__`killZone`__    | the radius of the death circle, i.e. the distance between the center of the coordinates of the __Wolf__ and the __player__ which ends the game, where the wolf is considered to win. The minimum `killZone` should be __32__ which is the diameter of the circles.
__`sheepNumber`__    | a vector of __comma separated integers__ that specifies the number of sheep __including the wolf__ who appear in the game.
__`Radius`__    | is an integer which defines the radius of the circle where the sheep and wolf should be located around it. The larger the radius, the more time the wolf will require to approach the player and also, the more time it takes other sheep to get close to the player. If set to anything below `killZone` there will be a chance of failure right at the start of the trial.
__`turnRate`__ | is an integer which defines the number of seconds that it takes for sheep and the wolf to make a random turn. The default is 1 turn per second.
__`randomPlayer`__ | can be `True` or `False`. If set to `True` the player will have a randomwalk similar to the other circles and the mouse will be disabled for moving the player during the trial. 


Instructions
------------

To run the experiment in Microsoft Windows click on __RUN.bat__ file.


Available colors
----------------

For the `fotColor` you can pick any of the colors mentioned in the figure
below. Write the name without any space in between, for example, `redorange` or
`midnightblue`.

![](https://github.com/haghish/Chase/raw/master/Chase/resources/image/available%20colors.jpg)
