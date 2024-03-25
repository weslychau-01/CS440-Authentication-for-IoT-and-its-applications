# CS440-Authentication-for-IoT-and-its-applications

## Steps to run this in your local machine 
delete .venv folder if it exists

cd nightlight          
python -m venv .venv
.venv\Scripts\activate.bat
pip install CounterFit-0.1.4.dev9-py3-none-any.whl
pip install werkzeug==2.0.0 --force-reinstall
pip install counterfit_connection-0.1.0.dev5-py3-none-any.whl
pip install counterfit_shims_grove-0.1.4.dev5-py3-none-any.whl
pip install pycryptodome
counterfit 

On the browser open a new page:  http://localhost:5001/
create one sensor with type light with pin 1
create one actuator with type LED with pin 2

go open another terminal
cd nightlight
.venv\Scripts\activate.bat
python app.py

stop the current process

go to app.py
change 1231 to 1232

python app.py
shows error (Invalid shared key :1232)