# Safe removal using an iterator
list1 = [12, 13, 14]
iterator = iter(list1)
while True:
    try:
        element = next(iterator)
        list1.remove(element)  # Safe removal
        print(list1)
    except StopIteration:
        break

print()

# Avoid adding elements during iteration
#ou are modifying (list2.append(150)) a list while iterating over it with an iterator. This can lead to unexpected behavior, infinite loops, or runtime errors.
#Best practice:
#If you need to add or remove elements during iteration, collect changes in a separate list and apply them after the loop, as shown in your list3 example.
list2 = [120, 130, 140]
iterator = iter(list2)
while True:
    try:
        element = next(iterator)
        if element == 130:
            list2.append(150)  

        
    except StopIteration:
        break

print(list2)

print()



list3 = [1200, 1300, 1400]
new_elements = []
for element in list3:
    if element == 1300:
        new_elements.append(1500)  # Store new elements separately
list3.extend(new_elements)  # Add new elements after iteration
print("Updated list:", list3)