class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des, to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_des=from_des
        self.to=to
        self.seats=["Empty" for i in range(20)]


class Phitron_Company: #this task is for admin
    total_bus=5
    total_bus_lst=[]
    def  install(self):
        bus_no=int(input("Enter bus NO: "))
        flag=1
        for bus in self.total_bus_lst:
            if bus_no==bus['coach']:
                print("The bus is already installed")
                flag=0
                break
        if flag:
            driver=input("Enter Driver Name: ")
            arrival=input("Enter Arrival Time: ")
            departure=input("Enter Departure Time: ")
            from_des=input("Enter Starting Point: ")
            to=input("Enter Ending Point: ")
            self.new_bus=Bus(bus_no,driver,arrival,departure,from_des,to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("Successfully Bus Installed\n")
            return


class BusCounter(Phitron_Company):
    user_list=[]
    bus_seat=20
    def ticket_booking(self):
        bus_no=int(input("Enter Bus Number: "))
        flag=0
        for bus in self.total_bus_lst:
            if bus_no==bus["coach"]:
                passenger=input("Enter Your Name: ")
                seat_no=int(input("Enter which seat you want: "))
                if seat_no-1 > self.bus_seat:
                   flag=1
                   break
                elif bus['seats'][seat_no-1]=="Empty":
                    bus['seats'][seat_no-1]=passenger
                    print("Thanks! Your Ticket Booking is Confirmed\n")
                    flag=1
                    break
                else:
                    print("The seat is already booked\n")
                    flag=1
                    break
        if flag==0:
            print("This bus is not available\n")


    def BusInformation(self):
       bus_no=int(input("Enter Bus No: "))
       count_bus=len(self.total_bus_lst)
       if count_bus<=0:
           return f"There is no bus available"
       for bus in self.total_bus_lst:
           if bus_no==bus['coach']:
               print('\n')
               print(f"{' '*8}{'#'*15}{' BUS INFORMATION '}{'#'*15}\n")
               print(f"Bus No: {bus_no}\t\t\tDriver: {bus['driver']}")
               print(f"Arrival Time: {bus['arrival']}\t\tDepurture Time: {bus['departure']}")
               print(f"Borading: {bus['from_des']}\t\t\tDestination: {bus['to']}\n")
               print("\n")
               a=1
               for i in range(5):
                   for j in range(2):
                       print(f"{a}.{bus['seats'][a-1]}", end=" ")
                       a += 1
                   print("\t",end="")
                   for j in range(2):
                       print(f"{a}.{bus['seats'][a-1]}", end=" ")
                       a += 1
                   print("\n")
               break
           else:
               print("This bus is not available\n")
               break
           
    def get_user(self):
        return self.user_list
    
    def create_account(self):
        name=input("Enter Your Name: ")
        flag=1
        for user in self.get_user():
            if name==user['username']:
                print("The user has already Exist\n")
                flag=0
                break
        if flag:
            password=int(input("Enter Your Password: "))
            self.new_user=User(name,password)
            self.user_list.append(vars(self.new_user))
    
    def Available_Bus(self):
        if len(self.total_bus_lst)==0:
            print("No Bus Available")
        else:
            for bus in self.total_bus_lst:
               print('\n')
               print(f"{' '*8}{'#'*15}{' AVAILABLE BUS '}{'#'*15}\n")
               print(f"Bus No: {bus['coach']}\t\t\tDriver: {bus['driver']}")
               print(f"Arrival Time: {bus['arrival']}\t\tDepurture Time: {bus['departure']}")
               print(f"Borading: {bus['from_des']}\t\t\tDestination: {bus['to']}\n")
               print("\n")
               a=1
               for i in range(5):
                   for j in range(2):
                       print(f"{a}.{bus['seats'][a-1]}", end=" ")
                       a += 1
                   print("\t",end="")
                   for j in range(2):
                       print(f"{a}.{bus['seats'][a-1]}", end=" ")
                       a += 1
                   print("\n")

while True:
    counter=BusCounter()
    print("1. Create An Account\n2. Log in Account\n3. Exit")
    user_input=int(input("Enter Your Choice: "))
    if user_input==3:
        break
    elif user_input==1:
        counter.create_account()
    elif user_input==2:
        name=input("Enter Your name: ")
        password=int(input("Enter Password: "))
        Admin=False
        flag=0
        if name=="Admin" and password==123:
            Admin=True
        if Admin==False:
            for user in counter.get_user():
                if name==user['username'] and user['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print("1.Available Buses\n2.Show Bus Information\n3.Ticket Booking\n4.Exist")
                    user_input=int(input("Enter Your Choice: "))
                    if user_input==1:
                        counter.Available_Bus()
                    elif user_input==2:
                        print(counter.BusInformation())
                    elif user_input==3:
                        counter.ticket_booking()
                    else:
                        break
            else:
                print("Yor are not valid User\n")
        else:
            while True:
                print("Hello Admin! Welcome Back")
                print("1. Bus Install\n2. Available Bus\n3. Show Bus Information\n4. Show User List\n5. Exist")
                user_input=int(input("Enter Your Choice: "))
                if user_input==5:
                    break
                elif user_input==1:
                    counter.install()
                elif user_input==2:
                    counter.Available_Bus()
                elif user_input==3:
                    counter.BusInformation()
                elif user_input==4:
                    print(counter.get_user())









            


    
               

        



        
#company=Phitron_Company()
#company.install()
#print(company.total_bus_lst)



"""counter=BusCounter()
counter.BusInformation()
counter.ticket_booking()
print(counter.get_user())
counter.create_account()
print(counter.get_user())
counter.create_account()
print(counter.get_user()"""


        
            
