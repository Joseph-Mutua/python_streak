# Instructions
# Prime numbers are numbers that can only be cleanly divided by itself and 1.

# https: // en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# https: // cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

# Here are the numbers up to 100, prime numbers are highlighted in yellow:

# https: // cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

# Example Input 1
# 73
# 73
# Example Output 1
# It's a prime number.
# It's a prime number.
# Example Input 2
# 75
# 75
# Example Output 2
# It's not a prime number.
# It's not a prime number.

num = int(input("Input any number\n"))


def prime_checker(num):
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime number")
            print(n)
            break
        else:
            print(f"{num} is a prime number")
            print(n)
            break


prime_checker(num)