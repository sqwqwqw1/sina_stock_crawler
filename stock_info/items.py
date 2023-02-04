import scrapy

class StockInfoItem(scrapy.Item):
    symbol = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()

class MarketItem(scrapy.Item):
    date = scrapy.Field()
    symbol = scrapy.Field()
    settlement = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    amount = scrapy.Field()
    changepercent = scrapy.Field()
    mktcap = scrapy.Field()
    nmc = scrapy.Field()
    turnoverratio = scrapy.Field()
    pb = scrapy.Field()

class GnItem(scrapy.Item):
    gn_name = scrapy.Field()
    gn_symbol = scrapy.Field()

class StockGnItem(scrapy.Item):
    symbol = scrapy.Field()
    gn_symbol = scrapy.Field()
