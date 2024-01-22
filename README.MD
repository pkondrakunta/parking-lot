# Parking Lot - Flask 

## Getting Started

1. Create a project folder
2. Create a virtual environment
```
py -m venv venv
```
3. Install Flask to your virtual environment
Navigate to your virtual environment: `\venv\Scripts\activate`
Install flask: `pip install flask`
4. Setup Environment variables
- Install the package to run environment variables using `pip install python-dotenv`
- Create your `.flaskenv` file with the following 
```
FLASK_ENV=development
FLASK_APP=app.py
```
5. Install the Flask-WTF extension for forms
```
pip install flask-wtf
```
6. Create a requirements.txt to track your dependencies
```
pip freeze > requirements.txt
```
To reinstall your dependencies you can do `pip install -r requirements.txt`