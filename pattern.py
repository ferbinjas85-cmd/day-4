# Pattern 1
print("Pattern 1:")
for i in range(1, 5):
    print("*" * i)

# Pattern 2
print("\nPattern 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern 3
print("\nPattern 3:")
for i in range(1, 6):
    print("ABCDE"[:i])

# Pattern 4
print("\nPattern 4:")
for i in range(1, 6):
    print("5" * i)

# Pattern 5
print("\nPattern 5:")
for i in range(5, 0, -1):
    print("*" * i)