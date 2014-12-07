#team_black_casework

##what is it?
Contains the web service to simulate a casework system.  
This service is completely faked, mocked etc.

##dependencies
Flask
 
Jinja

Install by running pip install -r requirements.txt

##config.py
create a config.py when you run the application.  It needs a key to know where the email and JPL service is.  e.g.

```
EMAIL_SERVICE = 'https://0.0.0.0:5011'
JPL_SERVICE = 'https://0.0.0.0:5012'
```
or

```
EMAIL_SERVICE = 'https://team-black-email-service-dancriddle.c9.io
```

##how to use it

to run the app:
```
python frontend.py
```

Hit the service locally at http://0.0.0.0:5010/  (if using cloud nine, run and preview with the IDE)

Curl the service to find the title number for a reference with:

```
curl -i -H "Content-Type: application/json" -X POST -d '{"reference":"1234"}' http://0.0.0.0:5010/titlefromreference
```
