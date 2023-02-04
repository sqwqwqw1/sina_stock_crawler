from sqlalchemy import Column, String, Integer, Date, Float
from stock_info.database import Base


class StockInfo(Base):
    __tablename__ = 'stockinfo'
    symbol = Column(String, primary_key=True)
    code = Column(String)
    name = Column(String)
    def __repr__(self):
        return f'股票代码：{self.code}, 股票名称：{self.name}'

class Market(Base):
    __tablename__ = 'market'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    symbol = Column(String)
    settlement = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    amount = Column(Float)
    changepercent = Column(Float)
    mktcap = Column(Float)
    nmc = Column(Float)
    turnoverratio = Column(Float)
    pb = Column(Float)

    def __repr__(self):
        return f'股票代码：{self.symbol}, 日期：{self.date}'

class Gn(Base):
    __tablename__ = 'gn'
    
    gn_symbol = Column(String, primary_key=True)
    gn_name = Column(String)

    def __repr__(self):
        return f'概念代码：{self.gn_symbol}, 概念名称：{self.gn_name}'

class StockGn(Base):
    __tablename__ = 'stockgn'

    symbol = Column(String, primary_key=True)
    gn_symbol = Column(String)

    def __repr__(self):
        return f'概念代码：{self.gn_symbol}, 股票代码：{self.symbol}'