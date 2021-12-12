input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"

]

my_file = open("input_002.txt", "r")
input = my_file.readlines()


xpos = 0
ypos = 0
aim = 0

for command in input:
    instruction, argument = command.split(" ")
    if instruction == "forward":
        xpos += int(argument)
        ypos += aim * int(argument)
    elif instruction == "down":
        aim += int(argument)
    elif instruction == "up":
        aim -= int(argument)

print(xpos * ypos)
