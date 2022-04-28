# BatAlgorithm---Travelling-Salesman-Problem

A simple implementation of BatAlgorithm to solve "The Travelling Salesman Problem"[1] based on the implementations that you can find in [2] and [3].

## Files

#### Bat.py

Python class that contains all the necessary bats attributes.

#### BathAlgorithm.py

Contains the BatAlgorithm implementation and the auxiliary methods that BatAlgorithm uses.

#### Graph.py

Contains all the methods to create and plot the graphs. Uses the library Igraph[4]

#### Main.py

Contains a simple test of this algorithm.

## Usage

1. Use the method **create_full_graph(n_vertex)** to create a full conected graph with **n** vertex.
```python
from Graph import create_full_graph

g = create_full_graph(5) #Create a full conected graph with 5 vertex
```
2. Create a instance of BatAlgorithm class with the following parameters:
    * **population_size**: Number of bats that the population will contain.
    * **max_generation**: Number of iterations(generations) of the algorithm.
    * **f_min**: Minimum value of the frequency.
    * **f_max**: Maximun value of the frequency.
    * **A_0**: Initial value of the loundness.
    * **r_0**: Initial value of the pulse rate.
    * **alpha**: Value of alpha that is used to decrease the loudness.
    * **gamma**: Value of gamma that is used to increase the pulse rate.
    * **g**: The graph.
    
```python
from BatAlgorithm import BatAlgorithm

algorithm = BatAlgorithm(5, 50, 1.0, 5.0, 0.995, 0.995, 0.98, 0.02, g)
```
3. Call the method **execute** of the BatAlgorithm.py to start the execution. Returns a list of vertex that represents the best path with the minimun cost.
```python

solution = algorithm.execute()
```
4. (Optional) Plotting the solution with the function **plot_graph_solution** that you can find in **Graph.py**
```python
from Graph import plot_graph_solution

plot_graph_solution(g, solution)
```
5. (Optional) Plotting the evolution of the fitness in the algorithm. You can find this data in the attribute **history** in the BathAlgorithm class.
```python
import matplotlib.pyplot as plt

plt.plot(algorithm.history)
plt.show()
```
## Basic example

```python
from BatAlgorithm import BatAlgorithm
from Graph import create_full_graph
from Graph import plot_graph_solution
import matplotlib.pyplot as plt


g = create_full_graph(6) #Create a full conected graph 

algorithm = BatAlgorithm(5, 50, 1.0, 5.0, 0.995, 0.995, 0.98, 0.02, g)
algorithm.print_population()

solution = algorithm.execute() #Start the execution

plt.plot(algorithm.history)
plt.show() #Plotting the fitness evolution

plot_graph_solution(g, solution) #Plotting the graph with the best solution.
```

## Ouputs
**Plotting the fitness evolution**

![fitness](https://user-images.githubusercontent.com/25170552/87702600-e5f23180-c799-11ea-97b2-48db70e6f30a.png)

**Plotting the best solution**

![output](https://user-images.githubusercontent.com/25170552/87702176-5a78a080-c799-11ea-8c9f-b87454f88ea5.png)

## References

[1] Travelling Salesman Problem. (2020/07/16). Wikipedia. https://en.wikipedia.org/wiki/Travelling_salesman_problem

[2] Yassine Saji. & Mohammed Essaid Riffi. (2014). A novel discrete bat algorithm for solving the travelling salesman
problem. The Natural Computing Applications Forum 2015.

[3] Lijue Liu., Shuning Luo., Fan Guo. & Shiyang Tan.(2018). Multi‐point shortest path planning based on an Improved
Discrete Bat Algorithm. Applied Soft Computing Journal(2020).

[4] The igraph core team. (2020/07/16) Python Igraph manual. https://igraph.org/python/#docs
