import scrapy
import requests
from typing import Optional
from stock_info.items import StockInfoItem, GnItem, MarketItem, StockGnItem
from datetime import date as date_

def get_total_num(node):
    return int(requests.get(f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?node={node}').json())

def get_pages(node):
    return int(get_total_num(node)/80) + 1

def get_data(node, page):
    return {
                'page': str(page),
                'num': '80',
                'sort': 'symbol',
                'asc': '1',
                'node': node,
                'symbol': '',
                '_s_r_a': 'page'
            }

def get_gn(symbol):
    r = requests.get(f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getSymbolGN?symbol={symbol}')
    return [x['type'] for x in r.json()]

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['finance.sina.com.cn']
    url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'

    def start_requests(self):
        # 爬概念板块详情
        yield scrapy.Request('https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodes', callback=self.get_gn)

        # 爬股票详情
        node = 'hs_a'
        pages = get_pages(node)
        for page in range(1, pages+1):
            data = get_data(node, page)
            yield scrapy.FormRequest(self.url, formdata=data, callback=self.parse_stock_info)



    def parse_stock_info(self, response):
        date = date_.today().strftime('%Y-%m-%d')
        for ticker in response.json():
            stock_info_item = StockInfoItem(
                    symbol=ticker['symbol'],
                    code=ticker['code'],
                    name=ticker['name'],
                )
            market_item = MarketItem(
                    date=date,
                    symbol=ticker['symbol'],
                    settlement=ticker['settlement'],
                    open=ticker['open'],
                    high=ticker['high'],
                    low=ticker['low'],
                    close=ticker['trade'],
                    volume=ticker['volume'],
                    amount=ticker['amount'],
                    changepercent=ticker['changepercent'],
                    mktcap=ticker['mktcap'],
                    nmc=ticker['nmc'],
                    turnoverratio=ticker['turnoverratio'],
                    pb=ticker['pb']
                )
            yield stock_info_item
            yield market_item

            stock_gn_list =  gn_symbol=get_gn(ticker['symbol'])
            if len(stock_gn_list) == 0:
                stock_gn_item = StockGnItem(symbol=ticker['symbol'], gn_symbol=None)
                yield stock_gn_item
            else:
                for stock_gn in stock_gn_list:
                    stock_gn_item = StockGnItem(symbol=ticker['symbol'], gn_symbol=stock_gn)
                    yield stock_gn_item            

    def get_gn(self, response):
        gn_list = response.json()[1][0][1][6][1]
        for gn in gn_list:
            gn_item = GnItem(gn_name=gn[0], gn_symbol=gn[2])
            yield gn_item