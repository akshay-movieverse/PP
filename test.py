import requests

data={'data':'rrr'}
r = requests.post("http://127.0.0.1:5000/api2/",json={'data':'rrr'})

print(r.json())