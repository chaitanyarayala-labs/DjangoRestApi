# DjangoRestApi

DjangoRestApi demonstrates on how to build a simple REST API using Django framework. Sqlite3 is used as an in-memory DB to perform CRUD operations.

## Installation
```bash
brew install python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pipenv shell
pip install -r requirements.txt
```
##### To run the application locally in http://127.0.0.1:8000 or http://localhost:8000
```bash
./manage.py runserver
```
##### To view all the available API calls
```bash
http://localhost:8000
or
http://localhost:8000/api/v1
```
##### To create an admin user
```bash
./manage.py createsuperuser
```
##### To login into the admin console
```bash
http://localhost:8000/admin
username: <super user name>
password: <super user password?
```
##### To add a new friend
- Open a browser
- Go to http://localhost:8000/admin
- Login into admin console
```bash
http://localhost:8000/friends
perform POST operation by filling name field
```
##### To get all the friends
```bash
curl -X GET http://localhost:8080/friends
```
##### To get a friend by id
```bash
curl -X GET http://localhost:8080/friends/:friendId

Example:
curl -X GET http://localhost:8080/friends/2
```
##### To add a new belonging
- Open a browser
- Go to http://localhost:8000/admin
- Login into admin console
```bash
http://localhost:8000/belongings
perform POST operation by filling name field
```
##### To get all the belongings
```bash
curl -X GET http://localhost:8080/belongings
```
##### To get a belonging by id
```bash
curl -X GET http://localhost:8080/belongings/:belongingId

Example:
curl -X GET http://localhost:8080/belogings/1
```
##### To add a new borrowing
- Open a browser
- Go to http://localhost:8000/admin
- Login into admin console
```bash
http://localhost:8000/borrowings
perform POST operation by creating a friend and belonging and fill What, To who, Returned fields
```
##### To get all the borrowings
```bash
curl -X GET http://localhost:8080/borrowings
```
##### To get a borrowing by id
```bash
curl -X GET http://localhost:8080/borrowings/:borrowingId

Example:
curl -X GET http://localhost:8080/borrowings/1
```
