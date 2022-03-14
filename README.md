# Employees manager

## Pre-requistes
- git version 2.25.1 (ubuntu 20.04) or git version 2.34.1.windows.1 (windows 11)
- Docker version 20.10.11 (ubuntu 20.04) or Docker version 19.03.12 (windows 11)
- docker-compose version 1.29.2 (ubuntu 20.04 or windows 11)
- Python 3.9.6

## How to run

- Clone the repository;
- Enable the virtual environment;
- Install requirements.txt;
- Copy the env sample file to root as .env;
- Generate a secret key;
- Enter the secret key into the .env file;
- Start the containers with docker-compose.

```
git clone https://github.com/renatojsilvas/Employees.git
cd Employees
python -m venv .venv
.venv/scripts/activate.bat (Windows) or source .venv/bin/activate (Ubuntu 20.04)
pip install -r requirements.txt
copy env_sample\sample.env .env (Windows) or cp env_sample/sample.env .env (Ubuntu 20.04)
python env_sample/secret_key_gen.py (copy the value generated into .env file into <PUT YOUR SECRET HERE>)
docker-compose up
```

## How to test

- A admin user has already been created. Go to http://localhost:8080/admin/ and enter user => admin and password => admin123@;
- Inside postman, perform a get to http://localhost:8080/employee/. A list of employees must be returned;
- Inside postman, perform a post to http://localhost:8080/employee/ with body (a new employee must be added):
```
{
   "name": "Renato José da Silva",
   "email": "renatojsilvas@gmail.com",
   "department": "Developer"
}
```
- Inside postman, perform a get to http://localhost:8080/employee/4/. The employee that has id=4 must be returned;
- Inside postman, perform a delete to http://localhost:8080/employee/4/. The employee that has id=4 must be deleted;

## How to clean
```
docker-compose down --v
```

## How does it works?

There is a nginx server that receives the requests. This server works as reverse proxy that forward the requests to gunicorn server. Besides, the nginx serves the static files. Gunicorn is a webserver that translates http into something python can understand. The request hits the django instance that communicates with a postgres database. The  django  instance returns a response to the gunicorn which returns the reponse to the nginx which returns the response to the user.  


## Issues
- There is no authentication/authorization;
- docker-compose up should be invoked once. If you need to perfom the command again, clean the database with docker-compose down --v. The docker-compose up create a new superuser with the same name created before. It is needed to fix it;
