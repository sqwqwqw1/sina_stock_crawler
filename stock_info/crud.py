from stock_info import models
from sqlalchemy.orm import Session
from stock_info.items import StockInfoItem, MarketItem, GnItem, StockGnItem


def read_stock_info(db:Session, item:StockInfoItem):
    return db.query(models.StockInfo).filter(models.StockInfo.symbol==item['symbol']).first()

def insert_stock_info(db:Session, item:StockInfoItem):
    db.add(models.StockInfo(**item))
    db.commit()
    return item

def read_market(db:Session, item:MarketItem):
    return db.query(models.Market).filter(models.Market.symbol==item['symbol'], models.Market.date==item['date']).first()

def insert_market(db:Session, item:MarketItem):
    db.add(models.Market(**item))
    db.commit()
    return item

def read_gn(db:Session, item:GnItem):
    return db.query(models.Gn).filter(models.Gn.gn_symbol==item['gn_symbol']).first()

def insert_gn(db:Session, item:GnItem):
    db.add(models.Gn(**item))
    db.commit()
    return item

def read_stock_gn(db:Session, item:StockGnItem):
    return db.query(models.StockGn).filter(models.StockGn.gn_symbol==item['gn_symbol']).filter(models.StockGn.symbol==item['symbol']).first()

def insert_stock_gn(db:Session, item:StockGnItem):
    db.add(models.StockGn(**item))
    db.commit()
    return item

