# task 10-06

# Medical expenses

# import procedure
# import patient
from objects import procedure
from objects import patient

def main(): 
    procedure_1 = procedure.Procedure("Medical examination", "8-24-2019", "Irwin", 250.0)
    procedure_2 = procedure.Procedure("X-ray examination", "8-24-2019", "Jameson", 500.0)
    procedure_3 = procedure.Procedure("Blood test", "8-24-2019", "Smith", 200.0)
    
    pat = patient.Patient("James", "Edward", "Jones", "123 Mane street", "Billings", "Montana", "59000", "406-555-1212", "Jenny Jones", "406-555-1213")
    
    print(pat)
    print(procedure_1)
    print(procedure_2)
    print(procedure_3)
    
# Call main function 
main()
