import random

hand = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}
# AI hand


def computer_hand_item():
    c_hand_int = random.randint(1, 3)
    c_hand_item = hand[c_hand_int]
    return c_hand_item


def judge(c_hand_item, u_hand_item):

    if c_hand_item == "Rock":
        if u_hand_item == "Rock":
            return "Tie"
        elif u_hand_item == "Paper":
            return "You win !!!"
        else:
            return "Computer wins !!!"
    elif c_hand_item == "Paper":
        if u_hand_item == "Rock":
            return "Computer wins !!!"
        elif u_hand_item == "Paper":
            return "Tie"
        else:
            return "You win !!!"
    else:
        if u_hand_item == "Rock":
            return "You win !!!"
        elif u_hand_item == "Paper":
            return "Computer wins !!!"
        else:
            return "Tie !!!"

user_score = 0
computer_score = 0
while 1:

    print "Choose: Rock", "Paper", "Scissors"

    user_hand = raw_input()

    computer_hand = computer_hand_item()
    print "Computer's hand :", computer_hand
    decision = judge(computer_hand, user_hand)
    print decision
    if decision == "You win !!!":
        user_score += 1
    elif decision == "Computer wins !!!":
        computer_score += 1
    else:
        user_score += 0.5
        computer_score += 0.5

    print "Play again: Yes / No"
    choice = raw_input()
    if choice == "No":
        print "Final Scores"
        print "User =", user_score, "Computer =", computer_score
        if user_score > computer_score:
            print "You win the game !"
            break
        elif user_score < computer_score:
            print "You lost the game !"
            break
        else:
            print "The scores are tied !!!"
            print "Play a tie-breaker ?"
            second_choice = raw_input()
            if second_choice == "No!":
                break
            else:
                continue
    else:
        continue
