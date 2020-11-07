import random


class Card:

    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        suits = ("Hearts","Diamonds","Spades","Clubs")
        ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King", "Ace")
        values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12,
         "King":13, "Ace":14}

        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank,values[rank])
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards) # random.shuffle does not return nothing. It shuffles the list yet created
        
    def deal_one(self):
        
        return self.all_cards.pop()

my_card = Deck()

for card in my_card.all_cards:
    print(card)