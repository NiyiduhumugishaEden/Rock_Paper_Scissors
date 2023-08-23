import random 

sides = ['head' , 'tail']
results = {'win': 'win' , 'lose':'lose'}

def start_message():
    print("Start coin toss")

def  get_my_side():
    while True:
        for index , side in enumerate(sides):
            print(f"{index} : {side}")

        try:
            choice  = int(input("Input your bet : "))
            if choice <0 or choice >1 :
                print("Invalid input")
            else:
                return choice
        except ValueError:
            print("you entered nothing or a string ")

           
def get_coin_side():
      return random.randint(0,1)

def get_side_name(side_name):
    return sides[side_name]


def view_side(my_bet, coin_bet):
    print("My bet is : " +  get_side_name(my_bet))
    print("Coin is : " +  get_side_name(coin_bet))

def get_result(side_diff):
     if side_diff == 0 : 
         return 'win'
     else:
         return 'lose'

def view_result(result):
    print(results[result]) 

def play():
    my_bet = get_my_side()
    coin_bet = get_coin_side()
    side_diff  = my_bet - coin_bet
    result = get_result(side_diff)
    
    view_side(my_bet,coin_bet)
    view_result(result)


start_message()
play()




