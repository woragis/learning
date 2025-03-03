# Search Problems

- Initial State
- Actions
- Transition Model
- Goal Test
- Path cost function

## Node

keeps track of

- a state
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)

## Algorithms

### DFS

Stack  
Explores the deepest node

### BFS

Queue  
Explores the shallowest node

### Greedy Best-First Search

Uses Heuristic function

### A\* Search

Search algorithm that expands node with lowest value of g(n) + h(n)  
Uses Heuristic function and Cost

#### Optimal if

- h is admissible (never overestimates the true cost)
- h is consistent (for every node and successor)

### Minimax

### Depth-Limited Minimax

- Evaluation Function
