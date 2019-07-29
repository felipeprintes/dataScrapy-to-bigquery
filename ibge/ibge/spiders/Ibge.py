# -*- coding: utf-8 -*-
import scrapy
from ibge.items import IbgeItem

class IbgeSpider(scrapy.Spider):
    name = 'ibge'
    #allowed_domains = ['agenciadenoticias.ibge.gov.br']
    start_urls = ['http://agenciadenoticias.ibge.gov.br/']
    def parse(self, response):
        titulo = response.xpath("//div[@class='home-noticias-content']//p[@class='home-noticia-subeditoria']//text()").extract()
        noticia = response.xpath("//div[@class='home-noticias-content']//p[@class='home-noticia-titulo']//text()").extract()

        dado = IbgeItem(titulo=titulo, noticia=noticia)
        
        #self.print_dado(dado)
        return dict(zip(dado['titulo'], dado['noticia']))

    '''
    def print_dado(self, dado):
        sub = 0
        for data in dado['data']:
            while sub<len(dado['titulo']):
                print(data+':'+dado['titulo'][sub])
                sub+=1
                break
    '''
from ibge.spiders import data_to_gcs