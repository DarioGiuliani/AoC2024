class Report:
    def is_safe(self, report, lower_bound, upper_bound):
        if self.numbers_are_in_range(report, lower_bound, upper_bound) and self.numbers_are_in_order(report):
            return True
        return False
    
    def is_safe_ignoring_one_level(self, report, lower_bound, upper_bound):
        for index, number in enumerate(report):
            list_without_element = report[:index] + report[index+1:]
            if self.is_safe(list_without_element, lower_bound, upper_bound):
                return True
        return False    

    def numbers_are_in_range(self, report, lower_bound, upper_bound):
        for index, number in enumerate(report):
            if index < len(report) - 1:
                difference = abs(number - report[index + 1])
                if difference < lower_bound or difference > upper_bound:
                    return False
        return True
    
    def numbers_are_in_order(self, report):
        return (all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1)))