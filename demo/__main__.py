from pytdx2.tdxClient import TdxClient, print_df
from pytdx2.utils.log import log
from pytdx2.parser import stock
from pytdx2.const import CATEGORY, MARKET, KLINE_TYPE
from .tickers import tickers
from time import time

client = TdxClient()
tickers = list(set(tickers))

def build_quotes(tickers):
    quotes = []
    for ticker in tickers:
        market = MARKET.SZ if ticker.startswith('0') or ticker.startswith('3') or ticker.startswith('2') else MARKET.SH
        quotes.append((market, ticker))
    return quotes

if client.connect(ip="180.153.18.170").login(True):
    log.info("获取行情列表")
    print(client.ip, client.port)
    tickers = tickers[:500]
    # request in 3 parts
    results = []
    start_time = time()
    for i in range(0, len(tickers), 80):
        part = tickers[i:i+80]
        res = client.call(stock.Quotes(build_quotes(part)))
        results.extend(res)
        print(f"已完成 {i+len(part)}/{len(tickers)} 个股票代码的行情获取")
        print(f"耗时: {time() - start_time} 秒")
    end_time = time()
    print(f"获取行情列表耗时: {end_time - start_time} 秒")
    print(len(results))
    exit()
    print_df(client.call(stock.QuotesList(CATEGORY.SZ, 200)))
    log.info("获取k线")
    print_df(client.get_security_bars(MARKET.SZ, '000001', KLINE_TYPE.DAY_K, 0, 500))
    log.info("获取指数k线")
    print_df(client.get_security_bars(MARKET.SH, '999999', KLINE_TYPE.DAY_K, 0, 2000))
