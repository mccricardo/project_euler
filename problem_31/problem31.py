"""
Coin change problem: http://www.algorithmist.com/index.php/Coin_Change

Good explanation for the implemented solution: 	
	http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
"""

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0 for x in range(target)]
 
for coin in coins:
  for i in range(coin, target+1):  	
  	ways[i] += ways[i-coin] 
 
print ways[target]
