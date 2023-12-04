s1 = "how are you doing my friend"
s2 = "he is a friend of my brother"
count = 0
for i in s1.split(" "):
    for j in s2.split(" "):
        if i in j:
            count += 1
print(count)