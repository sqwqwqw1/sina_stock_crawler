DROP TABLE IF EXISTS `gn`;
DROP TABLE IF EXISTS `item`;
DROP TABLE IF EXISTS `market`;
DROP TABLE IF EXISTS `stockinfo`;
DROP TABLE IF EXISTS `stockgn`;

CREATE TABLE `item` (
  `symbol` varchar(20) NOT NULL,
  `title` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `market` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `symbol` varchar(10) DEFAULT NULL,
  `settlement` float DEFAULT NULL,
  `open` float DEFAULT NULL,
  `high` float DEFAULT NULL,
  `low` float DEFAULT NULL,
  `close` float DEFAULT NULL,
  `volume` float DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `changepercent` float DEFAULT NULL,
  `mktcap` float DEFAULT NULL,
  `nmc` float DEFAULT NULL,
  `turnoverratio` float DEFAULT NULL,
  `pb` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `stockinfo` (
  `symbol` varchar(10) NOT NULL,
  `code` varchar(10) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `gn` (
  `gn_name` varchar(20) DEFAULT NULL,
  `gn_symbol` varchar(20) NOT NULL,
  PRIMARY KEY (`gn_symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `stockgn` (
  `id` int NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) DEFAULT NULL,
  `gn_symbol` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO item(symbol,title) VALUES ('symbol', '新浪代码'), ('date', '日期'), ('code', '股票代码'), ('name', '股票名称'), ('settlement', '昨收'), ('open', '开盘价'), ('high', '最高价'), ('low', '最低价'), ('close', '收盘价'), ('volume', '成交量'), ('amount', '成交额'), ('changepercent', '涨幅'), ('mktcap', '市值'), ('nmc', '流通市值'), ('turnoverratio', '换手率'), ('pb', '市净率'), ('gn', '概念板块');