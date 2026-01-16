api_types = ("graphql","restapi","grpc")
print(api_types)
print(api_types[0])
# api_types[0]= "websocket" yeh kaam nahi karega because tuple ek im mutable type hai so this will not work
if "graphql" in api_types:
    print("graphql is a type of api")

(graphql , restapi, grpc)=("graphql","restapi","grpc")#basically hum mutliple tuples koh distruct kar sakte hai eseh jese example meh show kara hai 

print(graphql)