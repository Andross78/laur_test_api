# test_api


To run this project please follow next steps:

Start it
install docker - on ubuntu https://docs.docker.com/engine/install/ubuntu/ 
               - on Mac https://docs.docker.com/docker-for-mac/install/
               - on Windows https://docs.docker.com/docker-for-windows/install/

On the command line, within this directory, do this to build the image and start the container:
  
 - docker-compose up
  
Open http://0.0.0.0:8000 in your browser.

To create superuser you should input this to comand line:

 - docker-compose run web su
  
 - python manage.py createsuperuser
  
Stop it all running:

 - docker-compose down
  
If you change something in docker-compose.yml then you'll need to build things again:

 - docker-compose build
  
You can generate postman_collection.json

 - python manage.py generateschema --format openapi > schema.yml

Add schema.yml content to new collection in postman and export it.

To use flake8 you need to install it:
 - docker-compose run web su
 - pip install flake8
 - flake8 .
  
