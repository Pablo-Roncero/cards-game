class Player:

    def __init__(self,name,rol="Neutral"):
        self.name = name
        self.rol = rol


    def get_Data(self):

        print(f"Welcome {self.name}! You were added to the list\nYour role in this game is: {self.rol}")


    # def rol_assignment(self,):
    #    pass
