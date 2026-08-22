# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

def memoization(func):

    cache = {}

    def wrapper(num):

        if num in cache:
            print("Getting result from cache")
            return cache[num]

        result = func(num)

        cache[num] = result

        return result

    return wrapper


@memoization
def square(num):
    return num * num


print(square(5))
print(square(5))

print(square(10))
print(square(10))