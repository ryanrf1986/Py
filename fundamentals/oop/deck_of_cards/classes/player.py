from .deck import Deck
from .card import Card
import random

class Player:
    players = []
    deck = None
    round = 1
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.pile = []
        Player.deck = Deck
        Player.players.append(self)

    def drawCard(self):
        self.hand.insert(0,Player.deck.giveCardcard())
        return self

    def addCardPile(self, card: Card) -> None:
        if type(card) is list:
            self.pile.extend(card)
        else:
            self.pile.append(card)
        
    def addCardHand(self, card)-> None:
        if type(card) is list:
            self.hand.extend(card)
        else:
            self.hand.append(card)

    def playCard( self) -> Card:
        return self.hand.pop()
    
    def cardCount(self):
        h = len(self.hand)
        p = len(self.pile)
        r= h + p
        return r

    
    def ensureFullHand(self):
        if not self.hand:
            self.shuffle()
            self.pileToHand()

    def shuffle(self):
        random.shuffle(self.pile)
        
    def pileToHand(self):
        while self.pile:
            self. addCardHand(self.pile.pop())
        
    @classmethod
    
    def playRound(cls):
        pl1 = cls.players[0]
        pl2 = cls.players[1]
        if pl1.cardCount() == 0 or pl2.cardCount() == 0:
            return
        # print(f'\nRound ::{cls.round}')
        # print(f'"player 1 hand: {len(pl1.hand)}')
        # print(f'"player 1 pile: {len(pl1.pile)}')
        # print(f'"player 2 hand: {len(pl2.hand)}')
        # print(f'"player 2 pile: {len(pl2.pile)}')
        pl1.ensureFullHand()
        pl2.ensureFullHand()
        pl1CardList = [pl1.playCard()]
        pl2CardList = [pl2.playCard()]
        Player.war(pl1, pl2, pl1CardList, pl2CardList)
        cls.war(pl1, pl2, pl1CardList, pl2CardList)
        cls.round += 1
        
    @staticmethod

    def war(pl1, pl2, pl1CardList, pl2CardList):
        print(f'{pl1.name} played {pl1CardList[-1].getstring()}')
        print(f'{pl2.name} played {pl2CardList[-1].getstring()}')
        if pl1CardList[-1].getPointVal() > pl2CardList[-1].getPointVal():
            # player 1 wins
            pl1.addCardPile(pl1CardList)
            pl1.addCardPile(pl2CardList)
        elif pl1CardList[-1].getPointVal() < pl2CardList[-1].getPointVal():
        # player 2 wins
            pl2.addCardPile(pl1CardList)
            pl2.addCardPile(pl2CardList)
        else:
            for x in range(2):
                if pl1.cardCount() == 0 or pl2.cardCount() ==0:
                    return
                pl1.ensureFullHand()
                pl2.ensureFullHand()
                pl1CardList.append(pl1.playCard())
                pl2CardList.append(pl2.playCard())
            Player.war(pl1, pl2, pl1CardList, pl2CardList)
        return