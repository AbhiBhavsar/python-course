import random

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
    """
    return a dealt card
    """
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if 11 and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(user_score,computer_score):
    
    if user_score == computer_score:
        return "It's a draw"
    elif user_score > computer_score:
        return 'You Won'
    else:
        return 'You Lost'
    


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f"your cards are {user_cards}, opponents 1st card is {computer_cards[0]}")
    print(f"your score is {user_score}, opponents score is {computer_score}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        should_deal = input('Deal another card(Y) or Pass(N)?')
        if(should_deal=='y' or should_deal=='Y'):
            new_card = user_cards.append(deal_card())
        else:
            is_game_over=True

while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)