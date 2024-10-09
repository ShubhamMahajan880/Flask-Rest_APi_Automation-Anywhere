#Lec - 1 - To creating a simple flask and handling a basic HTTP Request

"InTerminal"



Creating a Virtual environment for this project

pip install -r requirements.txt

Activate it
.\venv\Scripts\activate

To show all files
ls

If not activating then use 
Set-ExecutionPolicy RemoteSigned -Scope Process

Then try to activate again
.\venv\Scripts\activate

http://127.0.0.1:5000 - Base URL from HTTP Request
http://127.0.0.1:5000/ Then all other are end points which will be requested further

------------------------------------------------------------
"Code"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello Shubham, how are you"

@app.route("/home")
def welcometohome():
    return "2ndd time learning for welcoming at home page"


"terminal"
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\activate
Set-ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
flask run
http://127.0.0.1:5000
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Lec - 2 Removing Pycache File Automatically

"terminal"
use command -
$env:PYTHONDONTWRITEBYTECODE=1

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Lec - 3 Creating Multiple Files in Flask

Import of a file from previously stored file. OR use a code into multiple files
"""
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> python -m venv venv
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> Set-ExecutionPolicy RemoteSigned -Scope Process
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> .\venv\Scripts\activate
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> ls


    Directory: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         23-Sep-24  10:00 PM                venv
-a----         24-Sep-24  12:29 AM            293 app.py
-a----         24-Sep-24  12:44 AM           3598 Flask&Rest api Notes.py
-a----         24-Sep-24  12:30 AM            113 User_Controller.py


(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> $env:FLASK_ENV="development"  
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> $env:PYTHONDONTWRITEBYTECODE=1
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [24/Sep/2024 00:46:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:46:50] "GET /trying HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:47:09] "GET /trying/signup HTTP/1.1" 200 -
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api>
"""
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Lec - 4 Crating Packages in Flask Environment to  Segerate Files

Divide the same code in multiple folders.

"Code

app.py
#Creating First Flask application and handling HTTP Request

from flask import  Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello Shubham"

@app.route("/trying")
def Learn():
    return "2nd time using this command for learning"

# import Controller.User_Controller as User_Controller
# import Controller.Product_Controller as Product_Controller

# Instead of writing in this way we can use another way to write at a time

from Controller import Product_Controller, User_Controller
------------------------------------------------------------

User_Controller.py
from app import app
@app.route("/trying/signup")
def signup():
    return "3rd time learning signup operation"
------------------------------------------------------------
Product_Controller.py
from app import app
@app.route("/product/details")
def prodt():
return "4th Time I am Checking for Product Controller File into different Folder by adding in main.py"
------------------------------------------------------------

"terminal"
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> python -m venv venv
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> Set-ExecutionPolicy RemoteSigned -Scope Process
PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> .\venv\Scripts\activate
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> ls


    Directory: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         23-Sep-24  10:00 PM                venv
-a----         24-Sep-24  12:29 AM            293 app.py
-a----         24-Sep-24  12:44 AM           3598 Flask&Rest api Notes.py
-a----         24-Sep-24  12:30 AM            113 User_Controller.py


(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> $env:FLASK_ENV="development"  
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> $env:PYTHONDONTWRITEBYTECODE=1
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [24/Sep/2024 00:46:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:46:50] "GET /trying HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:47:09] "GET /trying/signup HTTP/1.1" 200 -
(venv) PS E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Flask&Rest api> flask run 
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [24/Sep/2024 00:58:03] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:58:07] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 00:58:29] "GET /trying/signup HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 01:01:38] "GET /trying/signup HTTP/1.1" 200 -
127.0.0.1 - - [24/Sep/2024 01:01:50] "GET /product/details HTTP/1.1" 404 -
127.0.0.1 - - [24/Sep/2024 01:02:20] "GET /product/details HTTP/1.1" 404 -
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Lec - 5 iMPORT aLL mODULES fROM pYTHIN pACKAGE AT oNCE

import Controller.User_Controller as User_Controller
import Controller.Product_Controller as Product_Controller

->Instead of writing in this way we can use another way to write at a time

from Controller import Product_Controller, User_Controller

->Instead of writing in this way we can use another way to write at a time

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Lec - 6 Creating the Controller Model Architecture using Flask

browser Se request controller ko jaa rahi h and Controller se redirect ho kar Model ko jaa rhi h and Model ka statement Return ho raha h


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Some Points -

1) A Decorator is always beginwith @
2_ For indicating a Folder as it is a Python Package. use __init__.py

  

