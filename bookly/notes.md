- in python we basically create a virtual enviourment in order our projects requirements and configuration and does not effect the python which is installed globally in our system   
```
Command which we use to create virtual enviournment:-
 python -m venv name-of-env

• When we create a virtual enviourment basically a copy of python is installed into our directory where are creating  the virtual enviourment and this is used by our application to run itself 
Command which we use to activate virtual enviourment:-
name-of-env\Scripts\activate
```
- in order to install fast api in our virtual enviourment we use following command:-
```
command:-
pip install "fastapi[standard]"

• basically pip is python file manager which can used to manage different file and there access in python
```
- bascially ham main.py create karenge har fastapi application keh main.py hota hai basically har fastapi application keh andar yeh entry point hota hai yeh file in nutshell code execution yaha seh shuru hogi
- main.py seh hame access milta har vo cheez kah joh hame chahiye hoti hai apne fast api application create karne keh liye
- basically main.py kah main instance banane keh liye hame fast api import karni padegi apni main.py meh
- basically apni fast api app koh run karne kehe liye hum fastpi cli use karnge  
  • isme different commands hote hi hai joh hamari application koh run karne keh liye use hoti hai yeh commands following hai:
  ```
  1. run:- fastapi run 
  
  "yeh command hamari fastapi app koh production meh run karne keh liye use hongi "
  
  2. dev:- fastapi dev 

"yeh command hamari fast api koh devlopment mode meh run karne keh liye use hongi 
  "

  3. fastapi deploy

    "yeh command basically  hamari application koh deploy karne meh use hoti hai "

  4. fastapi login cloud
  
  "yeh command basically hamari application koh cloud keh andar changes  karne keh liye use hoti hai   
  ```  
  • fastapi --help use karnge fastapi cli keh baare meh ham aur cheeze jaan skate hai 
  