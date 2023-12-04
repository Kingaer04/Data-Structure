words = input()
char = input()
count = 0
for i in words:
    if char == i:
        count += 1
print(int(count/len(words) * 100))
