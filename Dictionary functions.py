key = input()
contacts = {
    "David": ["123-321-88", "david@test.com"]
}
new = ""
if key not in contacts:
    print("Not found")
else:
    for i in contacts.get(key):
        new = i[0:]
    print(new)
