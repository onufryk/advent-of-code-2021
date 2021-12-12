import copy

input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

my_file = open("input_003.txt", "r")
input = [l.strip() for l in my_file.readlines()]

input_1 = copy.copy(input)
bit_index = 0
print(input_1)

while len(input_1) > 1:
    num_1 = sum([i[bit_index] == "1" for i in input_1])
    num_0 = len(input_1) - num_1
    most_common = "1" if num_1 >= num_0 else "0"
    input_1 = [i for i in input_1 if i[bit_index] == most_common]
    bit_index += 1
    print(input_1)

oxygen_generator_rating = int(input_1[0], 2)
print(oxygen_generator_rating)

input_2 = copy.copy(input)
bit_index = 0
print(input_2)

while len(input_2) > 1:
    num_1 = sum([i[bit_index] == "1" for i in input_2])
    num_0 = len(input_2) - num_1
    least_common = "0" if num_1 >= num_0 else "1"
    input_2 = [i for i in input_2 if i[bit_index] == least_common]
    bit_index += 1
    print(input_2)

co2_scrubber_rating = int(input_2[0], 2)
print(co2_scrubber_rating)

print(co2_scrubber_rating * oxygen_generator_rating)
