from utils.filereader import FileReader

#set up file reader and get input
input = FileReader.readfile("dayonepartone.txt")

#divide doubled list into two seperate ones
left_list = []
right_list = []
for line in input:
    #sanitize line
    sanitzed_input = line.replace("\t", "").replace("\n", "")
    split_input = sanitzed_input.split()
    left_list.append(int(split_input[0]))
    right_list.append(int(split_input[1]))

#compare list
#match smallest in left list with smallest in right and calculate absolute differce between
#make a sum of the difference
sum_of_differences = 0
elements_remaining = True
while elements_remaining:
    lowest_number_left = min(left_list)
    lowest_number_right = min(right_list)
    sum_of_differences += abs(lowest_number_left - lowest_number_right)

    left_list.pop(left_list.index(lowest_number_left))
    right_list.pop(right_list.index(lowest_number_right))

    if(len(left_list) == 0 and len(right_list) == 0):
        elements_remaining = False

print(sum_of_differences)