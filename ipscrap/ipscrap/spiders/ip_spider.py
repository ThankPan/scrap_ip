import scrapy
import time

class ipaddr(scrapy.Item):
    ip=scrapy.Field()
    port=scrapy.Field()

urls=[]
for i in range(1,201):
    urls.append('https://www.kuaidaili.com/free/inha/'+str(i))

class IpSpider(scrapy.Spider):
    name="ip"
    start_urls=urls

    def parse(self,response):   
        ip=ipaddr()
        for line in response.css('tr'):
            if line.css('td').get() is not None:            
                ip['ip']=line.css('td[data-title="IP"]::text').get()
                ip['port']=line.css('td[data-title="PORT"]::text').get()
                f = open("ip.txt","a+")
                f.write(ip['ip']+':'+ip['port']+'\n')
        
