total = 0
number = 1
before = 0
after = 0

while number < 4000000:
        before = after
        after = number
        number = before + after
        if number%2 == 0:
            total = total + number
print(total)
