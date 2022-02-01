# Currency Converter

You've just returned from an around-the-world trip and realize that you still have currencies from many different countries in your wallet.  Write a program that can read the contents of your wallet and convert those values into USD.  Your wallet is represented as `wallet.txt` and might look like this:
```txt
$3.40  ¥97

    €465.23     £587


  ₦305
```

All curency symbols inside your wallet refer to the currencies in this chart:

Symbol|Country|Currency|Code
------|-------|--------|----
ƒ|Aruba|Guilder|AWG
₼|Azerbaijan|Manat|AZN
៛|Cambodia|Riel|KHR
₡|Costa Rica|Colon|CRC
₱|Cuba|Peso|CUP
€|Euro Member Countries|Euro|EUR
¢|Ghana|Cedi|GHS
₪|Israel|Shekel|ILS
¥|Japan|Yen|JPY
₩|Korea (South)|Won|KRW
₭|Laos|Kip|LAK
₮|Mongolia|Tughrik|MNT
₦|Nigeria|Naira|NGN
₽|Russia|Ruble|RUB
฿|Thailand|Baht|THB
₴|Ukraine|Hryvnia|UAH
£|United Kingdom|Pound|GBP
$|United States|Dollar|USD
₫|Viet Nam|Dong|VND


Copy [currency_converter.py](currency_converter.py) into your code folder.  Run the file as is to create a `wallet.txt` filled with random currencies.  Everytime you run this code, the wallet will be randomized. Add your own code below the wallet randomizer to read `wallet.txt`, extract currencies, and convert their total to USD.  
You can solve the conversion problem any way you like, perhaps using an API.  There are apis out there that can be used to solve this problem without needing an api key.

### Note:
If you do sign up for an API and receive a key, be sure not to push it to GitHub, *especially* if it is a paid API.
