import eel

eel.init('web')



@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('index.html', size=(300, 200))  # Start


eel.start('index.html')
