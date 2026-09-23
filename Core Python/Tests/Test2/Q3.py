# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

def calculate_fencing_cost(radius, length, breadth, layers, cost_per_m):
    pi = 22 / 7 
    
    # Calculate components
    semicircle_arc = pi * radius
    outer_rectangle_sides = (2 * length) + breadth
    
    # Total perimeter for one round
    perimeter = outer_rectangle_sides + semicircle_arc
    
    # Total wire required for multiple loops
    total_wire_needed = perimeter * layers
    
    # Final cost
    total_cost = total_wire_needed * cost_per_m
    
    # Display results
    print(f"--- Fencing Estimation Breakdown ---")
    print(f"Perimeter of the field : {perimeter:.2f} meters")
    print(f"Total wire required    : {total_wire_needed:.2f} meters")
    print(f"Total cost of fencing  : ₹{total_cost:,.2f}")

# Field inputs from the problem statement
calculate_fencing_cost(
    radius=20, 
    length=50, 
    breadth=40, 
    layers=5, 
    cost_per_m=35
)
