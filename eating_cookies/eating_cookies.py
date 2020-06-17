'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    if cache == None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]

    


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 16

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
#  0  1  2  3  4  5   6   7   8   9    10   11   12   13    14    15    16
# [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609]
