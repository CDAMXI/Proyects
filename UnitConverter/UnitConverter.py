def FaranheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0

def CelsiusToFaranheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32

def MetersToFeet(meters):
    """Convert Meters to Feet."""
    return meters * 3.28084

def FeetToMeters(feet):
    """Convert Feet to Meters."""
    return feet / 3.28084

def KilogramsToPounds(kg):
    """Convert Kilograms to Pounds."""
    return kg * 2.20462

def PoundsToKilograms(pounds):
    """Convert Pounds to Kilograms."""
    return pounds / 2.20462

def LitersToGallons(liters):
    """Convert Liters to Gallons."""
    return liters * 0.264172

def GallonsToLiters(gallons):
    """Convert Gallons to Liters."""
    return gallons / 0.264172

def KilometersToMiles(km):
    """Convert Kilometers to Miles."""
    return km * 0.621371

def MilesToKilometers(miles):
    """Convert Miles to Kilometers."""
    return miles / 0.621371


if __name__ == "__main__":
    print("=== Unit Converter ===")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Liters to Gallons")
    print("8. Gallons to Liters")
    print("9. Kilometers to Miles")
    print("10. Miles to Kilometers")

    choice = int(input("Select a conversion (1-10): "))
    while choice < 1 or choice > 10:
        choice = int(input("Invalid choice. Select a conversion (1-10): "))

    # Dictionary simulating switch-case
    switch = {
        1: FaranheitToCelsius,
        2: CelsiusToFaranheit,
        3: MetersToFeet,
        4: FeetToMeters,
        5: KilogramsToPounds,
        6: PoundsToKilograms,
        7: LitersToGallons,
        8: GallonsToLiters,
        9: KilometersToMiles,
        10: MilesToKilometers
    }

    # Ask the user for the value to convert
    value = float(input("Enter the value you want to convert: "))

    # Get the correct function from the dictionary (switch)
    conversion_function = switch.get(choice)

    # Call the function and print the result
    result = conversion_function(value)
    print(f"Result: {result:.4f}")
