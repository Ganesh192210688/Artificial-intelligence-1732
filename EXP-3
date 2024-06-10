def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # To store visited states to avoid infinite loops
    visited = set()
    # To store the sequence of operations
    path = []
    
    # Initial state
    jug1 = 0
    jug2 = 0
    visited.add((jug1, jug2))
    path.append((jug1, jug2))
    
    while jug1 != target and jug2 != target:
        # Case 1: Empty Jug2 if it is full
        if jug2 == jug2_capacity:
            jug2 = 0
        # Case 2: Fill Jug1 if it is empty
        elif jug1 == 0:
            jug1 = jug1_capacity
        # Case 3: Pour water from Jug1 to Jug2 without overflowing Jug2
        else:
            amount_to_pour = min(jug1, jug2_capacity - jug2)
            jug1 -= amount_to_pour
            jug2 += amount_to_pour
        
        # If we've already seen this state, break to avoid infinite loop
        if (jug1, jug2) in visited:
            break
        
        visited.add((jug1, jug2))
        path.append((jug1, jug2))
    
    return jug1, jug2, path

if _name_ == "_main_":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    jug1_final, jug2_final, path = water_jug_problem(jug1_capacity, jug2_capacity, target)
    print(f"Final state: Jug1: {jug1_final} gallons, Jug2: {jug2_final} gallons")
    print("Path to solution:")
    for state in path:
        print(f"Jug1: {state[0]}, Jug2: {state[1]}")
        
OUTPUT:
Final state: Jug1: 2 gallons, Jug2: 3 gallons
Path to solution:
Jug1: 0, Jug2: 0
Jug1: 4, Jug2: 0
Jug1: 1, Jug2: 3
Jug1: 1, Jug2: 0
Jug1: 0, Jug2: 1
Jug1: 4, Jug2: 1
Jug1: 2, Jug2: 3
