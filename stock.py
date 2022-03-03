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
        if int(totalbuyquantity) > int(totalsellquantity):
            #print how many percent
            percent=int(totalbuyquantity)/int(totalsellquantity)
            if float(lastprice) > float(averageprice):
                #print("symbol "+str(symbol)+" last Price "+str(lastprice)+" average Price "+str(averageprice)+" Buy Quantity "+str(totalbuyquantity)+" Sale Quantity "+str(totalsellquantity)+" Total increase % "+str(percent))
                if percent > 2 :
                    print("symbol "+str(symbol)+" last Price "+str(lastprice)+" average Price "+str(averageprice)+" Buy Quantity "+str(totalbuyquantity)+" Sale Quantity "+str(totalsellquantity)+" Total increase % "+str(percent))
                    mytest = str(symbol) + " Total increase % " + str(percent)
                    language='en'
                    myobj = gTTS(text=mytest,lang=language,slow=False)
                    myobj.save(str(symbol)+".mp3")
                    #os.system("mpg321 welcome.mp3")
                    playsound(str(symbol)+".mp3")
          
        if int(totalbuyquantity) < int(totalsellquantity):
            #print how many percent
            percent=int(totalsellquantity)/int(totalbuyquantity)
            if float(lastprice) < float(averageprice):
                #print("symbol "+str(symbol)+" last Price "+str(lastprice)+" Average Price "+str(averageprice)+" Buy Quantity "+str(totalbuyquantity)+" Sale Quantity "+str(totalsellquantity)+" Total Decrease % "+str(percent))
                if percent > 2 :
                    print("symbol "+str(symbol)+" last Price "+str(lastprice)+" Average Price "+str(averageprice)+" Buy Quantity "+str(totalbuyquantity)+" Sale Quantity "+str(totalsellquantity)+" Total Decrease % "+str(percent))
                    mytest = str(symbol)+" Total Decrease % " + str(percent)
                    language='en'
                    myobj = gTTS(text=mytest,lang=language,slow=False)
                    myobj.save(str(symbol)+".mp3")
                    #os.system("mpg321 welcome.mp3")
                    playsound(str(symbol)+".mp3")


    except Exception as e:
        #print("hello")
        print(e)
        pass
