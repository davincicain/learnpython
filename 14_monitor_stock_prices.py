"""
tushare: financial data interface package
install: pip install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple
official website: https://tushare.pro/
"""

import tushare
import time

def sendEmail():
    print("Email has been sent.")

def main():
    buy_point = 540
    sale_point = 650
    n = 0
    while True:
        stock_data = tushare.get_realtime_quotes("300308")
        # print(stock_data)
        # print(type(stock_data))
        # print(stock_data.iloc[0])
        # print(stock_data.iloc[0]["price"])
        name = stock_data.iloc[0]["name"]
        price = float(stock_data.iloc[0]["price"])
        pre_close = float(stock_data.iloc[0]["pre_close"])
        increase_range = round((price-pre_close)/pre_close,4)
        print(f"name: {name}, price: {price}, pre_close: {pre_close}, increase_range: {increase_range*100}%")
        if price <= buy_point and n !=1:
            print("buy!")
            n = 1
            sendEmail()
        elif price > sale_point and n !=2:
            print("sale!")
            n = 2
            sendEmail()
        else:
            print("Don't make any transactions!")
        time.sleep(5)

if __name__ == "__main__":
    main()