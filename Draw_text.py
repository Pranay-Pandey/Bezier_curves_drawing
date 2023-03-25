import numpy as np
import matplotlib.pyplot as plt


class Letter:
    # Class to represent a letter, defined by a name and a list of 4 sets of (x,y) points.
    
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points


class Space:
    """
    Class to represent a space for drawing letters and words.
    """
    def __init__(self):
        self.plt = plt
        self.t = np.linspace(0, 1)
        self.ground_point = 0
        self.generating_4_mat = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
        self.gap = 1
        self.saved_letters = {}

    def set_ground_point(self, point):
        self.ground_point = point

    def get_ground_point(self):
        return self.ground_point

    def show(self):
        self.plt.show()

    def draw_diagram(self, pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8):
        object_ = np.array([[pt1, pt2], [pt3, pt4], [pt5, pt6], [pt7, pt8]])
        a, b, c, d, e, f, g, h = np.matmul(self.generating_4_mat, object_).flatten()
        x = a * (self.t ** 3) + c * (self.t ** 2) + e * self.t + g
        y = b * (self.t ** 3) + d * (self.t ** 2) + f * self.t + h
        self.plot(x + self.get_ground_point(), y)

    def plot(self, x, y):
        self.plt.plot(x, y)
        self.gap = max(self.gap, max(x) - self.get_ground_point() + 1)

    def letter_changed(self):
        self.set_ground_point(self.get_ground_point() + self.gap)

    def make_predefined_model(self, defined_letter: Letter):
        if defined_letter.get_name() not in self.saved_letters:
            self.saved_letters[defined_letter.get_name()] = defined_letter

    def draw_from_letter(self, letter: Letter):
        print("Drawing Text " + letter.get_name())
        for shape in letter.get_points():
            self.draw_diagram(*shape)
        self.letter_changed()
        self.make_predefined_model(letter)

    def draw_from_word(self, word):
        for letter in word:
            if letter in self.saved_letters:
                self.draw_from_letter(self.saved_letters[letter])

    def clear_slate(self):
        self.set_ground_point(0)
        self.gap = 1
        self.plt.clf()

if __name__ == "__main__":
    
    space = Space()
    p_letter = Letter('P', [[0, 0, 0, 2, 0, 3, 0, 5], [0, 5, 2, 5, 2, 3, 0, 3]])
    d_letter = Letter('D', [[0,0,0,2,0,3,0,5], [0,0,4,0,4,5,0,5]])
    r_letter = Letter('R', [[0,0,0,2,0,3,0,5], [0,3,4,3,4,5,0,5], [0,3,1,2,2,1,3,0]])
    x_letter = Letter('X', [[0,0,0.75,1.375,1.25,3.125,2,5], [2,0,1.25,1.375,0.75,3.125,0,5]])
    a_letter = Letter('A', [[0,0,0.75,1.375,1.25,3.125,2,5], [4,0,3.25,1.375,2.75,3.125,2,5], [1,2.5,1.5,2.5,2.5,2.5,3,2.5]])
    w_letter = Letter('W', [[0,0,0,2,0,3,0,5], [0,0,0,0,2,2.5,2,2.5], [2,2.5,2,2.5,4,0,4,0], [4,0,4,2,4,3,4,5]])

    space.make_predefined_model(w_letter)
    space.make_predefined_model(x_letter)
    space.make_predefined_model(r_letter)
    space.make_predefined_model(d_letter)
    space.make_predefined_model(p_letter)
    space.make_predefined_model(a_letter)
    
    space.draw_from_word("DRAW")
    
    space.show()
    space.clear_slate()
