import re


name = input("Enter file:")

if len(name) < 1:
    name = "sample.txt"
try:
    handle = open(name)
except:
    print("File cannot be opened:", name)
    quit()

all_numbers = []

for line in handle:
    line = line.strip()
    numbers_in_line = re.findall('[0-9]+', line) 
    
    if numbers_in_line:
        all_numbers.extend(numbers_in_line)

numbers_as_integers = [int(num) for num in all_numbers]

total_sum = sum(numbers_as_integers)

print("Sum:", total_sum)