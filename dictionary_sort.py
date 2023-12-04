new_name = input()
server = int(input())
name = [input()  for i in range(4)]
name.append(new_name)
new = sorted(name)
print(new)
count = 0
for i in new:
    if i != new_name:
        count += 20
    else:
        break
count = (count //server) + 20
print(count)
