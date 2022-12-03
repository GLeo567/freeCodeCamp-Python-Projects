import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        balls_list = []
        for color in kwargs:
            for _ in range(kwargs[color]):
                balls_list.append(color)
        self.contents = balls_list

    def draw(self, balls_drawn):
        balls_out = []
        if balls_drawn >= len(self.contents):
            for color in self.contents:
                balls_out.append(color)
            self.contents.clear()
            random.shuffle(balls_out)
        else:
            for _ in range(balls_drawn):
                # Obtaining random index
                ran_ind = random.randint(0, len(self.contents) - 1)
                # Selected ball in self.colors
                sel_ball = self.contents[ran_ind]
                # Extracting ball from self.colors
                balls_out.append(sel_ball)
                del self.contents[ran_ind]
        return balls_out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    coincidence = 0
    for _ in range(num_experiments):
        counting = 0
        extracted = {}
        hat_copy = copy.deepcopy(hat)
        extraction = hat_copy.draw(num_balls_drawn)
        for color in expected_balls:
            extracted[color] = extraction.count(color)
            if extracted[color] >= expected_balls[color]:
                counting += 1
        if counting == len(expected_balls):
            coincidence += 1
    return coincidence / num_experiments
