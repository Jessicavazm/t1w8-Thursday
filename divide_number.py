def divide_numbers():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

    # Perform the division
        result = dividend / divisor
        print(f"Result of division: {result}")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as error:
        print("Unexpected error occured: {error}")
    finally:
        print("Division operation closed.")

# Perform the division
divide_numbers()