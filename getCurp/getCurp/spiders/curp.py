
from scrapy.utils.response import open_in_browser
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.http import JsonRequest
from ..items import GetcurpItem
from .config import API_KEY
import scrapy

class curpCrawl(Spider):
    name = 'curp'
    allowed_domains = ['www.gob.mx']
    url_link = 'https://www.gob.mx/v1/renapoCURP/consulta'
    start_urls=['http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + url_link + '&render=true']

    def parse(self, response):
        
        data = {
            "nombres" : "FELIPE DE JESUS",
            "primerApellido" : "LAZARO",
            "segundoApellido" : "SANCHEZ",
            "diaNacimiento" : "19",
            "mesNacimiento" : "11",
            "selectedYear" : "1987",
            "sexo" : "H",
            "claveEntidad" : "DF",
            "tipoBusqueda" : "datos",
            "ip" : "127.0.0.1",
            "fechaNacimiento": "19/11/1987"
        } 

        yield JsonRequest(url = 'http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + self.url_link + '&render=true', method="POST", 
                            data = data, 
                            headers={'Content-Type':'application/json'}, 
                            callback= self.parse_quotes)

    def parse_quotes(self, response):
        open_in_browser(response)
        print (response)