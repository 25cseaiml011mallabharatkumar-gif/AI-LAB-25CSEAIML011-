"""hill climbing is the local search algorithm that repeatedly moves to the neighbouring state with the highest value until no better neighbour exists."""
"""
example of hill climbing algorithm are :
1.chess game
2.moving chairs in the lab

then a graph
  |
  |
  |
  |
  |
  |
  |
  |
  |
  | 
  |
  --------------------------------------------------
"""
"""
limitations of hill climbing algorithm are :
1. it can get stuck in local maxima
2. it can get stuck in plateaus
3. it can get stuck in ridges
"""
"""
objective function :
  f(x) = -(x-5)**2 + 25
  f(1) = 9
  f(2) = 16
  f(3) = 21
  f(4) = 24
  f(5) = 25           ////graph for all this valeus
  f(6) = 24
  f(7) = 21
  f(8) = 16
  f(9) = 9
  f(10) = 0
"""
"""
f(x) = -(x-4)**2 + 16
f(1) = 7
f(2) = 12
f(3) = 15
f(4) = 16
f(5) = 15
f(6) = 12
f(7) = 9
f(8) = 4
"""
"""
f(x) = -(x-8)**2 + 64
f(1) = 
"""

"""
f(x)  = -0.5(x-6)**2 + 40
f(1) = 7.5

"""

def objective_function(x):
    return -(x**2) +10
def hill_climbing(start,step_size,max_iterations):
    current = start
    current_value = objective_function(current)
    for i in range(max_iterations):
        left  = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        #move to the better neighbour
        if left_value >current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break
    return current,current_value

#main program
start = float(input("Enter the starting point : "))
step_size = float(input("Entet the step size :"))
max_iterations = int(input("Enter the maximum iterations : "))

best_position,best_value = hill_climbing(start,step_size,max_iterations)

print("\n Best position = ",best_position)
print("Maximum value =",best_value)

