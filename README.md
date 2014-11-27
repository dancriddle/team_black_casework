#team_black_jpl_microservice

##what is it?
Contains the web services and database/stubs to store, validate and process joint proprietor letter requests.  
This service is completely faked, mocked etc.

##dependencies
Flask
 
Jinja

Install by running pip install -r requirements.txt

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