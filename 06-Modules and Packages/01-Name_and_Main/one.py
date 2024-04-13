def func():
    print("FUNC() in one.py")


print("TOP-LEVEL print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
