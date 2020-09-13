

try:
    a = 5
    b = 2
    c = a/b
    print(c)
except Exception:
    print("Hey, you can divide the number by 0")

print("BYE")



try:
    a = 5
    b = 0
    c = a/b
    print(c)
except Exception as e:
    print("Hey, you can divide the number by 0", e)

print("BYE")


try:
    print("Resource Open")
    a = 5
    b = 2
    c = a/b
    print(c)
except Exception as e:
    print("Hey, you can divide the number by 0", e)

finally:
    print("Resource Closed")
    print("BYE")



try:
    print("Resource Open")
    k = int(input("Enter a number:"))
    print(k)
    a = 5
    b = 0
    c = a/b
    print(c)

except ZeroDivisionError as e:
    print("Hey, you can divide the number by 0", e)

except Exception as e:
    print("Please something went wrong", e)

except ValueError as e:
    print("THis is an invalid literal", e)

finally:
    print("Resource Closed")
    print("BYE")