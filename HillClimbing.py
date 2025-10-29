import math

function_input = input("Enter the function in terms of x : ")
start_x = float(input("Enter starting value of x: "))
step_size = float(input("Enter step size : "))
max_iterations = int(input("Enter maximum number of iterations: "))

# --- Objective Function ---
def f(x):
    # Evaluate user-defined function safely
    return eval(function_input, {"x": x, "math": math})

def hill_climbing(f, start_x, step_size, max_iterations):
    current_x = start_x
    current_value = f(current_x)

    print("\nHill Climbing Search : ")
    print(f"Initial: x = {current_x:.4f}, f(x) = {current_value:.4f}")

    for i in range(max_iterations):
        # Generate two neighboring points
        next_x1 = current_x + step_size
        next_x2 = current_x - step_size

        # Evaluate both neighbors
        next_val1 = f(next_x1)
        next_val2 = f(next_x2)

        # Choose the better neighbor
        if next_val1 > current_value:
            current_x, current_value = next_x1, next_val1
        elif next_val2 > current_value:
            current_x, current_value = next_x2, next_val2
        else:
            print(f"No better neighbor found at iteration {i+1}. Local maximum reached.")
            break

        print(f"Iteration {i+1}: x = {current_x:.4f}, f(x) = {current_value:.4f}")

    return current_x, current_value

# Run the Algorithm 
best_x, best_val = hill_climbing(f, start_x, step_size, max_iterations)

print("\nFinal Result :")
print(f"Best solution found: x = {best_x:.4f}")
print(f"Maximum value: f(x) = {best_val:.4f}")

# Enter the function in terms of x :  -(x-3)**2 + 9
# Enter starting value of x: 2
# Enter step size : 0.2
# Enter maximum number of iterations: 5

# Hill Climbing Search :
# Initial: x = 2.0000, f(x) = 8.0000
# Iteration 1: x = 2.2000, f(x) = 8.3600
# Iteration 2: x = 2.4000, f(x) = 8.6400
# Iteration 3: x = 2.6000, f(x) = 8.8400
# Iteration 4: x = 2.8000, f(x) = 8.9600
# Iteration 5: x = 3.0000, f(x) = 9.0000



        # f(x)
        #   |
        # 9 |           ●  (3,9)
        #   |        ●     ●
        #   |      ●         ●
        #   |    ●             ●
        #   |  ●                 ●
        #   |●______________________ x
        #                3
