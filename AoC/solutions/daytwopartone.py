from classes.report import Report
from utils.filereader import FileReader

#set up file reader and get input
input = FileReader.readfile("daytwopartone.txt")

#sanitize input
cleaned_input = []
for line in input:
    cleaned_input.append(list(map(int, line.replace("\n", "").split())))

#set-up
amount_of_safe_reports = 0
report = Report()

#loop over input and check if reports are safe or unsafe
for element in cleaned_input:
    if report.is_safe(element, 1, 3):
        amount_of_safe_reports += 1

print(amount_of_safe_reports)