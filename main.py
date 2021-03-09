import requests

banner = """
  ____  _                   
 / ___|(_)_ __   __ _  ___  
 \___ \| | '_ \ / _` |/ _ \ 
  ___) | | | | | (_| | (_) |
 |____/|_|_| |_|\__, |\___/ 
                |___/                                      
_____________________________________________________________________
"""

print(banner)
vblink = input("Write Webhook Url:")

requests.delete(vblink)

print("Webhook Deleted.")


-- Credits ! Singo#9999