class Player:

    def __init__(self,name,role="Neutral",hand=[]):
        self.name = name
        self.role = role
        self.hand = hand

    #def data_player(self):

     #   self.name = name 

    def get_data(self):

        print(f"Welcome {self.name}! You were added to the list\nYour role in this game is: {self.role}")

    def add_card(self,card):

        self.hand.append(card)

    def role_assignment(self,assigned_role):

        self.role = assigned_role


