from currency_converter import CurrencyConverter
AUD = 5
CNY = 233.08
CZK = 25
EUR = 73.81
GBP = 8.9
HKD = 510.1
HUF = 285
JPY = 166
KHR = 500
KRW = 46370
MYR = 1
NZD = 0.6
THB = 0.25
TWD = 1828
USD = 113.71
VND = 898700
# print((float(TWD) + CurrencyConverter().convert(AUD, 'AUD', 'TWD') + CurrencyConverter().convert(CNY, 'CNY', 'TWD') + CurrencyConverter().convert(CZK, 'CZK', 'TWD') + CurrencyConverter().convert(EUR, 'EUR', 'TWD') + CurrencyConverter().convert(GBP, 'GBP', 'TWD') + CurrencyConverter().convert(HUF, 'HUF', 'TWD') + CurrencyConverter().convert(HKD, 'HKD', 'TWD') + CurrencyConverter().convert(JPY, 'JPY', 'TWD') + CurrencyConverter().convert(KRW, 'KRW', 'TWD') + CurrencyConverter().convert(KHR, 'KHR', 'TWD') + CurrencyConverter().convert(MYR, 'MYR', 'TWD') + CurrencyConverter().convert(NZD, 'NZD', 'TWD') + CurrencyConverter().convert(THB, 'THB', 'TWD') + CurrencyConverter().convert(USD, 'USD', 'TWD') + CurrencyConverter().convert(VND, 'VND', 'TWD')))
# print(CurrencyConverter().convert(AUD, 'AUD', 'TWD'))
print(CurrencyConverter().currencies)
