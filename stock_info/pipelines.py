from itemadapter import ItemAdapter
from stock_info.items import StockInfoItem, MarketItem, GnItem, StockGnItem
from stock_info.database import SessionLocal
from stock_info import crud


class StockInfoPipeline:

    def __init__(self):
        self.db = SessionLocal()

    def process_stock_info_item(self, db, item):
        if crud.read_stock_info(db, item):
            return item
        else:
            crud.insert_stock_info(db, item)

    def process_market_item(self, db, item):
        if crud.read_market(db, item):
            return item
        else:
            crud.insert_market(db, item)

    def process_gn_item(self, db, item):
        if crud.read_gn(db, item):
            return item
        else:
            crud.insert_gn(db, item)

    def process_stock_gn_item(self, db, item):
        if crud.read_stock_gn(db, item):
            return item
        else:
            crud.insert_stock_gn(db, item)


    def process_item(self, item, spider):
        if isinstance(item, StockInfoItem):
            self.process_stock_info_item(self.db, item)
        if isinstance(item, MarketItem):
            self.process_market_item(self.db, item)
        if isinstance(item, GnItem):
            self.process_gn_item(self.db, item)
        if isinstance(item, StockGnItem):
            self.process_stock_gn_item(self.db, item)

