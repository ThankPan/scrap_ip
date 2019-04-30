import requests

outputf=open("valid_ip_1.txt","a+")
proxies=[]
h={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
with open('ip.txt','r') as reader :
    for line in reader :
        proxy = line.split('\n', 1)[0]
        http_p = "http://" + proxy
        https_p="https://"+proxy        
        proxies.append({"http":http_p,"https":https_p})
for p in proxies:
    try:    
        response=requests.get('http://httpbin.org/ip',headers=h,proxies=p,timeout=1)
        if response.status_code==200:
            valided_ip=p['http'][7:]
            outputf.write(valided_ip)
            outputf.write('\n')
            print(response.text)
            print('测试通过')
    except Exception as e:
        print(e)
        continue