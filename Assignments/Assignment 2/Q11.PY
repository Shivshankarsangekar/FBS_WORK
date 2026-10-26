# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter amount: "))

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

notes_5 = amount // 5
amount = amount % 5

notes_2 = amount // 2
amount = amount % 2

notes_1 = amount // 1

total_notes = notes_500 + notes_200 + notes_100 + notes_50 + notes_20 + notes_10 + notes_5 + notes_2 + notes_1

print("Minimum number of notes =", total_notes)