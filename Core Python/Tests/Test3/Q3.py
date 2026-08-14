# Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

num_employees = int(input("Enter the number of employees (n): "))
total_company_payout = 0.0

for i in range(1, num_employees + 1):
    print(f"\n--- Employee {i} ---")
    basic_salary = float(input(f"Enter the basic salary for employee {i}: "))
    
    if basic_salary < 20000:
        da_percent = 0.10   # 10%
        ta_percent = 0.12   # 12%
        hra_percent = 0.15  # 15%
    else:
        da_percent = 0.15   # 15%
        ta_percent = 0.18   # 18%
        hra_percent = 0.20  # 20%
        
    da = basic_salary * da_percent
    ta = basic_salary * ta_percent
    hra = basic_salary * hra_percent
    
    individual_total_salary = basic_salary + da + ta + hra
    total_company_payout += individual_total_salary
    
    print(f"DA (Dearness Allowance) : {da:.2f}")
    print(f"TA (Travel Allowance)   : {ta:.2f}")
    print(f"HRA (House Rent Allow.) : {hra:.2f}")
    print(f"Total Salary            : {individual_total_salary:.2f}")

print("\n========================================")
print(f"Total Salary of All Employees: {total_company_payout:.2f}")
print("========================================")
