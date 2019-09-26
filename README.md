# action_livros
Application made to learn React and Django

## Stack

1 - [React](https://github.com/facebook/create-react-app);  
2 - [Django](https://www.djangoproject.com/);  
3 - [PostgreSQL](https://www.postgresql.org/);  

### Steps to execute

1 - First clone or download this repo on your computer;  
2 - Copy the docker-compose.yml from docker-compose.example:
```
    cp docker-compose.example docker-compose.yml 
```
3 - Inside the docker-compose.yml file you'll need to set values to these variables `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`, provide a valid email;  
4 - Run the pip environment:
```
    pipenv shell
```
5 - Run the dependencies:
```
    docker-compose up -d
```
6 - Go to `localhost:16543` and login on pgadmin with the email and password provided at the docker-compose.yml file, once you're in create a database named action_livros;  
7 - You're gonna need to migrate all the configuration:
```
    python3 manage.py migrate
```
8 - Create the super user:
```
    python3 manage.py createsuperuser
```
9 - Finally run the server:
```
    python3 manage.py runserver
```
