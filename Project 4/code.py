# Node of the adjacency list
class Node:
    def __init__(self, target_vertex, edge_color):
        self.target_vertex = target_vertex
        self.edge_color = edge_color
        self.next = None


# LinkedList for the adjacency list
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        node.next = self.head
        self.head = node


# ----------------------------------------------------------------------------------------------------------------------
# the function to solve the problem
def solve(r_vertex, l_vertex):

    # if this function was called with the same parameters before, we must not execute it again, because it'll
    # create an infinite loop
    if called[r_vertex][l_vertex]:
        return 0

    called[r_vertex][l_vertex] = True

    # this variable indicates if this state will get into a dead end
    dead_end = True

    # let's try to move Rocket
    r_adjacent = graph[r_vertex].head
    while r_adjacent is not None:  # while there is an adjacent vertex
        if r_adjacent.edge_color == colors[l_vertex]:  # if it is possible to move on that edge
            dead_end = False  # there's a hope that this path will no get to a dead end
            solution.append('R ' + str(r_adjacent.target_vertex + 1))  # adding the step

            # check if we will get to the finish room
            if r_adjacent.target_vertex == n - 1:
                return 1   # indicating that the solution is found and there's no need to search anymore

            # if we won't get to the finish room, we must call the function recursively
            res = solve(r_adjacent.target_vertex, l_vertex)
            if res == 1:  # if the path got to the finish room
                return 1
            if res == 0:  # if the path failed to get to the finish room
                dead_end = True  # we lost our hope on this path
                if len(solution) != 0:
                    solution.pop()  # take back the last step
        r_adjacent = r_adjacent.next

    # -------------------------------------------------------------------
    # let's try to move Lucky
    l_adjacent = graph[l_vertex].head
    while l_adjacent is not None:  # while there is an adjacent vertex
        if l_adjacent.edge_color == colors[r_vertex]:  # if it is possible to move on that edge
            dead_end = False  # there's a hope that this path will no get to a dead end
            solution.append('L ' + str(l_adjacent.target_vertex + 1))  # adding the step

            # check if we will get to the finish room
            if l_adjacent.target_vertex == n - 1:
                return 1  # indicating that the solution is found and there's no need to search anymore

            res = solve(r_vertex, l_adjacent.target_vertex)
            if res == 1:  # if the path got to the finish room
                return 1
            if res == 0:  # if the path failed to get to the finish room
                dead_end = True  # we lost our hope on this path
                if len(solution) != 0:
                    solution.pop()  # take back the last step
        l_adjacent = l_adjacent.next

    # if we couldn't get to the finish room from this state by any means
    if dead_end:
        return 0  # inform the parent function


# ----------------------------------------------------------------------------------------------------------------------
# getting the inputs:

# getting n, m
n, m = input().split()
n = int(n)
m = int(m)

# storing color of the vertices
colors = input().split()

# start vertex of Rocket and Lucky
s1, s2 = input().split()
s1 = int(s1) - 1
s2 = int(s2) - 1

# creating the Adjacency List to store the graph
graph = [LinkedList() for i in range(n)]
for i in range(m):
    line = input().split()
    graph[int(line[0]) - 1].add(Node(int(line[1]) - 1, line[2]))

# this array shall have the solution steps
solution = []

# this array is used to check if solve() is called once to prevent any loops
called = [[False for i in range(n)] for j in range(n)]

# let's solve the problem
solve(s1, s2)

# printing the steps
for i in range(len(solution)):
    print(solution[i])
