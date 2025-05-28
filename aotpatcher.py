import eel

import os


eel.init('web')



@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

#say_hello_py('Python World!')
#eel.say_hello_js('Python World!')   # Call a Javascript function



@eel.expose
def expand_user(folder):
    """Return the full path to display in the UI."""
    return '{}/*'.format(os.path.expanduser(folder))



eel.start('index.html', size=(800, 1000))  # Start


