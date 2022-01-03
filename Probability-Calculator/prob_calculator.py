#import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += [k]*v
        self.default = self.contents.copy()

    def draw(self, number):
        rest = self.contents
        output = []
        while number != 0 and len(rest) != 0:
            pos = random.randint(0, len(rest)-1)
            output += [rest.pop(pos)]
            number -= 1
        return output

    def refill(self):
      self.contents = self.default.copy()

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    positive = 0
    drawn = []
    target = []
    for k,v in expected_balls.items():
        target += [k]*v
        
    for i in range(num_experiments):
        hat.refill()
        drawn = hat.draw(num_balls_drawn)
        try:
            for item in target:
                drawn.remove(item)
            positive += 1
        except:
            continue
    return positive / num_experiments