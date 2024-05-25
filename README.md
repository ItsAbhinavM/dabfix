# DABFIX

Dabfix is a Flask-based application designed to help users fix links to disambiguation pages in Wikipedia

### Prerequistic
Before we begin, ensure that you have the following installed in your computer
- Python (version 3.5 or later)
- pip
- git
___
### Installation

1. clone this repository : `git clone https://github.com/sohomdatta1/dabfix.git` 
2. go to the directory : `cd dabfix`
3. Create a virtual environment : `python -m venv venv` or `python3 -m venv venv`
4. Activate the venv : 
- Windows : `venv\Scripts\activate`
- mac : `source venv/bin/activate`
- Linux  : `source venv/bin/activate` <br>
5. Set up environment variables:
  Create a .env file in the project root with the following content:

   - SECRETKEY=`your_secret_key` <br>
   - CONSUMER_KEY=`your_consumer_key` <br>
   - CONSUMER_SECRET=`your_consumer_secret` <br>
   - TOOL_REPLICA_USER=`your_tool_replica_user` (Toolforge only) <br>
   - TOOL_REPLICA_PASSWORD=`your_tool_replica_password` (Toolforge only) <br>
   - TOOLFORGE=`True`  # Set to True if running on Toolforge

6. Set up the database configuration:
  Create a replica.my.cnf file in the project root with the following content:
   [client]
   user=your_local_username
   password=your_local_password


### Install the required dependencies :
- `pip install -r requirements.txt`

### Running the application

Type the command : `flask run` <br>
The application will be available at port : `http://127.0.0.1:5000/`

## **Database Connection** :

To connect to the database, use the following SSH command to create an SSH tunnel:

`ssh -N -v gopavasanth@dev.toolforge.org -L localhost:3306:simplewiki.analytics.db.svc.eqiad.wmflabs:3306`

## **APIs** :
- Retrieve disambiguation data:
`http://localhost:5000/api/getdabs/simple/Reading`
- Retrieve raw data :
`http://localhost:5000/api/getraw/simple/Reading`

## contributing

Contributors are welcome , please follow the following steps :
1. Fork the repository
2. Clone the forked repository
3. Create a new branch : `git checkout -b branchName`
4. Make your changes
5. Commit your changes : `git commit -m "commit message"`
6. Push the code to the repository `git push`
7. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
