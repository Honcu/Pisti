import random

class Cards:
    def __init__(self):
        self.pack = []
        kinds = ["clubs", "diamonds", "hearts", "spades"]
        for kind in kinds:
            for num in range(1, 14):
                self.pack.append([num, kind])

    def get_cards(self):
        return self.pack

    # returns random card from pack and removes the card from pack
    def rand_card(self):
        high = len(self.pack) - 1
        rnum = random.randint(0, high)
        card = self.pack[rnum]
        del self.pack[rnum]
        return card

    # creates a list of 4 random cards from pack and removes the cards from pack
    def fill4(self):
        hand = []
        for num in range(0, 4):
            hand.append(Cards.rand_card(self))
        return hand

class Computer:
    def __init__(self, hand):
        self.hand = hand

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def get_hand_values(self):
        hand_values = []
        for i in range(0, 4):
            hand_values.append(self.hand[i][0])
        return hand_values

    def decision(self, middle):
        card = []

        # if there is no card in the middle
        if len(middle) == 0:
            index = 4
            comp_hand_nums = self.get_hand_values()

            # to avoid picking an 11 value card when middle is empty
            # sets card value as 11 and checks if there is any other choice
            card = [11, "Null"]
            check = any(item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13] for item in comp_hand_nums)
            if check:
                while card[0] == 11:
                    if self.hand[0][0] != 0 and self.hand[0][0] != 11:
                        card = self.hand[0]
                        index = 0
                    elif self.hand[1][0] != 0 and self.hand[1][0] != 11:
                        card = self.hand[1]
                        index = 1
                    elif self.hand[2][0] != 0 and self.hand[2][0] != 11:
                        card = self.hand[2]
                        index = 2
                    elif self.hand[3][0] != 0 and self.hand[3][0] != 11:
                        card = self.hand[3]
                        index = 3
                self.hand[index] = [0, "Null"]

            else:
                if self.hand[0][0] != 0:
                    card = self.hand[0]
                    index = 0
                elif self.hand[1][0] != 0:
                    card = self.hand[1]
                    index = 1
                elif self.hand[2][0] != 0:
                    card = self.hand[2]
                    index = 2
                elif self.hand[3][0] != 0:
                    card = self.hand[3]
                    index = 3
                self.hand[index] = [0, "Null"]

        # if there is at least one card in the middle
        else:
            # gets the num of top card on the middle
            top_card_num = middle[-1][0]

            # creates a list of the nums in comp hand
            comp_hand_nums = self.get_hand_values()

            # if top card value can be matched from on hand cards
            if top_card_num in comp_hand_nums:
                card = self.hand[comp_hand_nums.index(top_card_num)]
                self.hand[comp_hand_nums.index(top_card_num)] = [0, "Null"]

            # picks a random card
            else:
                if self.hand[0][0] != 0:
                    card = self.hand[0]
                    self.hand[0] = [0, "Null"]
                elif self.hand[1][0] != 0:
                    card = self.hand[1]
                    self.hand[1] = [0, "Null"]
                elif self.hand[2][0] != 0:
                    card = self.hand[2]
                    self.hand[2] = [0, "Null"]
                elif self.hand[3][0] != 0:
                    card = self.hand[3]
                    self.hand[3] = [0, "Null"]

        return card
