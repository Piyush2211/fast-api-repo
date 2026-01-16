import math # jabh bhi hum list meh kaam karte hai toh hame order yaad rakhna padhta hai operations perform karne seh pehle and hum order keh hisab seh operations perform karte hai  
api_types = ["Rest api","Webhooks","Websockets","Graphql","Grpc","Soap","MQTT","AQMP"]# so basically hum log list koh [] seh define karte hai and isme values , seh differentiate kar skate hai 
print(api_types)
print(api_types[-1])# list meh bhi slicing string keh tarah hi kaam karti hai and we can basically the access the element in the list in same method by passing index no - or normal in the []  
print(api_types[1::2])# yeh bhi ek slicing kah example hai jisme  hamne 2 kah jump use kiya hai just as string  
api_types[1]= "rest"#basically yaha par hum with index element koh access kar rahe hai 
print(api_types)
print(api_types[1:2])
api_types[1:2] = "Webhooks"# basically yaha par hum slicing use karke first index par ek naya variable add kar rahe hai par yeh kaam nahi karega kyuki python "Webhooks" koh as a array consider karlega and single single word ok a a new element add karlega
print(api_types)
api_types[1:2] = ["Webhooks"]#to overcome this issue ham array koh api_types list meh as a array pass karenge with one element so that list usko as a single string is consider kare
print(api_types)
print(api_types[1:1])
api_types[1:1] = ["test_api","test_api"]
print(api_types)
api_types[1:3]= []
print(api_types)
api_types[2:9]=[]
print(api_types)
for api in api_types:
    print(api, end=" ~~~ ")
if "Webhooks" in api_types:
    print("\nWebhook is a great api")
else:
    api_types.append("Webhooks")

print(api_types.pop())#so basically pop method will remove the last element from the api_types and will print it 
print(api_types)
api_types.remove("MQTT")
api_types.insert(2,"Mqtt")
print(api_types)
api_types_copy = api_types[:]#kyuki agar hum api_types_copy = api_types keh equal karenge toh api_types_copy and api_types dono ek hi memory block koh refer karne lag jayenge in order vo naah ho hum slicing seh ek copy create karenge jiseh ek naya memory block banjayega and api_types_copy usko point karega rather than api_types keh memory block koh
api_types_copy2 = api_types.copy()# yeh bhi same ek naya memory block banayega for api_types_copy keh liye
print(api_types_copy)
print(api_types_copy2)
nums = [x for x in range(10)] # yeh list compression expression hota hai idhar basically hum list koh define kar sakte hai on basis of a specific mathamatical expression , condditonal expressions keh hisab seh list koh create kar sakte hai and also hum iske andar apne predefined functions bhi use kar sakte hai to create a list 

squared_nums = [x**2 for x in range(10)]
y = range(10)
square_root_numbers_without_ceil = [math.sqrt(x) for x in range(100)]
square_root_numbers_with_ceil = [math.ceil(math.sqrt(x)) for x in range(100)]
difference_caused_due_to_ceil = [x-y for x , y in zip(square_root_numbers_with_ceil,square_root_numbers_without_ceil)]

print(str(nums)+"\n"+str(squared_nums))
print(difference_caused_due_to_ceil)
name_list = ["piyush","yuvraj","nandini"]
name_upper_case = [x.upper() for x in name_list]
print(name_upper_case)
