# nwea_blogpostapi

## Requirements
* Python 2.7
* pip
* git

## How to install:
1. pip install flask
2. pip install flask-restful
3. pip install sqlalchemy
4. git clone https://github.com/throwaway9482920/nwea_blogpostapi.git
5. python blogpostapi.py

## To read posts
Open a browser to [http://127.0.0.1:8080/posts](http://127.0.0.1:8080/posts)

## To post a new blog
`curl -i -H "Content-Type: application/json" -X POST -d '{"title":"My First Blog","body":"Hello NWEA!"}' http://127.0.0.1:8080/post` 
