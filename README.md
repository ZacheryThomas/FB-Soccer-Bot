# FB Messenger Soccer Bot

This is a Python based image recognition / mouse click bot that is designed to play the FB Messenger Soccer Game. Somehow my friend got a score of 300. There was no way I could get that myself. So here we are.

## How to run:
#### Install all the dependencies and openCV:

```pip install -r requirements.txt```

In addition to the normal requirements, you will have to install [OpenCV-Python](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html) as well.


#### Start up your favorite Android emulator:
I found it easiest for the emulator to be extremely small and tucked into the top left of the screen in order to get the resolution of the screenshot to be as low as possible. This lead to the fastest image detection times in my tests. In general the faster the image detection, the more accurate the click.

#### Run main.py using python 2.7:

```python main.py```

To exit, press the escape key.
