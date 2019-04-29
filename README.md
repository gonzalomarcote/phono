# phono
IoT bot for voice interaction

## Backend
Python backend based in Flask - https://www.flaskapi.org/

Interact with:  
```
$ curl -X GET http://0.0.0.0:5000/  or curl -X GET http://phono.marcote.org:5000/
[{"url": "http://0.0.0.0:5000/0/", "text": "do the shopping"}, {"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}, {"url": "http://0.0.0.0:5000/2/", "text": "paint the door"}]
$ curl -X GET http://0.0.0.0:5000/1/
{"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}
$ curl -X PUT http://0.0.0.0:5000/1/ -d text="flask api is teh awesomez"
{"url": "http://0.0.0.0:5000/1/", "text": "flask api is teh awesomez"}
```
