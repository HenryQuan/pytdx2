from tdxClient import TdxClient, print_df
from utils.log import log
from parser import stock
from const import CATEGORY, MARKET, KLINE_TYPE

client = TdxClient()
if client.connect().login():
    log.info("获取行情列表")
    print_df(client.call(stock.QuotesList(CATEGORY.SZ, 200)))
    log.info("获取k线")
    print_df(client.get_security_bars(MARKET.SZ, '000001', KLINE_TYPE.DAY_K, 0, 500))
    log.info("获取指数k线")
    print_df(client.get_security_bars(MARKET.SH, '999999', KLINE_TYPE.DAY_K, 0, 2000))
