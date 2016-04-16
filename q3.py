
number = 600851475143
prime = 2
#largest prime no. < root of number
while prime*prime < number:
    while number%prime == 0:
        number = number//prime
    prime = prime + 1
print(number)


