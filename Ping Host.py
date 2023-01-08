import os
ipAddress = input("Enter URL/IP to ping: ")
# Pinging the system
os.system("ping {}".format(ipAddress))
