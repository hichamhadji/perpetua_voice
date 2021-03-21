# Perpetua Voice

Perpetua Voice
### Tech Stack

The project uses a number of open source projects to work properly:

* [Django] - Python framework to build fast, progressive and robust web applications
* [Django rest framework] - Django REST framework is a powerful and flexible toolkit for building Web APIs.


### Run on localhost

Create a virtualenv and install requirements

```sh
$ python -m venv venv
$ source venv/bin/activate
$ cd perpetua_voice
$ pip install -r requirements.txt
```
Export the envirment variables
```sh
$ ./ l_env.sh
```

```
Create a super user :
```sh
username: admin
password: admin123
```
Run migrations:
```sh
$ python manage.py migrate
```


Run the local server:
```sh
$ python manage.py runserver
```
Visit the link below for full API documentation:

```sh
http://localhost:8000/swagger/
```
### Run on docker

Run docker compose command:
```sh
$ docker-compose up -d
```

License
----
Perpetua  property

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Django rest framework]: <https://www.django-rest-framework.org/>
   [Django]: <https://www.djangoproject.com/>

