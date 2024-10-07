class Star_Cinema:
    hall_list=[]

    @classmethod
    def entry_hall(cls,hall_obj):
        cls.hall_list.append(hall_obj)


    @classmethod
    def view_all_shows(cls):
        print("--------Welcome to the Star_cinema Hall---------")
        for hall in cls.hall_list:
            hall.view_show_list()
        print("---------Thank You For Visiting---------")

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no

        self.entry_hall(self)

    def entry_show(self,show_ID,movie_name,time):
        show = (show_ID,movie_name,time)    
        self.show_list.append(show)

        seats = [[0] * self.cols for _ in range(self.rows)]  # 2d list 
        self.seats[show_ID] = seats

    def book_seats(self,show_ID,show_list):
        if show_ID not in self.seats:
            print(f"INVALID SHOW ID '{show_ID}'")
            return 
        
        seats = self.seats[show_ID]
        for row,col in show_list:
            if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
                print("INVALID SEAT")
                continue
            if seats[row][col] == 1:
                print("SEAT HAS BEEN BOOKED ALREADY")
            else:
                seats[row][col] = 1
                print("SEAT BOOKED SUCCESSFULLY")
        
    def view_show_list(self):
        for show in self.show_list:
            show_ID, movie_name, time  = show 
            print(f"Show_ID: {show_ID}, Movie_Name: {movie_name}, Movie_Time: {time}") 

    def view_available_seats(self,show_ID):
        if show_ID not in self.seats:
            print(f"INVALID SHOW ID '{show_ID}'")
            return
        print(f"Available seats for Show ID '{show_ID}':")
        seats = self.seats[show_ID]
        for row in range(self.rows):
            for col in range(self.cols):
                status = 'Available' if seats[row][col] == 0 else 'Booked'
                print(f"Seat ({row}, {col}): {status}")

def cinema():
    hall_1 = Hall(1,1,10)
    hall_1.entry_show("101","KGF","10:00 am")
    hall_1.entry_show("102","Pathan","12:00 pm")

    hall_2 = Hall(1,1,11)
    hall_2.entry_show("103","Jawan","10:00 am")
    hall_2.entry_show("104","Sultan","12:00 pm")

    hall_3 = Hall(1,1,13)
    hall_3.entry_show("105","Kalank","10:00 am")
    hall_3.entry_show("106","Hero","12:00 pm")

    while True:
        print("1.View all show today")
        print("2.View available seats")
        print("3.Book ticket")
        print("4.Exit")

        op = input("Enter Options: ")

        if op == '1':
            Star_Cinema.view_all_shows()

        elif op == '2':
            show_ID = input("Enter Your Show_ID to view available seats: ")
            for hall in Star_Cinema.Star_Cinema__hall_list:
                hall.view_available_seats(show_ID)     

        elif op == '3':
            show_ID = input("Enter Your Show_ID to Book Ticket: ")        
            seat_list=[]

            while True:
                seat = input("Enter seat (row,col) to book ticket")
                if seat.lower() == 'Done':
                    break

                row,col = map(int,seat.split(','))
                seat_list.append((row,col))

            for hall in Star_Cinema.hall_list:
                hall.book_seats(show_ID, seat_list)

        elif op == '4':
            print("Exit")
            break 
        else:
            print("Try Again")   

cinema()               






        
