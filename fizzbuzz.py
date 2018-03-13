def fizz_buzz(start, end):
    for i in range(start, end):
        if (i % 3 == 0) and (i % 5 == 0):
            print("{0} fizzbuzz".format(i))
        elif i % 3 == 0:
            print("{0} fizz".format(i))
        elif i % 5 == 0:
            print("{0} buzz".format(i))
        else:
            print("--")

if __name__ == "__main__":
    fizz_buzz(1, 50)
