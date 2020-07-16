def list_to_string(elem):
    string = ""
    for vertex in elem:
        string = string + str(vertex) + " "
    return string


class Bat:
    def __init__(self, x, fitness, r, A, v, f):
        self.x = x
        self.fitness = fitness
        self.r = r
        self.A = A
        self.v = v
        self.f = f

    def __str__(self):
        return "X => " + list_to_string(self.x) + " FITNESS=> " + str(self.fitness) + " R=> " + str(self.r) + " A=> " + str(self.A) +\
               " v=> " + list_to_string(self.v) + " f=> " + str(self.f)