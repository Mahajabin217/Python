class Star_Cinema:
    hall_list=[]

    @classmethod
    def entry_hall(self,hall_obj):
        self.hall_list.append(hall_obj)

    @classmethod
    def view_all_shows(self):
        print("-----------Welcome to the Star_cinema Hall-----------")
        for hall in self.hall_list:
            hall.view_show_list()
        print("-------------Thank You For Visiting--------------")

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self,show_ID,movie_name,time):
        show = (show_ID,movie_name,time)    
        self.show_list.append(show)

        seats = [[0] * self.cols for _ in range(self.rows)]  # 2d list 
        self.seats[show_ID] = seats

    def view_show_list(self):
        for show in self.show_list:
            show_ID, movie_name, time  = show 
            print(f"Show_ID: {show_ID}, Movie_Name: {movie_name}, Movie_Time: {time}")   

    def view_available_seats(self,show_ID):
        if show_ID not in self.seats:
            print(f"NOT FOUND")
            return

        for row in self.seats[show_ID]:
            print(row)               

    def show_ID_checking(self,show_ID):
        if show_ID in self.seats:
            return True

        print("INVALID SHOW_ID")  

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
        
def cinema():
    hall= Hall(5,5,10)
    hall.entry_show(101,"KGF","10:00 am")
    hall.entry_show(102,"Pathan","12:00 pm")

    while True:
        print("1.View all show today")
        print("2.View available seats")
        print("3.Book ticket")
        print("4.Exit")

        op = int(input("Enter Options: "))

        if op == 1:
            Star_Cinema.view_all_shows()

        elif op == 2:
            show_ID = int(input("Enter Your Show_ID to view available seats: "))
            if not hall.show_ID_checking(show_ID):
                continue
            hall.view_available_seats(show_ID)

        elif op == 3:
            show_ID = int(input("Enter Your Show_ID to Book Ticket: ")) 

            if not hall.show_ID_checking(show_ID):
                continue
            try:
                tickets_number = int(input("ENTER NUMBER OF TICKETS: "))
            except ValueError:
                print("ENTER A VALID TICKET NUMBER")
                continue 
            
            tickets = []
            for i in range(tickets_number):
                print()
                rowS = f"ENTER ROW FOR SEAT {i + 1}:"
                colS = f"ENTER COLUMN FOR SEAT {i + 1}:"
                row = int(input(rowS))
                col = int(input(colS))
                tickets.append((row, col))

            hall.book_seats(show_ID,tickets)     

        elif op == 4:
            print("Exit")
            break 
        else:
            print("Try Again")   

cinema()               






        
