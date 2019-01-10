import requests


try:
    
    request = requests.get("https://raw.githubusercontent.com/justinwidney/404Lab1/master/script.py")
    open('script.py', 'wb').write(request.content)
    

    print(request.text)
    
except ConnectionError:
    
    print("error")





