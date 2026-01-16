# Implement an exponential backoff stratergy that increase the time between retries starting from 1 second but stop after 5 retries 
import time 

max_retries = 5
no_of_atempts = 0
wait_time = 1

while no_of_atempts < max_retries :
    print("the atempt no is "+str(no_of_atempts +1)+" wait time : "+ str(wait_time))
    time.sleep(wait_time)
    no_of_atempts = no_of_atempts +1
    wait_time = wait_time *2

