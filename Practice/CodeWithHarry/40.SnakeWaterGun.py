# This program is not complete yet. Hence, it throws error

def main():
    import random

    def getKey(val):
        """getKey() returns the key of a specific value in a dictionary """
        for key,value in plays.items():
            if val == value:
                 return key
            else:
                return "key doesn't exist"

    play_options = ["snake", "water", "gun"]

    _input = input("Your play: snake(s)   water(w)   gun(g) >> ")
    if _input == 's':
        user_choice = 'snake'
    elif _input == 'w':
        user_choice = 'water'
    elif _input == 'g':
        user_choice = 'gun'
    else:
        print("Please play seriously!!!")
        return

    bot_choice = random.choices(play_options)
    plays = {'user':user_choice, 'bot':bot_choice}

    if user_choice == bot_choice:
        result = "It's a tie"
    elif [user_choice,bot_choice] == ['snake','water']:
        if getKey('snake') == 'user': result = "You won!"
        else: result = "You lose...😒"
    elif [user_choice, bot_choice] == ['snake', 'gun']:
        if getKey('gun') == 'user': result = "You won!"
        else: result = "You lose...😒"
    elif [user_choice, bot_choice] == ['water', 'gun']:
        if getKey('water') == 'user': result = "You won!"
        else: result = "You lose...😒"

    print(result)

main()