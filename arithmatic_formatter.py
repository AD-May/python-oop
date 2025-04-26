def separate_string(string):
    leading_space_index = string.find(" ")
    leading_substring = string[:leading_space_index]
    remaining_string = string[leading_space_index:]
    translation_table = str.maketrans({"+": "", "-": "", " ": ""})
    trailing_substring = remaining_string.translate(translation_table)
    
    return [leading_substring, trailing_substring]

def check_errors(problem):
    invalid_operators = ["/", "*"]

    for operator in invalid_operators:
        if operator in problem:
            return "Error: Operator must be '+' or '-'."

    strings = separate_string(problem)

    
    for substring in strings:
        if len(substring) > 4:
            return "Error: Numbers cannot be more than four digits."

        for char in substring:
            if char.isalpha():
                return "Error: Numbers must only contain digits."
    
    return None
    
def arithmetic_arranger(problems, show_answers=False):
    operator = ""
    top_line = ""
    bottom_line = ""
    dashes = ""
    output = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        error = check_errors(problem)
        if error:
            return error

        if problems.index(problem) == len(problems) - 1:
            separating_spaces = ""
        else:
            separating_spaces = "    "
        
        strings = separate_string(problem)

        if problem.find("+") > -1:
            operator = "+"
            result = int(strings[0]) + int(strings[1])
        else:
            operator = "-"
            result = int(strings[0]) - int(strings[1])

        output_length = len(str(result))
        

        if len(strings[1]) > len(strings[0]):
            num_spaces_top = (len(strings[1]) + 2) - len(strings[0])
            num_spaces_bottom = 1
            top_line += f"{' ' * num_spaces_top}{strings[0]}{separating_spaces}"
            bottom_line += f"{operator}{' ' * num_spaces_bottom}{strings[1]}{separating_spaces}"
            dashes += f"{'-' * (len(strings[1]) + 2)}{separating_spaces}"
            output_spaces = len(strings[1]) + 2 - output_length
        else:
            num_spaces_top = 2
            num_spaces_bottom = (len(strings[0]) + num_spaces_top) - (len(strings[1]) + 1)
            top_line += f"{' ' * num_spaces_top}{strings[0]}{separating_spaces}"
            bottom_line += f"{operator}{' ' * num_spaces_bottom}{strings[1]}{separating_spaces}"
            dashes += f"{'-' * (len(strings[0]) + 2)}{separating_spaces}"
            output_spaces = len(strings[0]) + 2 - output_length

        output += f"{' ' * output_spaces}{result}{separating_spaces}"

    if show_answers:
        return f"{top_line}\n{bottom_line}\n{dashes}\n{output}"
    else:
        return f"{top_line}\n{bottom_line}\n{dashes}"
    
    
    
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')