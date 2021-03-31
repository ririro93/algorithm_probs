from sys import stdin
import math

stdin = open('input.txt', 'r')
input = stdin.readline

# function
def getPrimes(max_num):
    isPrime[2] = 1
    primes = [2]

    for i in range(3, max_num+1, 2):
        if isPrime[i] == -1:
            curr = 2
            primes.append(i)
            isPrime[i] = 1
            while i * curr < max_num+1:
                isPrime[i * curr] = 0
                curr += 1
    return primes


def getNumOfGold(N):
    i = 2
    cnt = 0

    while i ** 2 <= N:
        for prime in primes:
            if prime > N // 2:
                return cnt
            if isPrime[N-prime] == 1:
                cnt += 1
    return cnt

##################################################
# inputs
T = int(input())
Nums = [int(input()) for _ in range(T)]
max_num = max(Nums)

# init
isPrime = [-1] * (max_num+1)
primes = getPrimes(max_num)

# Test cases
for num in Nums:
    print(getNumOfGold(num))