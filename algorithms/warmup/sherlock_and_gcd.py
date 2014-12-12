#! /bin/python

from sets import Set

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        nums = [int(i) for i in raw_input().split(' ')]
        if non_gcd_subset_exists(nums):
            print "YES"
        else:
            print "NO"

def non_gcd_subset_exists(nums):
    for i in xrange(len(nums)):
        for j in xrange(i+1, len(nums)):
            if not common_factors_exist(nums[i], nums[j]):
                return True

    return False

def common_factors_exist(a, b):
    return len(factors_of(a) & factors_of(b)) > 0

def static_var(name, value):
    def decorate(func):
        setattr(func, name, value)
        return func
    return decorate

@static_var("cache",dict())
def factors_of(num):
    if num not in factors_of.cache:
        denominators = Set()

        for i in xrange(2, (num / 2) + 1):
            if num % i == 0:
                denominators.add(i)

        if num > 1:
            denominators.add(num)

        factors_of.cache[num] = denominators

    return factors_of.cache[num]

if __name__ == "__main__":
    main()
