count = 0
for i in range(1, 201):
    if i % 2 != 0:
        count += 1
print(count)
#or
print(len([i for i in range(1, 201) if i % 2 != 0]))