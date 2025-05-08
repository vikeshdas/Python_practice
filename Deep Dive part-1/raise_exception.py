"""
we raise exception in our program to stop excution rest of the program when if condition satisfy

- difference between raise and assert
riase is used to terminate the rest of the program if user enter unexpected value.it can be handle by except block.

assert is used to check the logical error not user input unlike exception 
"""

def check_positive(value):
    if value < 0:
        raise ValueError("Value cannot be negative")  
            # or 
        # raise Exception("Value cannot be negative")  
        
    
    print("Value is valid:", value)  

try:
    check_positive(-5)  # This will raise an exception
    print("This line won't execute")  # Skipped because exception was raised
except ValueError as e:
    print("Caught an error:", e)  # Handles the exception


