items = ["apple", "cat", "apple", "orange", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplciate:",item)
        break
    unique_item.add(item)