
import requests
import random

def x(proxy):
  global ua
  try:
    requests.get("https://httpbin.org/ip", headers={"User-agent": random.choice(ua)}, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
    with open("alive.txt", "a") as fp:
      fp.write(proxy + "\n")
      fp.close()
    print(f"{proxy} ~ Working HTTP/s")
    
  except Exception as e:
    pass
    

with open("./wsp11/bro_1.txt", "r") as rr:
  proxies = rr.read().splitlines()
  
for proxy in sorted(proxies):
  x(proxy)
