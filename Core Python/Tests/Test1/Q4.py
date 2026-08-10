# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

def CalculatePaintingCost():
    area = float(input("Enter the area of one wall: "))
    interior = float(input("Enter the interior painting cost per unit area: "))
    exterior = float(input("Enter the exterior painting cost per unit area: "))
    
    exterior_faces = 6
    interior_faces = 8
    
    total_exterior = exterior_faces * area * exterior
    total_interior = interior_faces * area * interior
    total_cost = total_exterior + total_interior
    
    print(f"\n--- Painting Cost Estimate ---")
    print(f"Total Exterior Cost: {total_exterior:.2f}")
    print(f"Total Interior Cost: {total_interior:.2f}")
    print(f"Total Combined Cost: {total_cost:.2f}")

CalculatePaintingCost()
