import random

hands = ['Rock 🪨', 'Scissors ✂️' , 'Paper 📃']
results = {'win': 'you won 🎉🎉🎉🎉🎉🎉🎉' , 'lose': 'you lose 😭😭😭😭😭😭😭', 'draw': 'draw please play again'}

def start_message():
    print('Start Rock paper scissors Game')

def get_player():
    while True:
        print('Choose the number of your choice')
        for index , hand in enumerate(hands):
            print(f"{index} : {hand}")
        try:
            choice  = int(input("Enter the number you want "))
            if choice < 0 or choice > 2 :
                print('Please choose a valid number  0,1 or 2')
            else :
                return choice
        except ValueError:
            print(" you entered nothing")

def get_computer():
    return random.randint(0,2)

def  get_hand_name(hand_number):
    return hands[hand_number]

def view_hand(your_hand , computer_hand):
    print('\n')
    print('My hand ' + get_hand_name(your_hand))
    print('Computer hand ' + get_hand_name(computer_hand))

def get_result(hand_diff):
     if hand_diff == 0 :
         return 'draw'
     elif hand_diff == -1 or hand_diff == 2:
         return 'win'
     else :
         return 'lose'

def view_result(result):
            print(results[result]) 

      
def play():
    your_hand = get_player()
    computer_hand = get_computer()
    hand_diff = (your_hand - computer_hand) % 3

    if hand_diff == 0:
        draw(your_hand, computer_hand)
        play()  
    else:
        result = get_result(hand_diff)
        view_result(result)
        return result

def draw(your_hand, computer_hand):
    view_hand(your_hand, computer_hand)
    print(results['draw'])    
            

start_message()

your_hand = get_player()
computer_hand = get_computer()
hand_diff = your_hand - computer_hand

view_hand(your_hand,computer_hand)
result = get_result(hand_diff)
view_result(result)
play()

