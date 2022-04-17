# LogicFinder Inc. 2018
import time
from datetime import datetime as dt

# Change host path according to your OS
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"  # localhost's IP

website_list = [  # Websites you want to block
    "www.facebook.com", "facebook.com",
    "www.twitter.com", "twitter.com",
    "dub119.mail.live.com", "www.dub119.mail.live.com"
]

if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
    print("Working hours...")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                        file.truncate()
                        print("Fun Hours...")
                        time.sleep(2.5)
