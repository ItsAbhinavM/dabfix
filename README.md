# DABFIX

Dabfix is a Flask-based application designed to help users fix links to disambiguation pages in Wikipedia
___
### Prerequistic
Before we begin, ensure that you have the following installed in your computer
- Python (version 3.5 or later)
- pip
- git
___
### Installation

clone this repository : `git clone https://github.com/sohomdatta1/dabfix.git` <br>
go to the directory : `cd dabfix`

Create a virtual environment : `python -m venv venv` or `python3 -m venv venv` <br>
Activate the venv : <br>
Windows : <br>
- `venv\Scripts\activate`<br>
mac :<br>
- `source venv/bin/activate`<br>
Linux  :
- `source venv/bin/activate` <br>

clone this repository : `git clone https://github.com/sohomdatta1/dabfix.git`
go to the directory : `cd dabfix`

Create a virtual environment : `python -m venv venv` or `python3 -m venv venv`
Activate the venv : 
Windows :
- `venv\Scripts\activate`
mac :
- `source venv/bin/activate`
Linux  :
- `source venv/bin/activate`


Install the required dependencies :
- `pip install -r requirements.txt`

## Running the application

`flask run` <br>
The application will be available at port : `http://127.0.0.1:5000/`

## contributing

Contributors are welcome , please follow the following steps :
1. Fork the repository
2. Clone the forked repository
3. Create a new branch : `git checkout -b branchName`
4. Make your changes
5. Commit your changes : `git commit -m "commit message"
6. Push the code to the repository `git push`
7. Open a pull request


DB:

- `ssh -N -v gopavasanth@dev.toolforge.org -L localhost:3306:simplewiki.analytics.db.svc.eqiad.wmflabs:3306`

API's:

- http://localhost:5000/api/getdabs/simple/Reading
- http://localhost:5000/api/getraw/simple/Reading
