# Challenge Summary

Implement a breadth-first traversal on a graph.

## Whiteboard Process

[Whiteboard Link](https://docs.google.com/document/d/1UCzZOjfXXYsIdnBtkDz3n3Oel--LdFcyGJEkQ8kf6CU/edit?usp=sharing)

## Approach & Efficiency

The algorithm takes in a graph and creates a queue and a set of visited vertex. It then itreates through each vertex adding the vertex to the visited set and adding all of that vertex neighbors to the queue. Rinse and repeat. Returs the list of visted vertex

Big 0:

Time --> 0(n)

Space --> 0(n)

## Solution

[Code](python/data_structures/graph.py)
