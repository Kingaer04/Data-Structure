data = {
    "100-90": 25,
    "42-01": 48,
    "55-09": 18,
    "128-64": 71,
    "002-22": 18
}
sum = 0
for i in data.values():
    if i >= 18:
        sum += 20
    else:
        sum += 5
print(sum)
