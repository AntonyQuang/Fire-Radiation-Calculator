# Fire Radiation Calculator

A TKinter app that calculates how close a train passenger can stand away from a train on fire without being harmed by the resulting heat.

# Repository Description:

![Fire Radiation Calculator](/images/calculator.png)

This is a Python-based GUI application that allows users to calculate how close railway passengers can be near a train on fire to aid railway station design.

Users can input fire and geometric data. Using a root-finding method known as the bisection method is, the maximum safe distance is calculated. This parameter, as well as several fire related parameters are saved as an excel spreadsheet file. The app provides a separate tab to educate users who are not familiar with the scientific methodology.

# Project Organization:

The project consists of the following directories and files:

```
├── methodology equations/
├── methodology text/
├── images/
├── calculator.py
├── input_manager.py
├── methodology_reader.py
└── run.py
```


instance/: Contains SQL lite database for the application.

migrations/: Contains the various migrations for the SQL lite database for the application.

config.py: Contains the configuration settings for the application.

requirements.txt: Lists the required packages and dependencies for the application.

run.py: The entry point for the application.

# First Time Set-up:

1. Clone the repository:

```$ git clone https://github.com/AntonyQuang/Allergy-Menu-Map.git```

2. Create a virtual environment and activate it:

```$ python3 -m venv env 
$ source env/bin/activate`
```
3. Install the required packages:

```$ pip install -r requirements.txt```

Ensure that the Flask-Googlemaps package in installed from [this github link](https://github.com/flask-extensions/Flask-GoogleMaps/releases/tag/0.4.1.1)

If you wish to do this separately you can do so with

```$pip install https://github.com/flask-extensions/Flask-GoogleMaps/archive/refs/tags/0.4.1.1.tar.gz```

4. Set up your individual .env file which contains:
 - Your Google API Key
 - Your Flask Secret Key
 - Your SQL Alchemy database uri
 - Your ipinfo token

5. Set up the database:

```
$ export FLASK_APP=run.py
$ flask db init
$ flask db migrate
$ flask db upgrade`
```
6. Run the application:

`  $ flask run`

# Persistent Environments:

This application uses a SQLite database by default. To switch to a different database, update the SQLALCHEMY_DATABASE_URI in config.py.

# Deployment:

The application can be deployed to a production environment using a web server such as Gunicorn or uWSGI.

# Code Style and Standards:

This project follows the PEP 8 (python.org/dev/peps/pep-0008/) coding style guidelines.

# License Information:

This project is licensed under the MIT License (opensource.org/licenses/MIT).

# Status and Roadmap

The application is currently in a functional state, but there is still room for improvement and new features to be added. The project roadmap includes transferring the database to a PostgreSQL database format, improving the website scalability, and integrating email functions.
