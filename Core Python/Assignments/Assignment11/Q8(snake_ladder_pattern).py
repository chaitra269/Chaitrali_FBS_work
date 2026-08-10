# Print 1 to 100 in snakes and ladder pattern.

# Generate rows from top-level down (100 to 1) to match layout visual flow
for row in range(10, 0, -1):
    # Calculate start and end boundary indices for the current row
    start = (row - 1) * 10 + 1
    end = row * 10
    
    row_elements = list(range(start, end + 1))
    
    # Reverse alternate rows (even rows in the 1-10 counting system)
    if row % 2 == 0:
        row_elements.reverse()
        
    # Format layout to look like a perfectly aligned game board grid
    for num in row_elements:
        print(f"{num:3}", end=" ")
    print()  # Newline after completing the row
