try: 
    n = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"You entered: {n}")
finally:
    print("Execution completed.")
