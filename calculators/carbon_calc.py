def calculate_carbon_footprint(transportMethod, transportAmount, Ev, renewType, lights, heating, takeawayFreq, foodType):
    transportScore = calculate_transport_emissions(transportMethod, transportAmount, Ev)
    homeScore = calculate_home_emmissions(renewType, lights, heating)
    foodScore = calculate_food_emissions(takeawayFreq, foodType)
    score = transportScore + homeScore + foodScore
    result = create_result_message(score)
    return result, score


def calculate_transport_emissions(transportMethod, transportAmount, Ev):
    match transportMethod:
        case 'Car':
            methodScore = 0
        case 'Public_Transport':
            methodScore = 1
        case 'Bicycle':
            methodScore = 2
        case 'Walking':
            methodScore = 3

    if transportAmount > 3:
        AmountScore = 2
    elif transportAmount > 5:
        AmountScore = 1
    elif transportAmount > 6:
        AmountScore = 0
    else:
        AmountScore = 3

    match Ev:
        case 'Yes':
            EVScore = 1
        case 'No':
            EVScore = 0
        case 'NA':
            EVScore = 2
    
    transportScore = methodScore + AmountScore + EVScore

    return transportScore


def calculate_home_emmissions(renewType, lights, heating):
    match renewType:
        case 'None':
            renewScore = 0
        case 'Solar':
            renewScore = 3
        case 'GroundSource':
            renewScore = 2
        case 'Wind':
            renewScore = 1
        case 'Hydro':
            renewScore = 4
    
    match lights:
        case 'Yes':
            lightScore = 3
        case 'No':
            lightScore = 1
        
    match heating:
        case 'Yes':
            heatingScore = 3
        case 'No':
            heatingScore = 1
    
    homeScore = renewScore + lightScore + heatingScore

    return homeScore

def calculate_food_emissions(takeawayFreq, foodType):
    match takeawayFreq:
        case 'Yes':
            takeawayScore = 1
        case 'No':
            takeawayScore = 3


    match foodType:
        case 'Yes':
            foodTypeScore = 1
        case 'No':
            foodTypeScore = 3

    foodScore = takeawayScore + foodTypeScore

    return foodScore


def create_result_message(score):
    if score > 20:
        result = "Well Done! You consistenly act to help reduce carbon emissions in every day tasks."
    elif score > 15:
        result = "Good Job! You do many things in your life to reduce your carbon emissions."
    elif score > 10:
        result = "You incorporate some measures into your life to help reduce your carbon footprint."
    elif score > 5:
        result = "You occasionaly do things to reduce your carbon footprint but do not go out of your way to do so."
    else:
        result = "You do little to nothing to reduce the amount of carbon you produce. "

    return result
    

