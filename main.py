from fastapi import FastAPI  #Import
from typing import Optional

app = FastAPI()  #Instance


#Query Parameter
@app.get('/blog') 
def index(limit = 10, published:bool = True, sort:Optional[str] = None):   #Default value also given, in case we do not pass the parameter
    if published: 
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    
# http://localhost:8000/blog?limit=50&published=true  (API Call syntax with Query Parameter)


@app.get('/about')
def about():
    return {'data':'about page'}


#Dynamic Routing

#Path parameter
@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1' , '2'}}