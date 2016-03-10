Distance = int(input("Distance Of Journey: "))
Passengers = int(input("How many passengers?: "))

if(Distance > 1):
    Distance -= 1
    TotalCost = Distance * 2 + 3
    if(Passengers >= 5):
        NewTotal = TotalCost / 2
        TotalCost = NewTotal + TotalCost
        print("Thanks for using out serivces, you traveled:", Distance, "km with", Passengers, "people!")
        print("Total to be paid: £" + str(TotalCost))
    else:
        print("Thanks for using out serivces, you traveled:", Distance, "km with", Passengers, "people!")
        print("Total to be paid: £" + str(TotalCost))
else:
    if(Passengers >= 5):
        print("Thanks for using out serivces, you traveled:", Distance, "km with", Passengers, "people!")
        print("Total to be paid: £4.50")
    else:
        print("Thanks for using out serivces, you traveled:", Distance, "km with", Passengers, "people!")
        print("Total to be paid: £3")
