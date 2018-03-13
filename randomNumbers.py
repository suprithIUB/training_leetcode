import random

def randomNumbers(a, b):
    outcomes = b - a + 1
    while True:
        result = 0
        i = 0
        while (1 << i) < outcomes:
            i += 1
            result = result << 1
            result |= random.randint(0,1)
        
        print("res: %s"%result)
        if result < outcomes:
            return result + a

if __name__ == "__main__":
    print(randomNumbers(1,6))

