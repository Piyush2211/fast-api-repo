file_handler = open('loop_behind_the_scene.md')

# file_line_1 = file_handler.read()

file_line_by_next = file_handler.__next__()# agar hum readline() method use karta hai file kah data store yah read karne keh liye toh jabh line break aata hai toh readline() '' quotes deta hai but jabh hum .__next__() use karte hai manage karne keh liye toh  agar line break aata hai toh yeh hame StopIteration  exception throw kardeta hai 

# print("the data in the file is : \n"+file_line_1+"\n :the data in the file has eneded \n the datatype of the file is : "+str(type(file_line_1)))

print("THIS IS THE DATA USING NEXT TO HANDLE FILE :\n"+file_line_by_next)
for line in open("sets_prc.py"):
    print(line)

print ("the below is the code using the while loop\n")
while True:
    line = file_handler.readline()
    if not line:
        break
    print(line,end="")