import random

def get_random_number(max_random_value):
    return random.randint(1, max_random_value)

def main():
    max_random_value = 6  
    is_continue_rolling_dice = True  

    while is_continue_rolling_dice:
        user_roll_dice = input("Ready to roll? Enter 'Q' to Quit: ")  

        if user_roll_dice.lower() != "q":  
            dice_value = get_random_number(max_random_value)  
            print("You have rolled:", dice_value)  
        else:
            is_continue_rolling_dice = False  
            
if __name__ == "__main__":
    main()  