from pprint import pprint
from nsetools import Nse
from gtts import gTTS
from playsound import playsound
import os
#import numpy as np
nse = Nse();
all_stock_codes=nse.get_fno_lot_sizes()
for x in all_stock_codes:
    try:
        #print(x)
        symbol=nse.get_quote(x)['symbol']
        lastprice=nse.get_quote(x)['lastPrice']
        averageprice=nse.get_quote(x)['averagePrice']
        totalbuyquantity=nse.get_quote(x)['totalBuyQuantity']
        totalsellquantity=nse.get_quote(x)['totalSellQuantity']
        low=nse.get_quote(x)['pricebandlower']
        high=nse.get_quote(x)['pricebandupper']
        print(x)
        

    except Exception as e:
        #print("hello")
        print(e)
        pass
