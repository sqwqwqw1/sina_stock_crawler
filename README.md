## 新浪财经市场行情爬虫

爬取行情中心（https://vip.stock.finance.sina.com.cn/mkt/#hs_a）的信息，因为是实时信息，建议每个交易日结束之后运行。

虽然我也不清楚这个有什么作用，但是对于没有Wind和其他API的我，我总觉得有一天会用到我每天爬下来的数据。

![images/1.png](./images/1.png)

先创建一个stock的mysql数据库，导入createtable.sql，然后在database.py里配置一下数据库：

```python
SQLALCHEMY_DATABASE_URL = 'mysql://user:password@127.0.0.1:3306/stock' 
```

运行start.py就可以开始爬了。

总共有五个表

### item

存储了各个字段的含义

![images/2.png](./images/2.png)

### stockinfo

存储了股票的名称，对应的股票代码ticker（code）和新浪代码（symbol）

![images/1.png](./images/3.png)

### gn

存储了概念板块的代码和名称

![images/1.png](./images/4.png)

### stockgn

存储了股票所对应的概念，虽然有些股票好像也没有对应的概念![images/1.png](./images/5.png)

### market

市场行情，注意这个date是你运行爬虫的日期

![images/1.png](./images/6.png)