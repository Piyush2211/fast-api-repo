piyush_address = {
    "name":"piyush",
    "address":"# 3455 15-D Chandigarh",
    "phone-no": 9855114676
    
}
print(piyush_address)
print(piyush_address["name"])
print(piyush_address.get("address"))
piyush_address["name"]= "vasu"
print(piyush_address)
for data in piyush_address:
    print(data)
for data in piyush_address:
    print(data,piyush_address[data])
piyush_address_copy = piyush_address.copy()
print(piyush_address_copy)
address_of_people = {
    "piyush_address":{
        "name":"piyush",
        "address":"# 3455 15-D Chandigarh",
        "phone-no": 9855114676
    
    },
    "nandini_address":{
        "name":"Nandini",
        "address":"#F-7 375 lavanya model school amritsar ",
        "phone-no":8283823535
    },
    "ekaksh_address":{
        "name": "Ekaksh sharma",
        "address":"#3455 15-D Chandigarh",
        "phone-no":9914273460
    }
}
print(address_of_people)
print(address_of_people["ekaksh_address"])
print(address_of_people["piyush_address"]["phone-no"])
squared_no = {x:x**2 for x in range(6)}
print(squared_no)
