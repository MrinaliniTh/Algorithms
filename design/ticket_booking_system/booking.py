ROW = 20
SEATS = 20
BOOKED_SEATS = 0
TOTAL_SEATS = ROW * SEATS
SEAT_CHART = {}
RUN_COUNT = 10
booking_details = {}
prize_of_ticket = 0

class Chart:
    @staticmethod
    def chart_maker():
        for i in range(ROW):
            seats_in_row = {}
            for j in range(SEATS):
                seats_in_row[j + 1] = '$'
            SEAT_CHART[i] = seats_in_row
        return SEAT_CHART

chart = Chart()
table_of_chart = chart.chart_maker()
print(table_of_chart)

while RUN_COUNT != 0:
    print("1. Show the seats")
    print("2. Buy a ticket")
    print("3. Show statistics")
    print("4. Show booked tickets")
    RUN_COUNT = int(input("Select option - "))
    if RUN_COUNT == 1:
        print(0, end="  ")
        for key in table_of_chart.keys():
            if key < 9:
                print(key + 1, end="  ")
            else:
                print(key + 1, end=" ")
        print(end="\n")
        for key, val in table_of_chart.items():
            if key < 9:
                print(key + 1, end="  ")
            else:
                print(key + 1, end=" ")
            for k, v in val.items():
                print(v, end="  ")
            print(end="\n")
    elif RUN_COUNT == 2:
        row = int(input("Select row - "))
        seat = int(input("Select seat - "))
        if table_of_chart[row][seat] == '$':
            name = input("Enter your name ")
            email = input("Enter your email ")
            age = int(input("Enter your age "))
            ans = input("Do you want to proceed to payment ? Yes/No ")
            if ans.lower() == "yes":
                table_of_chart[row-1][seat] = 'B'
                TOTAL_SEATS -= 1
                if seat < 10:
                    prize_of_ticket = 1000
                else:
                    prize_of_ticket = 800

                booking_details[row+seat] = {"seat": (row, seat),
                                         "name": name,
                                         "age": age,
                                         "email": email,
                                         "prize_of_ticket": prize_of_ticket}
            else:
                continue
        else:
            print("Seats already occupied, select other seat")
            continue
    elif RUN_COUNT  == 4:
        row = int(input("Select row -"))
        seat = int(input("Select seat -"))
        if row <= ROW and seat <= SEATS:
            if table_of_chart[row-1][seat] == 'B':
                person = booking_details[row + seat]
                print('Name - ', person['name'])
                print('Gender - ', person['email'])
                print('Age - ', person['age'])
                print('Ticket Prize - ', 'Rs', person['prize_of_ticket'])


    