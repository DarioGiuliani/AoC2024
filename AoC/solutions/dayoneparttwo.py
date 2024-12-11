from utils.filereader import FileReader

#set up file reader and get input
input = FileReader.readfile("dayoneparttwo.txt")

#divide doubled list into two seperate ones
left_list = []
right_list = []
for line in input:
    #sanitize line
    sanitzed_input = line.replace("\t", "").replace("\n", "")
    split_input = sanitzed_input.split()
    left_list.append(int(split_input[0]))
    right_list.append(int(split_input[1]))

sum_of_multiplications = 0
#loop over left list
for left_number in left_list:
    #check amount of occurences of left number in right list
    occurences_of_left_number = right_list.count(left_number)
    #multiply number by amount of occurences
    multiplication_result = left_number * occurences_of_left_number
    #make sum of multiplications
    sum_of_multiplications += multiplication_result

print(sum_of_multiplications)