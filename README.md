
# Development

### venv
virtualenv venv creates yoru pip env.  then `source venv/bin/activate`.  Then `pip install`.


### Build

For development:

`python aotpatcher.py`

For deployment:


`python -m eel aotpatcher.py web --onefile --noconsole --exclude win32com --exclude cryptography`
