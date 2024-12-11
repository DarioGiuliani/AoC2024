class Report:
    def __init__(self, report):
        self.report = report

    def isSafe(self, lower_bound, upper_bound):
        if self.numbers_are_in_range(lower_bound,upper_bound) and self.numbers_are_in_order():
            return True
        return False
    
    def numbers_are_in_range(self, lower_bound, upper_bound):
        for index, number in enumerate(self.report):
            if index < len(self.report) - 1:
                difference = abs(number - self.report[index + 1])
                if difference < lower_bound or difference > upper_bound:
                    return False
        return True
    
    def numbers_are_in_order(self):
        return (all(self.report[i] <= self.report[i + 1] for i in range(len(self.report) - 1)) or all(self.report[i] >= self.report[i + 1] for i in range(len(self.report) - 1)))