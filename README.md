
# Age of Titans Patcher

Age of Titans is a roguelike Everquest adaptation using [EQEMU](https://www.eqemulator.org/).

This patcher is built with vanilla html/css/js and  [Python Eel](https://github.com/python-eel/Eel).


# Development

### venv
virtualenv venv creates yoru pip env.  then `source venv/bin/activate`.  Then `pip install`.


### Build

For development:

`python aotpatcher.py`

For deployment:


`python -m eel aotpatcher.py web --onefile --noconsole --exclude win32com --exclude cryptography`
