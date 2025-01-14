#To implement A* search for solving the 8-puzzle problem, you can follow this roadmap:

#1. **Define the Goal State**: Specify the goal state of the puzzle, typically `[[1, 2, 3], [4, 5, 6], [7, 8, 0]]`.

#2. **State Representation**: Ensure that the state of the puzzle is represented in a way that can be easily manipulated and compared.

#3. **Heuristic Function**: You already have a heuristic function (`getHeuristic`) that calculates the Manhattan distance. Ensure it is correctly implemented.

#4. **Cost Function**: Implement the cost function (`getCost`) which typically returns the number of moves made from the initial state to the current state.

#5. **Priority Queue**: Use a priority queue to store the frontier nodes, prioritized by their total cost (heuristic + cost).

#6. **Node Expansion**: Implement a function to expand nodes, generating all possible valid moves (up, down, left, right) from the current state.

#7. **Goal Test**: Implement a function to check if the current state matches the goal state.

#8. **Tracking Visited States**: Use a set or dictionary to keep track of visited states to avoid processing the same state multiple times.

#9. **Reconstruct Path**: Once the goal state is reached, reconstruct the path from the initial state to the goal state.

#10. **Main A* Algorithm**: Combine all the above components in the main A* algorithm loop:
#    - Initialize the priority queue with the initial state.
#    - Loop until the priority queue is empty or the goal state is found.
#    - Dequeue the node with the lowest total cost.
#    - If the node is the goal state, reconstruct and return the path.
#    - Otherwise, expand the node and add the resulting states to the priority queue if they haven't been visited.
#
#By following this roadmap, you can implement the A* search algorithm to solve the 8-puzzle problem.



from queue import PriorityQueue as pq

state = [[3, 2, 1], [4, 8, 6], [7, 0, 5]]

class Puzzle:

    def __init__(self,initialState=((1,2,3),(4,5,6),(7,8,0))):
        self.initialState = initialState
        self.currentState = [list(row) for row in self.initialState]
        self.goalState = (1,2,3),(4,5,6),(7,8,0)
        self.moves = 0 
        self.VisitedState ={}

    def isGoal(self):
        return self.currentState == self.goalState
        
    def getHeuristic(self):
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if self.currentState[i][j] != 0:
                    row = int((self.currentState[i][j] - 1) / 3)
                    col = (self.currentState[i][j] - 1) % 3
                    val = abs(row - i) + abs(col - j)
                    print(val, end=" ")
                    heuristic += val
                else:
                    print('x', end=" ")
            print("\n")
        return heuristic
    
    def findZeroPosition(self):
        for i in range(3):
            for j in range(3):
                if self.currentState[i][j]==0:
                    return {i,j}
                
    def findNodes(self):
        i,j =self.findZeroPosition()


        

    def getCost(self):
        return self.moves

    def totalCost(self):
        return self.getHeuristic(state) + self.getCost()


pz = Puzzle(((3,2,1),(4,8,6),(7,0,5)))
cost = pz.getHeuristic()
print(cost)