# contacts-backend-python-flask

**contacts-backend-python-flask** is part of "contacts" project that is an initiative where we try to explore frontend and backend implementations in order to better understand it cutting-edge features. This repository presents a python rest API sample.

## stack
* python 3.10
* flask
* sqlite
* pony

## features
* orm
* migrations
* small footprint

## get started (linux instructions only)

### option 1 - use latest docker image from dockerhub

execute the remote docker image
```
docker run -p 8010:8010 wastingnotime/contacts-backend-python-flask
```

### option 2 - just build and use as docker image
build a local docker image
```
docker build --tag contacts-backend-python-flask .
```

inspect local docker image (optional)
```bash
docker run -it --rm contacts-backend-python-flask /bin/ash
```

execute the local docker image
```
docker run -p 8010:8010 contacts-backend-python-flask
```
### option 3 - execute from source code 
- first, install python 3.10+, if you don't have it on your computer:  [how to install python 3](https://docs.python.org/3/using/unix.html#on-linux)
- go to root of solution and execute the commands below


set environment for development
```
cp .env_example .env
```

activate venv
```
source venv/bin/activate
```

install deps
```
pip install -r requirements.txt
```

and then run the application
```
python3 main.py
```

## testing
create a new contact
```
curl --request POST \
  --url http://localhost:8010/contacts \
  --header 'Content-Type: application/json' \
  --data '{
	"firstName": "Albert",
	"lastName": "Einstein",
	"phoneNumber": "2222-1111"
  }'
```

retrieve existing contacts
```
curl --request GET \
  --url http://localhost:8010/contacts
```
more examples and details about requests on (link) *to be defined



# observations
* no multi-stage docker building process due to the final image is small enough (about 54Mb). 

