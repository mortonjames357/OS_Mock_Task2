# Function to calculate energy cost
def calculate_energy(wattage, hours, price):
    # Constants
    WATT_CONVERSION = 1000
    # Get kwh based on wattage, hours and conversion
    kwh = (wattage * hours) / WATT_CONVERSION

    # Get rounded cost based on kwh and price 
    cost = round(kwh * price, 2)

    # Return the data
    return cost