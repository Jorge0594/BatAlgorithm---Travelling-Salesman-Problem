from BatAlgorithm import BatAlgorithm
from Graph import create_full_graph
from Graph import plot_graph_solution
import matplotlib.pyplot as plt


g = create_full_graph(6)

algorithm = BatAlgorithm(5, 50, 1.0, 5.0, 0.995, 0.995, 0.98, 0.02, g)
algorithm.print_population()

solution = algorithm.execute()

plt.plot(algorithm.history)
plt.show()

plot_graph_solution(g, solution)

