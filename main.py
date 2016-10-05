import tingbot
from tingbot import *

# TingBot UI
#import TingUI
#from TingUI import *

# setup code here

@every(seconds=1.0/30)
def troploop():
    # drawing code here
    screen.fill(color='black')
    screen.text('Hello world!')

tingbot.run()
