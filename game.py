import random

hand = {
	1 : "Rock",
	2 : "Paper",
	3 : "Scissors"
}
#AI hand
def computer_hand_item():
	c_hand_int = random.randint(1,3)
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
			return "You wins !!!"
	else:
		if u_hand_item == "Rock":
			return "You win !!!"
		elif u_hand_item == "Paper":
			return "Computer wins !!!"
		else:
			return "Tie !!!"

print "Choose: Rock", "Paper", "Scissors"


user_hand = raw_input()


computer_hand= computer_hand_item()
print "Computer's hand :", computer_hand
print judge(computer_hand,user_hand)
