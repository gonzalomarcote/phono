# Phono
Personal IoT bot with arduino to get data from some sensors and API to interact with.  

## Backend
Python backend based in Flask - https://www.flaskapi.org/  

Build and deploy locally with docker-compose:  
`$ docker-compose -p phono up -d`

Once built, start/stop it with:  
`$ docker-compose start phono`  
`$ docker-compose stop phono`

Remove with:  
`$ docker-compose rm phono`


Interact with phono api:  
```
$ curl -X GET http://0.0.0.0:5000/  or curl -X GET http://api.marcote.org
[{"url": "http://0.0.0.0:5000/0/", "text": "do the shopping"}, {"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}, {"url": "http://0.0.0.0:5000/2/", "text": "paint the door"}]
$ curl -X GET http://0.0.0.0:5000/1/
{"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}
$ curl -X PUT http://0.0.0.0:5000/1/ -d text="flask api is teh awesomez"
{"url": "http://0.0.0.0:5000/1/", "text": "flask api is teh awesomez"}
```
