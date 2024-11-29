# Note: The original code that I wrote was one, cause I was bored and two, I didn't want to go back and change the variables again which is why this exist now with added inputs and such. Original code is commented out for my understanding on what I wrote and for your understanding also

import random

# The disclaimer
print('==========================================================================================================================================================================================\n')
print('DISCLAIMER!!!!!\n')
print('Please do not use this code to actually predict the outcomes of your scenarios, this code can\'t simulate real life and I\'ll never write it to be or close to be (mostly cause I\'m js lazy lol)\n')
print('Treat it like a old ass gambling machine and don\'t take anything this code produces seriously (aka don\'t end up like the guy killing himself over a ch.ai bot...)\n')
print('(PS: If your using the exe version, dm me for the python file or go back to github where I have the original code there.\n)')
print('==========================================================================================================================================================================================\n')

original = input('What\'s you orignal scenario for this? \n\n')

# Define traits as variables specific to your scenario
'''
traits = {
    "variable_1": 6,  # Replace with relevant variable (e.g., input_power)
    "variable_2": 8,  # Replace with relevant variable (e.g., material_quality)
    "variable_3": 5   # Replace with relevant variable (e.g., environment_temp)
}
'''

traits = {}
# Ask user for variables and their values then puts them into traits
num_traits = int(input('\nHow many variables do you want? \n\n'))

for i in range(num_traits):
    trait_name = input('\nWhat variable do you want to add? \n\n')
    trait_value = int(input(f'\nEnter the original value for the variable {trait_name.upper()}? \n\n'))

    traits[trait_name] = trait_value

# Example actions and their impacts
'''
actions = [
    {"action": "Action 1 (e.g., increase power)", "impact": +10},
    {"action": "Action 2 (e.g., change material)", "impact": -5},
    {"action": "Action 3 (e.g., adjust temperature)", "impact": +20},
]
'''

actions = []
# Asks user for the actions and their impact to the original variables they've listed above
num_actions = int(input('\nHow many actions have happened that impacted your original scenario? \n\n'))

for i in range(num_actions):
    action_name = input('\nWhat action do you want to add? \n\n')
    action_impact = int(input(f'\nEnter the impact of the action {action_name.upper()}? (Use + for a positive impact and - for a negative impact) \n\n'))
    actions.append({'action': action_name,'impact': action_impact})

# Asking user for the initial score for the scenario (e.g., starting condition or baseline)
initial_score = int(input('\nWhat do you want the intial score of the scenario to be? \n\n'))

# Simulate the scenario and calculate probabilities for outcomes
def simulate_scenario():
    # Modify the impact based on traits
    '''
    factor_1 = traits["variable_1"] * 0.2  # Adjust the weight as needed
    factor_2 = (10 - traits["variable_2"]) * 0.2  # Adjust weight for the second variable
    factor_3 = traits["variable_3"] * 0.3  # Adjust weight for the third variable
    '''

    factors = {}
    # Ask user for the factors they want to add and add them to factors
    num_factors = int(input('\nHow many variables do you want to add to the calculation (put 0 if you want all variables to be added)? \n\n'))

    if num_factors == 0:
        for i in range(len(traits)):
            factor_name = input(f'\nWhat factor do you want to add the weight first? \n\n')
            if factor_name not in traits:
                print(f"Error: The factor '{factor_name}' does not exist in traits. Please add it first.")
                break
            weight = float(input(f'\nEnter the weight for the factor {factor_name.upper()}: \n\n'))
            factors[factor_name] = weight
    else:
        for i in range(num_factors):
            factor_name = input(f'\nWhat factor do you want to change? \n\n')
            if factor_name not in traits:
                print(f"Error: The factor '{factor_name}' does not exist in traits. Please add it first.")
                break
            weight = float(input(f'\nEnter the weight for the factor {factor_name.upper()}: \n\n'))
            factors[factor_name] = weight

    # Generate the factor calculations dynamically
    total_factor_score = sum(traits[factor] * weight for factor, weight in factors.items())

    # Add randomness to try and somewhat simulate real life
    rand1 = int(input('\nPick a number: \n\n'))
    rand2 = int(input('\nPick another number bigger than the first number: \n\n'))
    random_factor = random.randint(rand1, rand2)

    # Define outcomes and their probabilities
    '''
    outcome_1 = max(0, min(100, (final_score - 90) * 2))  # Example: Excellent Outcome
    outcome_2 = max(0, min(100, (final_score - 70) * 1.5))  # Example: Moderate Outcome
    outcome_3 = max(0, 100 - (outcome_1 + outcome_2))  # Example: Neutral Outcome
    '''

    outcomes = {}
    total_probability = 0
    random_factor = random.randint(0, 100)
    # Asking user for the number of outcomes they want for their scenario
    num_outcomes = int(input('\nHow many outcomes do you want for your scenario? \n\n'))
    for i in range(num_outcomes):
        outcome_name = input('\nWhat\'s the outcome? \n\n')
        weight = float(input('\nHow likely is this outcome? \n\n'))
        outcomes[outcome_name] = weight
        
    for action in actions:
        base_impact = action["impact"]

        # Calculate final score
        final_score = initial_score + base_impact + total_factor_score + random_factor

        # Calculate probabilities for each outcome
        outcome_probabilities = {}
        for outcome, weight in outcomes.items():
            probability = max(0, min(100, (final_score - random_factor) * weight))
            outcome_probabilities[outcome] = probability
            total_probability += probability

        # Normalize probabilities
        total_probability = sum(outcome_probabilities.values())
        for outcome in outcome_probabilities:
            outcome_probabilities[outcome] = (outcome_probabilities[outcome] / total_probability) * 100

        # Add neutral outcome
        neutral_outcome = max(0, 100 - sum(outcome_probabilities.values()))
        outcome_probabilities["Neutral Outcome"] = neutral_outcome

        # Normalize percentages to sum to 100%
        '''
        total = outcome_1 + outcome_2 + outcome_3
        outcome_1 = (outcome_1 / total) * 100
        outcome_2 = (outcome_2 / total) * 100
        outcome_3 = (outcome_3 / total) * 100
        '''

        # Beginning of outputting the results (header)
        print('\nOriginal Scenario: \n')
        print(f'{original.upper()} \n')
        print(f"Initial Score: {initial_score}\n")
        print("\nAlternative Scenarios with Outcome Probabilities:\n")

        # Normalize the probabilities to ensure the sum is 100%
        total_probability = sum(outcome_probabilities.values())
        for outcome in outcome_probabilities:
            outcome_probabilities[outcome] = (outcome_probabilities[outcome] / total_probability) * 100
            # Output the results
            '''
            print(f"Action: {action['action']}")
            print(f"  Final Score: {final_score:.2f}")
            print(f"  Outcome 1 (e.g., Excellent): {outcome_1:.2f}%")
            print(f"  Outcome 2 (e.g., Moderate): {outcome_2:.2f}%")
            print(f"  Outcome 3 (e.g., Neutral): {outcome_3:.2f}%\n")
            '''

        print(f"Action: {action['action'].upper()}")
        print(f"  Final Score: {final_score:.2f}")
        for i, (outcome, probability) in enumerate(outcome_probabilities.items(), start=1):
            print(f"  {outcome.upper()}): {probability:.2f}%")
            
# Run the simulation
simulate_scenario()