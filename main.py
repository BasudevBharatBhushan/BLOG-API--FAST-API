from fastapi import FastAPI  #Import

app = FastAPI()  #Instance

@app.get('/') #Define Route  (Decorator)
def index():  #Define Controller
    return {'data':{'name':'Sarthak'}}

@app.get('/about')
def about():
    return {'data':'about page'}


#Dynamic Routing

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1' , '2'}}