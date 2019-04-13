import random
# random module for shuffle

# Global variables (tuple & dictionary)
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

# Boolean value to control while loops
playing = True

# Classes
# Card: a suit and a rank
# Deck: 52 cards (shuffled)
# Hand: player


class Card:

    def __init__(self,suit,rank):
        # Basic attributes
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # dunder(magic) method (print, string method runs for the Card class)
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = [] # empty list to start with
        for suit in suits: # iterate every element in suits array(tuple)
            for rank in ranks: # nested for loop (iteration)
                self.deck.append(Card(suit,rank)) # build deck array (list) with Card object (fed with suit, rank)

    def __str__(self):
        deck_comp = '' # empty string to start with
        for card in self.deck: # iterate every element in deck array (list)
            deck_comp += '\n ' +card.__str__() # add each card object's "string" in each new line
        return 'The deck has: ' + deck_comp

    def shuffle(self): # self = Deck, shuffle applies to Deck
        random.shuffle(self.deck) # shuffle deck using random module's shuffle()

    def deal(self):
        single_card = self.deck.pop() # pop one card from deck
        return single_card # return 'single_card' to a method to call deal()


class Hand:
    # hold cards from deck, calculate values, determine the ace's value
    def __init__(self):
        self.cards = [] # empty hand
        self.value = 0 # also empty value to start with
        self.aces = 0 # ace attribute to use later

    def add_card(self,card): # card (from Card class)
        self.cards.append(card) # build the list of cards in hand
        self.value += values[card.rank] # add values per added cards (dictionary list)
        if card.rank == 'Ace': # if ace card
            self.aces += 1 # number of ace card increase

    def adjust_for_ace(self):
        while self.value > 21 and self.aces: # self.value > 21 and ace card is in hand
            self.value -= 10 # minus 10 from total (with ace value adjusted to 1)
            self.aces -= 1 # take one ace card out of cards in hand (e.g. if two aces, 1st ace value = 1, 2nd ace value = 11)


class Chips:
    # track of chips
    def __init__(self):
        self.total = 100 # default chip 100
        self.bet = 0 # prepare to bet

    def win_bet(self):
        self.total += self.bet # add the erned bet to total chips

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips): # chips (from Chips class)
    # check the player's bet against available chips
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break # confirmed legitimate chips.bet


def hit(deck,hand): # access class deck and hand

    hand.add_card(deck.deal()) # popped single card added hand.cards [] list
    hand.adjust_for_ace() # adjust for ace if the added card is ace

def hit_or_stand(deck,hand):
    global playing

    while True: # while playing = True
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand) # run the hit() defined above
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False # dealer's turn
        else:
            print("Sorry, please try again.")
            continue # go back to while loop
        break # end while loop


def show_some(player,dealer): # player, dealer (required parameters) <= 'player_hand, dealer_hand' passed in as args
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ') # * is used to print every item in a collection, and sep='\n' arg to print each item on a separate line

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# functions to handle end of game scenarios
def player_busts(player,dealer,chips): # important to pass player's hand, dealer's hand and player's chips
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push")


# Main game codes

while True:
    # opening statement
    print('Welcome to BlakJack! Get as close to 21 as you can without going over! \n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Instantiate deck and shuffle
    deck = Deck()
    deck.shuffle()

    # Player and Dealer cards setup
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal()) # for two pairs of cards

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Setup player's chips
    player_chips = Chips()

    # Take player's bet
    take_bet(player_chips)

    # Show cards of player and dealer
    show_some(player_hand,dealer_hand)

    while playing: # while global variable 'playing' = True

        # prompt for player to hit or stand
        hit_or_stand(deck,player_hand)

        # show cards
        show_some(player_hand,dealer_hand)

        # if player's hand exceeds 21, player_busts()
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break # exit 'while playing'

    # if player hasn't busted
    if player_hand.value <= 21: # (verify) this 'if' position, can be 'elif' in the same line as the preceding if?

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            # show all cards
            show_all(player_hand,dealer_hand)

            # run different wining scenairos
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)

    # all cases handled -> proceed to the below logic

    # show player's chips total
    print("\nPlayer's winnings stand at",player_chips.total)

    # ask to play again
    new_game = input("Would you like to play another game? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue # go to the root while loop
    else:
        print("Thanks for playing!")
        break # exit the while loop (game exit)