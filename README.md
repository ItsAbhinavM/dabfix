# 📦 Dabfix
Dabfix is a Flask-based application designed to help users fix links to disambiguation pages in Wikipedia.

## Introduction

This project is a Flask-based web application that allows users to manage and edit Wikipedia disambiguation pages. It provides both a web interface and a set of API endpoints to interact with Wikipedia. The application supports OAuth authentication and integrates with Wikimedia's databases.

## Features

- Edit Wikipedia pages
- Fetch disambiguation pages

## Installation

### Prerequisites

- Python 3.5 or above
- pip(usually included with python)
- Access to a Wikimedia Toolforge account
- mysql

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/hkx05/dabfix_wikimedia.git
    cd dabfix_wikimedia
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv # Also for mac
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root with the following content:
      ```env
      SECRETKEY=your_secret_key
      CONSUMER_KEY=your_consumer_key
      CONSUMER_SECRET=your_consumer_secret
      TOOL_REPLICA_USER=your_tool_replica_user (Toolforge)
      TOOL_REPLICA_PASSWORD=your_tool_replica_password (Toolforge)
      TOOLFORGE=True  
      ```

5. Set up the database configuration:
    - Create a `replica.my.cnf` file in the project root with the following content:
      ```ini
      [client]
      user=your_local_username(your mysql username)
      password=your_local_password(your mysql password)
      ```

6. Make the tunnel, connecting the database
    ```
    ssh -N -v sarthakparashar@dev.toolforge.org -L localhost:3306:enwiki.analytics.db.svc.eqiad.wmflabs:3306
    ```

7. Run the Flask application:
    ```sh
    flask run
    ```
### Database
- To view the mysql database, run the command
    ```
    mysql -h 127.0.0.1 -P 3306 -u s53922 -p
    ```
- Enter the obtained password


## Configuration

The application uses environment variables to manage configuration settings. Ensure you have a `.env` file in the root directory with the necessary variables. Additionally, the `replica.my.cnf` file is used for local database credentials.

### Environment Variables

- `SECRETKEY`: Secret key for Flask sessions.
- `CONSUMER_KEY`: OAuth consumer key for MediaWiki.
- `CONSUMER_SECRET`: OAuth consumer secret for MediaWiki.
- `TOOL_REPLICA_USER`: Database username for Toolforge (only needed on Toolforge).
- `TOOL_REPLICA_PASSWORD`: Database password for Toolforge (only needed on Toolforge).
- `TOOLFORGE`: Set to `True` if running on Toolforge.

## Usage

### Web Interface

1. Navigate to the home page at `http://localhost:5000`.
2. Log in using your MediaWiki credentials.
3. Use the interface to view, edit, and manage Wikipedia disambiguation pages.

### API Endpoints

The application provides several API endpoints for programmatic access:

- **Get Disambiguation Links**: 
  - `GET /api/getdabs/<proj>/<path:pagename>`
- **Get Raw Page Content**: 
  - `GET /api/getraw/<proj>/<path:pagename>`
- **Get Parsed Page Content**: 
  - `GET /api/getparsed/<proj>/<path:pagename>`
- **Edit Page Content**: 
  - `POST /api/edit/<proj>/<path:pagename>`

### Example Usage

Fetch disambiguation links for the "Reading" page:
```sh
curl http://localhost:5000/api/getdabs/simple/Reading
```
### Contributing

Contributors are welcome ! Please follow the following instructions

- Fork the repository
- Clone the forked repository
- Create a new branch : git checkout -b branchName
- Make your changes
- Commit your changes : git commit -m "commit message"
- Push the code to the repository git push
- Open a pull request

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
