#Lavdrim Islami  Justin Pham

import random
import math

nums = []


for i in range(100):
    randNum = random.randint(1,100)
    nums.append(randNum)
    # print(len(nums))


def isEvenorOdd(nums):
    even = []
    odd = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        
        else:
            odd.append(nums[i])

    for i in range(len(even)):
        print("Evens: ", even[i])

    for j in range(len(odd)):
        print("odds: ", odd[j])
    

def sum(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    print(sum)

def isPrime(nums):
    if nums < 2:
        return False
    if nums == 2:
        return True
    for i in range(2, int(math.sqrt(nums)) + 1):
        if nums % i == 0:
            return False
    return True


def largestPrime(nums):
    for i in sorted(nums,reverse=True):
        if isPrime(i):
            return i
        

def isPerfectSquare(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            return False
        squareRt = math.sqrt(nums[i])
        if squareRt % 1 == 0:
            print(nums[i])



result = largestPrime(nums)

isEvenorOdd(nums)
sum(nums)
print("Largest prime: ", result)
isPerfectSquare(nums)






