import os

check = input("You want to restart the system? (y or n)")

if check == "y" or check == "Y":
#    os.system("sudo reboot") # for linux
    os.system("shutdown /s /t 30") # for windows shutdown after 30 mins

else:
    print("Exiting the programme") 
