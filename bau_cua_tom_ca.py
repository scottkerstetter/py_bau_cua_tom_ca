import random

class player:
    """ Instance this class to represent each player who is able to make bets. """
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
    
    def make_bet(self, choices):
        """ Prompt user for bet at strings and integers and return bet amount."""
        # get player's choice to bet on
        while True:
            self.betChoice = input("Bet on a space: ").upper()
            if self.betChoice in choices:
                break
            else:
                print("Invalid choice.")
        # get integer amount that player is betting
        while True:
            self.betAmount = get_int("Bet amount: ")
            if self.money - self.betAmount >= 0:
                self.money -= self.betAmount # remove bet from player's total money.
                break
            else:
                print("Cannot bet more money than you have.")
        return self.betAmount

class dice:
    """ Instance this class to represent a set of three dice. """
    def __init__(self) -> None:
        self.sides = {"GOURD":0, "CRAB":0, "SHRIMP":0, "FISH":0, "DEER":0, "ROOSTER":0}
        self.numDice = 3

    def roll(self):
        """ Randomizer that simulates rolling three six-sided dice. """
        rolls = []
        # get random key for each di
        for i in range(self.numDice):
            rolls.append(random.choice(list(self.sides.keys())))
        # count roll results
        for r in rolls:
            self.sides[r] += 1
        return self.sides

class engine:
    def __init__(self, numPlayers) -> None:
        self.numPlayers = numPlayers

    def setup(self) -> None:
        # get currency
        self.currency = input("Enter currency: ")
        # get player names and money (must be positive and not zero)
        self.players = []
        for i in range(self.numPlayers):
            playerName = input("\nEnter your name: ")
            playerMoney = get_int("Enter starting money: ")
            self.players.append(player(playerName, playerMoney))
            
        # set bank balance to negative sum of player money
        self.bank = sum(-p.money for p in self.players)

        # initialize dice set
        self.diceSet = dice()

        # get list of choices to bet on
        self.choiceList = list(self.diceSet.sides.keys())

    def check_balance(self) -> None:
        """ Check that sum of  bank money and sum of player money equals zero to ensure good math. If not, quit."""
        self.playerSum = sum(p.money for p in self.players)
        if self.playerSum + self.bank != 0:
            raise ValueError(f"Bank {self.bank} plus sum of player money {self.playerSum} must equal zero.")
        
    def display_status(self) -> None:
        print("\n**********")
        for p in self.players:
            print(f"{p.name} has {p.money} {self.currency}")
        print("**********")

    def play_round(self) -> None:
        # initialize dice set
        diceSet = dice()
        
        # get player bets
        print("\nPlacing bets...")
        for p in self.players:
            print(f"\n{p.name}'s turn")
            self.bank += p.make_bet(self.choiceList)
        
        # roll dice
        print("\nRolling dice...")
        self.rollResults = self.diceSet.roll()
        print("\nRoll results...")
        print(self.rollResults)
        
        # pay winners
        for p in self.players:
            if self.rollResults[p.betChoice] == 0:
                print(f"{p.name} lost {p.betAmount} {self.currency}.")
            else:
                winnings = p.betAmount * (1 + self.rollResults[p.betChoice])
                p.money += winnings
                self.bank -= winnings
                print(f"{p.name} won {winnings} {self.currency}!")
                print(self.bank)
        
        # check balance
        self.check_balance()

        # reset results for next round
        for key in self.rollResults:
            self.rollResults[key] = 0

    def exit_or_continue(self):
        # prompt user for whether or not to play another round
        while True:
            answer = input("\nPlay another round? Enter YES or NO: ").upper()
            if answer == "YES":
                return True
            elif answer == "NO":
                return False
            else:
                print("Answer must be either YES or NO.")


def get_int(text) -> int:
    while True:
        inputInt = input(text)
        try:
            inputInt = int(inputInt)
            if inputInt > 0:
                return inputInt
            else:
                print("Invalid input: number must be positive and not zero.")
        except:
            print("Invalid input: must enter a whole number.")

def main():
    # get number of players and initialize engine
    n = get_int("Enter number of players: ")
    game = engine(n)
    
    # get player names and starting money
    game.setup()

    keepPlaying = True
    while keepPlaying:
        game.display_status()
        game.play_round()
        keepPlaying = game.exit_or_continue()
    
    print("\nThank you for playing! Happy Lunar New Year!")
    quit()

if __name__ == "__main__":
    main()