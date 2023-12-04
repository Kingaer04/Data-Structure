prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
new = 0
for i in prices:
    new += i
print(len(prices))
print(sum(prices)/len(prices))
print(int(new/len(prices)))
