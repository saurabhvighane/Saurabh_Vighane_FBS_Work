# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero


class Television:
    def __init__(self):
        self.model_no=0
        self.screen_size=0
        self.price=0

    def member(self):
        try:
            self.model_no=int(input("Enter model no: "))
            self.screen_size=int(input("Enter screen size: "))
            self.price=int(input("Enter price: "))

            if len(str(self.model_no))>4:
                raise ValueError("Model no should not be more than 4 digits")
            if self.screen_size<12 or self.screen_size>70:
                raise ValueError("Invalid Screen size")
            if self.price<0 or self.price>5000:
                raise ValueError("Invalid price")

        except ValueError as e:
            print(f'Error:{e}')

            self.model_no=0
            self.screen_size=0
            self.price=0

    def __str__(self):
        return (f'Model No:{self.model_no}\t'
                f'Screen size:{self.screen_size}\t'
                f'Price:{self.price}\t')


    def display(self):
        print("---Television Details---")
        print(f'Model No:{self.model_no}\t')
        print(f'Screen size:{self.screen_size}\t')
        print(f'Price:{self.price}\t')

tv=Television()
tv.member()
tv.display()