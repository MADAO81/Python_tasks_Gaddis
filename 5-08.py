# Appraiser of painting works.
# The painting company found that for every 10 square meters of wall surface, 
# 5 liters of paint and 8 hours of work are required. The company
# charges 2,000 rubles per hour for the work. Write a program that asks the user
# to enter the surface area of the wall to be painted and the price of a 5-liter container of paint. 
# The program should show the following data:
# • number of required paint containers; 
# • number of required working hours; 
# • price of paint; 
# • price of work; 
# • the total cost of painting work.
PRICE_WORK_HOUR = 2000 # Price of one working hour in roubles
PAINT_CONSUMPTION = 0.5 # Paint consumption per square meter
HOURS_METER = 0.8 # The time required to paint one square meter

def main():
    painted_area = float(input("Enter the area to be painted, sq.meters: "))
    can_paint_price = float(input("Enter the price of 5-liter can, roubles: "))
    total = price_paint(can_paint_price,painted_area) + price_work(painted_area)
    print(f"Quantity of required paint containers: {paint_cont(painted_area)}")
    print(f"Required working hours: {work_hours(painted_area)}")
    print(f"Total price of paint: {price_paint(can_paint_price,painted_area):,.2f}")
    print(f"Total price of work: {price_work(painted_area):,.2f}")
    print(f"Total price of renovation: {total:,.2f}")
    
def paint_cont(area): # quantity of required paint containers
    containers_quantity = area * PAINT_CONSUMPTION
    return containers_quantity
    
def work_hours(area): # quantity of required working hours 
    total_work_hours = area * HOURS_METER
    return total_work_hours
    
def price_paint(price,area): # total price of paint 
    total_price_paint = price * paint_cont(area)
    return total_price_paint
    
def price_work(area): # total price of work
    total_price_work = work_hours(area) * PRICE_WORK_HOUR 
    return total_price_work
    
main()
    
