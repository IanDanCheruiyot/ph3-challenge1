class Car:
    def __init__(self, make, model, year):
        # Initialize a new Car instance
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):

#Print the car's information
        print(f"Car Information: {self.make} {self.model} {self.year}")

# Example usage:
if __name__ == "__main__":
    # Create a new Car instance
    my_car = Car("volkswagen,", "Westfalia,", 1966)
    
    # Display the car's information
    my_car.display_info()
