str = 'X-DSPAM-Confidence: 0.8475 '
var1 = str.find(":")
print(var1)
var2 = str[19:]
print(var2)
var3 = float(var2)
print(type(var3))