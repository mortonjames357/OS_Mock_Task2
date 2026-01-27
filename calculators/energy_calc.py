def calculate_energy(wattage, hours, price):
    WATT_CONVERSION = 1000
    kwh = (wattage * hours) / WATT_CONVERSION

    cost = round(kwh * price, 2)

    return cost