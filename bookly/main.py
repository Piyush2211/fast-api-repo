from fastapi import FastAPI
from fastapi import Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel#So basically hum pydantic module seh BaseModel import karnge joh  use hota hai post request keh liye body create karne keh liye
app = FastAPI()# idhar hamne FastAPI class joh keh fastapi module kah part hai uska ek object create kiya hai app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get('/')#idhar hamne app kah use karke FastAPI class kah ek method call kiya joh hai get and usme hame / daala hai joh home directory koh define kar raha hai yaha par  
# @app.get basically as a decortator use kar rahe to add the functionality of app.get method in our read_root() method 
# basically get ek http method hai joh use hota hai to retrive data from the path joh hamne usme define kara hai jese idhar hamne / use kiya hai joh hamare root directory koh define  kar rha hai
async def read_root():
    #iseh method meh hamne ek dictionary return karvaye hai joh @app.get method keh use seh basically koi bhi jabh hamari directory keh / koh access yah hit karega to hum yeh dictonary return karenge basically in json 
    return {
        "meesage":"Hello World"
    }

@app.get('/greet/{name}')
async def read_greet(name:str)->dict:
    # basically ham type define kar sakte hai parameter keh and return type bhi define kar sakte hai jese name keh type str and  function keh return type dictionary hai
    return {
        "message":f"Hello {name} welcome to  the fast api server"
    }

@app.get('/address')#so basically agar hame kise param koh as a query paas karna hai toh hum usko path meh naah define karke @app.get genrator function keh directly as parameter useh path keh handling function meh push kardenge and jabh useh function kah path access karenge toh path?name_of_variable_passed_as_param = "value we want to pass in param as argument  " kardenge and function call hojayega   
async def read_greet_query(name:str="User",age:int=19)->dict:#so by passing the default values in the name and age we have created them optional parameter now if we do not pass them in  path?name="valueofname"&age="valueofage" it is gonna take User and 0 as default parameter 
    return{
        "message":f"Hello {name} is passed in the address and  {age} we are passing through query param"
    }


class BookCreateModel(BaseModel):#idhar basically hamne ek class define kari hai joh inherit kar rahi hai BaseModal koh in this class hum post request keh body genreate 1
    title:str
    author:str
@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    # idhar basically humne apne parameter kah type  hamari defined class keh bana rahe  hai taki argument meh body pass ho sake and than humne data koh return kardiya hai
    return{
        "title":book_data.title,
        "author":book_data.author
    }

@app.get('/get_headers',status_code=299)#so basically we can also pass the status code in the @app.get('/path',status_code=400) this will show over the actual status code  
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
                      ):# basically hum headers bhi access kar sakte hai fastapi meh by usinng Header class in fastapi  basically hum headers koh parameter seh access kar sakte hai joh keh Header keh equal none rakha hai hamne
    request_headers = {
    }
    request_headers["Accept"]= accept
    request_headers["Content-Type"]= content_type
    request_headers["User-Agent"]= user_agent
    request_headers["Host"]= host
    return request_headers

class OrderModal(BaseModel):
    
    orderItem:str
    orderquantity:int
    orderaddress:str

@app.post("/create_order")
async def get_order(order_data:OrderModal):
    #basically jabh bhi hum api call karnge post wali toh joh key add honge body meh vo class wali defined add honge nah keh return wali toh best practice yeh hai key class keh jiska variable bana hai BaseModal koh inherit karke vo same rakho 
    return{
        "order_item":order_data.orderItem or "Nothing is selected",
        "order_quantity":order_data.orderquantity or 0,
        "order_address":order_data.orderaddress or "# Domesday radio Russia"
    }

class  PackegingCost( BaseModel ):
    package_size:str
    package_weight:int
    package_cost:str

@app.post("/package_order")
async def package_order(package:PackegingCost):
    return{
        "package_size":package.package_size,
        "package_weight":package.package_weight,
        "package_cost":package.package_cost
    }

