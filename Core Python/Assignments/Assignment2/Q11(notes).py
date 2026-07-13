# WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount 
# start 
# take integer amount from user 
amount = int(input("Enter Amount: "))

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50 
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

note5 = amount // 5
amount = amount % 5

note2 = amount // 2
amount = amount % 2

note1 = amount
print(f"500 = {note500}")
print(f"200 = {note200}")
print(f"100 = {note100}")
print(f"50 = {note50}")
print(f"20 = {note20}")
print(f"10 = {note10}")
print(f"5 = {note5}")
print(f"2 = {note2}")
