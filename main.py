expenses = []

while True:
    print("1.Add 2.Total")
    c = input("> ")

    if c=="1":
        s = float(input("sum: "))
        expenses.append(s)

    if c=="2":
        print("Total:", sum(expenses))
