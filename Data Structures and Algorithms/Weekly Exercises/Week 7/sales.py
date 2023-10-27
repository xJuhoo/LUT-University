# Week 7: Exercise 1
# Juho Rekonen

def sales(cars, customers):
    # Sorting both lists
    cars.sort()
    customers.sort()
    
    counter = 0

    # Using two pointers, one for the cars and one for the customers
    # to iterate through them simultaneosly
    pCar = 0
    pCustomer = 0
    
    while pCar < len(cars) and pCustomer < len(customers):
        if cars[pCar] <= customers[pCustomer]:
            counter += 1
            pCar += 1
        pCustomer += 1

    return counter


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))          # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5
