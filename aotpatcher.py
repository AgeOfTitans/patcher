import eel
import os
import src.eel_api  # so eel can find the src api


@eel.expose
def expand_user(folder):
    """Return the full path to display in the UI."""
    return '{}/*'.format(os.path.expanduser(folder))


if __name__ == '__main__':
    eel.init('web')
    eel.start('index.html', size=(800, 1000))  # Start
