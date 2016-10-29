CREATE TABLE `TICKER` (
      `SYMBOL` varchar(10) DEFAULT NULL,
      `NAME` varchar(2056) DEFAULT NULL,
      `MARKETCAP` float DEFAULT '0',
      `IPO` varchar(15) DEFAULT NULL,
      `SECTOR` varchar(1024) DEFAULT NULL,
      `INDUSTRY` varchar(1024) DEFAULT NULL,
      `EXCHANGE` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


