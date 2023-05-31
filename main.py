import eel
from middle.middle_parsing import *

if __name__ == '__main__':
    eel.init('front')
    eel.start('index.html', mode="chrome", size=(450, 370), suppress_error=True)

