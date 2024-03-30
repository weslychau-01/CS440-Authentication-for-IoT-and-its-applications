# CS440-Authentication-for-IoT-and-its-applications

## Steps to run this in your local machine 
### Step 1:
delete .venv folder if it exists <br />
`cd nightlight`   <br />
`python -m venv .venv`<br />
`.venv\Scripts\activate.bat`<br />
`pip install CounterFit-0.1.4.dev9-py3-none-any.whl`<br />
`pip install werkzeug==2.0.0 --force-reinstall`<br />
`pip install counterfit_connection-0.1.0.dev5-py3-none-any.whl`<br />
`pip install counterfit_shims_grove-0.1.4.dev5-py3-none-any.whl`<br />
`pip install pycryptodome`<br />
`counterfit `

### Step 2:
On the browser open a new page:  
http://localhost:5001/
create one sensor with type light with pin 1
create one actuator with type LED with pin 2

### Step 3:
go open another terminal<br />
`cd nightlight`<br />
`.venv\Scripts\activate.bat`<br />
`python app.py`

You may stop app.py and change the shared key to different value (use the commented code) and try it. 
