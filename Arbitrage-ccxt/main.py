# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:44:02 2018



"""



import ccxt
import time
import _thread


def calc():

	bitfinex = ccxt.bitfinex()
	marketsBf = bitfinex.load_markets ()


	cex = ccxt.cex()
	kucoin = ccxt.kucoin()
	poloniex=ccxt.poloniex()
	bittrex=ccxt.bittrex()


	FEE = 1.02 # fee for every trade (2%)
	Diff = 0.6 # 1 % arbitrage to execute
	curr = ["ETH/BTC", "OMG/BTC", "LTC/BTC", "DASH/BTC", "ETC/BTC", "OMG/BTC"] #  "LTC/BTC", "DASH/BTC", "ETC/BTC", "OMG/BTC", "BCH/BTC"     currencies to trade if arbitrage is found
	exc = [bitfinex, kucoin, bittrex, cex] #  cex ,kucoin , bittrex   exchanges to trade on for the function calls


	def getAsk(market, sym):
		orderbook = market.fetch_order_book(sym)
		ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
		return ask

	def getBid(market, sym):
		orderbook = market.fetch_order_book(sym)
		bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
		return bid


	def compare():
		print ("Arbitrage Trader starting up...")
		yon_file = open("yon.txt", "r")
		yon = yon_file.read()
		yon_file.close
		n=0
		while n<=(len(curr)-1):
			print ("Starting Arbitrage checking for ", curr[n])
			pairpart1 = curr[n]
			m=0
			while m<=(len(exc)-1):
				#print "m = " + str(m)
				k = 0
				while k<=(len(exc)-1):
					#print "k = " + str(k)
					try:
						if (yon == "1"):
							sprice = getBid(exc[m], curr[n])
							bprice = getAsk(exc[k], curr[n])
						else:
							sprice = getBid(exc[k], curr[n])
							bprice = getAsk(exc[m], curr[n])

					except Exception:
							pass

					#print ("Sell price = " , str(sprice) , " on " , exc[m].id)
					#print ("Buy price  = " , str(bprice) , " on " , exc[k].id)

					if (float(bprice) < float(sprice)):
						#print ("Opportunity to buy " , curr[n] , " for ", str(bprice), " on ",exc[k]," and sell for " , str(sprice) , " on " , exc[m])
						yie = ((float(sprice) - float(bprice))/float(sprice))*100.0;
						#print ("Yield before trading costs would be: ",str(yie),"%")

					if (((float(sprice) - float(bprice))/float(sprice))*100.0 > Diff):
						# make_trade(exc[k], "buy", amount1, pairpart1, "btc", bprice)
						# make_trade(exc[m], "sell", amount1, pairpart1, "btc", sprice)
						#printouts for debugging
						print ("price on " , exc[m].id , " for " , curr[n] , " is " , str(sprice) , " BTC")
						print ("price on " , exc[k].id , " for " , curr[n] , " is " , str(bprice) , " BTC")
						print ("executing trade at a win per 1" , curr[n] , " of " , str(round(((sprice * 0.998)-(bprice * 1.002004)),8)) , "BTC")
						profit = str(round(100*(((sprice+bprice)+(sprice * 0.998)-bprice*1.002004)-(sprice+bprice))/(sprice+bprice),2))
						print ("profit %" , profit)
						with open("log.txt", "a") as text_file:
							print(f"{curr[n]}      {exc[m].id}      {sprice}    Sell", file=text_file)
							print(f"{curr[n]}      {exc[k].id}      {bprice}    Buy", file=text_file)
							print(f"-{exc[k].id}'den alındı {exc[m].id} 'de satıldı-----yön:{yon}------- Profit % {profit}\n", file=text_file)
							print (f" yön: {yon}")
							text_file.close
						yon_filer = open("yon.txt", "w")
						if yon == "1":
							yon_filer.write("0")
						else:
							yon_filer.write("1")
						yon_filer.close


					k+=1
				m+=1
			n+=1



	compare()





"""

def main():

	def run1(sleeptime, lock):
		while True:
			lock.acquire()
			calc() #The main Arbitrage function
			print ("Round completed sleeping for 30 seconds")
			lock.release()
			time.sleep(sleeptime)

	lock = _thread.allocate_lock()
	_thread.start_new_thread(run1, (30, lock))

	while True:
		pass

if __name__ == "__main__":
    main()

"""



delay = 20
while 1<2:
	try:
		calc()
		print ("sleep 20")
		time.sleep(delay)
	except:
		pass
		print("hıamina")
		time.sleep(20)





"""

# any time
bitfinex = ccxt.bitfinex ()
bitfinex.apiKey = 'YOUR_BFX_API_KEY'
bitfinex.secret = 'YOUR_BFX_SECRET'

# upon instantiation
hitbtc = ccxt.hitbtc ({
    'apiKey': 'YOUR_HITBTC_API_KEY',
    'secret': 'YOUR_HITBTC_SECRET_KEY',
})

"""