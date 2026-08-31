# A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100, 50, 20, 10, 5]
amount = int(input("Enter the amount: "))

print(f"\nTarget Amount: {amount}")
print("------------------------")
total_notes = 0
remaining_amount = amount
for note in D:
    if remaining_amount >= note:
        count = remaining_amount // note          # Find how many notes of this denomination fit
        remaining_amount = remaining_amount % note  # Calculate the left-over amount
        total_notes += count
        print(f"Notes of {note} : {count}")

print("------------------------")
print(f"Minimum total notes needed: {total_notes}")

if remaining_amount > 0:
    print(f"Remaining amount that couldn't be paid with available notes: {remaining_amount}")
