def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    # Input temperature in Celsius
    celsius = float(input("Enter the temperature in Celsius: "))

    # Convert Celsius to Fahrenheit using the conversion formula
    fahrenheit = (celsius * 9/5) + 32

    # Print the temperature in Fahrenheit with two fractional values
    print("Fahrenheit: {:.2f}".format(fahrenheit))

    return celsius, fahrenheit
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
if __name__ == '__main__':
    main()
