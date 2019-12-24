# test_task
## API endpoints:
1. ```GET: /api/subjects``` - returns list of all subjects in database
![GET Request](https://i.imgur.com/QujQ1Oi.png)
2. ```POST: /api/subjects``` (POST body: ```query: <your_query_here>```) - returns queried subject
![POST Request](https://i.imgur.com/gJPODbC.png)
## Getting Started
On this section you will understand how to get a copy of the project and 
deploy it on your local machine for development or testing purposes.
### Get the source code
First, you need to get this project on your local machine. 
Well, go to the directory you want to see this project in.
```
> cd ~/.../<target_directory>
```
Now you can get all the source code of this project using git clone command.
```
> git clone https://github.com/KamilRizatdinov/test_task.git
```
## Deployment using Docker
### Change environmental variables
Now you can see example.env with such content inside it:
```
SECRET_KEY=your_django_secret_key_here
```
Put your django secret key here. If you don't have one, you can get it [here](https://djecrety.ir).
### Copy to .env
Now you need to copy the content of example.env to .env file. Use this:
```
> cp example.env .env
```
### Compose up
Now you need build our application, to do this use the following command:
```
> docker-compose up --build -d
```
### Make migrations
Now you need to migrate your postgres database, use this:
```
> docker-compose run web /code/manage.py migrate
```
### Create superuser (optional)
If you want to use Django admin panel you need to create a superuser with the following command:
```
> docker-compose run web python /code/manage.py createsuperuser
```
