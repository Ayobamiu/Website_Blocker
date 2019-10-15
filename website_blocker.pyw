#To block a website
#we need to access the host file in the PC
#Write a program to attach a certain IP address to the prospect websites by writing in the host file at some time:
#[The IP we are Redirecting to]   [website Address]

host_temp =r"C:\Users\Ayobamiu\PycharmProjects\Training\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

#if time is "hour A"
#open file
#write [The IP we are Redirecting to]   [website Address] in the file
from datetime import datetime
import time
websites = ("www.fb.com","www.facebook.com","fb.com","facebook.com")
IP_ = "127.0.0.1"
while True:
    m=datetime.now().hour
    print(f"It is {m}:00")
    if m>=8 and m<11:
        print ("it's working hour")
        with open(host_path, "r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(f"{IP_}   {website}   \n")
    else:
        print("It's fun time")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

    time.sleep(5)

else:
    print("It's fun time")
    time.sleep(5)
