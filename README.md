# Phono
Personal IoT bot with arduino to get data from some sensors and API to interact with them.  

## Backend
Python backend based in Flask - https://www.flaskapi.org/  

### Dev deploy locally with docker-compose
Build and deploy locally with docker-compose:  
`$ docker-compose -p phono up -d`

Once built, start/stop it with:  
`$ docker-compose start phono`  
`$ docker-compose stop phono`

Remove with:  
`$ docker-compose rm phono`

### Prod deploy with helm in k8s
Deploy with helm:
`helm upgrade -i --debug phono-ingress charts/ingress/ --namespace phono -f charts/ingress/secrets/values.yaml`  
`helm upgrade -i --debug phono-api charts/api/ --namespace phono -f charts/api/secrets/values.yaml`  

### Deploy with CI/CD in GitHub Actions
See `.github/workflows/ci.yaml` self-commented file.  
https://vault.marcote.org:8200 must be *unsealed*.  

### Interact with phono api:
```
$ curl -X GET http://0.0.0.0:5000/  or curl -X GET https://phono.marcote.org
[{"url": "http://0.0.0.0:5000/0/", "text": "do the shopping"}, {"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}, {"url": "http://0.0.0.0:5000/2/", "text": "paint the door"}]
$ curl -X GET http://0.0.0.0:5000/1/
{"url": "http://0.0.0.0:5000/1/", "text": "build the codez"}
$ curl -X PUT http://0.0.0.0:5000/1/ -d text="flask api is teh awesomez"
{"url": "http://0.0.0.0:5000/1/", "text": "flask api is teh awesomez"}

