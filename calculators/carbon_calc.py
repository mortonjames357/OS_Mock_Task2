# Function to call other functions, calculate total score and return the results
def calculate_carbon_footprint(transportMethod, transportAmount, Ev, renewType, lights, heating, takeawayFreq, foodType):
    # Get scores from other functions
    transportScore = calculate_transport_emissions(transportMethod, transportAmount, Ev)
    homeScore = calculate_home_emmissions(renewType, lights, heating)
    foodScore = calculate_food_emissions(takeawayFreq, foodType)
    # Calculate total score
    score = transportScore + homeScore + foodScore
    # Get result based on score
    result = create_result_message(score)
    # Return the data
    return result, score

# Function to calculate score for transport emmisions
def calculate_transport_emissions(transportMethod, transportAmount, Ev):
    # Match statement to get score for transport method data
    match transportMethod:
        case 'Car':
            methodScore = 0
        case 'Public_Transport':
            methodScore = 1
        case 'Bicycle':
            methodScore = 2
        case 'Walking':
            methodScore = 3

    # If statement to get score for transort amount
    if transportAmount > 3:
        AmountScore = 2
    elif transportAmount > 5:
        AmountScore = 1
    elif transportAmount > 6:
        AmountScore = 0
    else:
        AmountScore = 3
    
    # Match statement to get score for if they have an ev
    match Ev:
        case 'Yes':
            EVScore = 1
        case 'No':
            EVScore = 0
        case 'NA':
            EVScore = 2
    
    # Add all scores to get total transport score
    transportScore = methodScore + AmountScore + EVScore

    # Return the data
    return transportScore

# Function to calculate home emissions
def calculate_home_emmissions(renewType, lights, heating):
    # Match statement to get the score for the type of renewable energy they have 
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
    
    # Match statement to get score based on lights question
    match lights:
        case 'Yes':
            lightScore = 3
        case 'No':
            lightScore = 1
        
    # Match statement to get score based on heating question
    match heating:
        case 'Yes':
            heatingScore = 3
        case 'No':
            heatingScore = 1
    
    # Calculate total score from all scores
    homeScore = renewScore + lightScore + heatingScore

    # Return the data
    return homeScore

# Function to calculate food emission
def calculate_food_emissions(takeawayFreq, foodType):
    # Match statement to get score based on frequency of ordering food
    match takeawayFreq:
        case 'Yes':
            takeawayScore = 1
        case 'No':
            takeawayScore = 3

    # Natch statement to get score based on the type of food they eat
    match foodType:
        case 'Yes':
            foodTypeScore = 1
        case 'No':
            foodTypeScore = 3

    # Calculate the food score based on all score
    foodScore = takeawayScore + foodTypeScore
    
    # Return the data
    return foodScore

# Function to choose message based on score
def create_result_message(score):
    # If statement to set result based on the total score
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

    # Return the data
    return result
    

