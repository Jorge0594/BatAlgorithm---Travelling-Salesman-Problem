import random as rnd
from igraph import *
from Bat import Bat


class BatAlgorithm:
    def __init__(self, population_size, max_generation, f_min, f_max, A_0, r_0, alpha, gamma, graph):
        self.population_size = population_size
        self.max_generation = max_generation
        self.f_min = f_min
        self.f_max = f_max
        self.A_0 = A_0
        self.r_0 = r_0
        self.alpha = alpha
        self.gamma = gamma
        self.graph = graph
        self.population = self.initialize_population()
        self.best = self.population[0]
        self.history = []

    def initialize_population(self):
        population = []
        for i in range(self.population_size):
            x_aux = self.initialize_x_bats()
            bat = Bat(x_aux.copy(), self.calculate_fitness(x_aux), 0, 1, [], self.update_frequency())
            population.append(bat)
        return population

    def initialize_x_bats(self):
        list_vertex_index = []
        x_bat = []
        for i in range(len(self.graph.vs)):
            list_vertex_index.append(i)
        rnd.shuffle(list_vertex_index)

        while list_vertex_index:
            x_bat.append(list_vertex_index.pop())
        return x_bat

    def update_frequency(self):
        return round(self.f_min + (self.f_max - self.f_min) * round(rnd.uniform(0, 1), 3))

    def calculate_fitness(self, x):
        sum_distances = 0
        for i in range(len(x) - 1):
            sum_distances += self.graph[x[i], x[i + 1]]
        sum_distances += self.graph[x[i + 1], x[0]]
        return sum_distances

    def get_best(self):
        for pop in self.population:
            if pop.fitness < self.best.fitness:
                self.best = pop

    def increase_r(self, r, it):
        if it == 0:
            it = 1
        return self.r_0 * (1 - math.exp(-(self.gamma * it)))

    def decrease_A(self, A):
        return self.alpha * A

    def generate_new_solutions(self, bat):
        x_best_copy = self.best.x.copy()
        for i in range(bat.f):
            x_best_copy.remove(bat.x[i])
        bat.x = bat.x[0:bat.f] + x_best_copy

    def random_walk(self, bat):
        index_1 = rnd.randint(0, len(bat.x) - 1)
        index_2 = rnd.randint(0, len(bat.x) - 1)
        while index_1 == index_2:
            index_2 = rnd.randint(0, len(bat.x) - 1)
        aux = bat.x[index_1]
        bat.x[index_1] = bat.x[index_2]
        bat.x[index_2] = aux

    def execute(self):
        for i in range(self.max_generation):
            for j in range(len(self.population)):
                aux_bat = deepcopy(self.population[j])
                self.generate_new_solutions(aux_bat)
                if rnd.uniform(0, 1) > self.population[j].r:
                    self.random_walk(aux_bat)
                aux_bat.fitness = self.calculate_fitness(aux_bat.x)
                if rnd.uniform(0, 1) < self.population[j].A and aux_bat.fitness < self.population[j].fitness:
                    self.population[j] = deepcopy(aux_bat)
                    self.population[j].r = self.increase_r(self.population[j].r, i)
                    self.population[j].A = self.decrease_A(self.population[j].A)
            self.get_best()
            self.history.append(self.best.fitness)
        print("BEST BAT: {}".format(self.best))
        return self.best.x

    def print_population(self):
        for pop in self.population:
            print(pop)
        print()