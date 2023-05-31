from back.parsing import explore
import eel

@eel.expose
def explore_py():
    return explore()