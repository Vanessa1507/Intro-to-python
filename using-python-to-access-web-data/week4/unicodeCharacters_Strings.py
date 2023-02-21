print("Representing Simple strings")
print(ord("H")) # 72
print(ord("e")) # 101
print(ord("\n")) # 10
print(ord("i")) # 10

print("\nTwo kinds of strings in Python")
x = b"abc"
print(type(x)) # <class 'bytes'>
y = "abc"
print(type(y)) # <class 'str'>
z = u"abc"
print(type(z)) # <class 'str'>