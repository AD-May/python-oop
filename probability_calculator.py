import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        if len(kwargs) < 1:
            raise ValueError("You must create the Hat instance with at least 1 ball")
        self.contents = []
    
        # Create the contents list attribute for balls in the hat instance
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(f"{key}")
    
    def __repr__(self):
        return f"Hat(color_1 = 1, ..., color_n-1 = 5, color_n = 8)"


    def draw(self, amount_to_draw):
        withdrawn = []

        # If the amount_to_draw is more than the number of balls in the hat instance, return all of the balls currently in the hat instance
        if amount_to_draw >= len(self.contents):
            return_all = copy.copy(self.contents)
            self.contents = []
            return return_all

        # Draw random items from the hat and remove those items from the instance, returning the items removed
        for i in range(amount_to_draw):
            current_item = random.choice(self.contents)
            withdrawn.append(current_item)
            self.contents.remove(current_item)
        return withdrawn

    

def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
    num_correct_draws = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_bool_list = []
        this_draw = hat_copy.draw(num_balls_drawn)
        this_draw_dict = {}
        # Create a dictionary for current draw in format {"color": num_balls_of_color}
        for color in this_draw:
            if color in this_draw_dict:
                this_draw_dict[color] += 1
            else:
                this_draw_dict[color] = 1
        # Create a boolean list iterating over if the expected number of ball occurances are in the current draw
        for color, number_of_balls in expected_balls.items():
            if color in this_draw_dict and this_draw_dict[color] >= number_of_balls:
                draw_bool_list.append(True)
            else:
                draw_bool_list.append(False)
        if all(draw_bool_list):
            num_correct_draws += 1
    return round(num_correct_draws / num_experiments, 8)

# Test
hat = Hat(black=6, red=4, green=3)
print(hat.contents)
probability = experiment(hat=hat, expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)