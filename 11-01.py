# task 11-01
# Employee and ProductionWorker classes

def main():
    # Local valuables
    worker_name = ""
    worker_id = ""
    worker_shift = 0 
    worker_pay = 0.0 
    
    # Get data attributes 
    worker_name = input("Enter name: ")
    worker_id = input("Enter ID: ")
    worker_shift = int(input("Enter the number of shift: "))
    worker_pay = float(input("Enter the hourly pay rate: "))
    
    # Create an instance of the ProductionWorker class
    worker = emp_prod.ProductionWorker(worker_name, worker_id, worker_shift, worker_pay)
    
    # Show info 
    print("Information about the production worker: ")
    print("Name: ", worker.get_name())
    print("ID: ", worker.get_id_number())
    print("Shift: ", worker.get_shif_number())
    print("Pay rate: , $", format(worker.get_pay_rate(), ",.2f"), sep="")
    
# call main function 
main()