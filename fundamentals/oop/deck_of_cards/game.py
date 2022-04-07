from classes.deck import Deck
from classes.player import Player

bicycle = Deck()
bicycle.show_cards()
p1 = Player('Ryan', bicycle)
p2 = Player('A Aron', bicycle)
bicycle.distributeCards(Player)

minCards = 0

while (p1.cardCount() != minCards) and (p2.cardCount() != minCards):
    Player.playround()
if p1.cardCount() == minCards:
    print(f"{p1.name} won the game")
else:
    print(f"{p2.name} won the game")

# bicycle.distributeCards(Player)
# for player in Player.players:
#     for card in player.hand:
#         print(f'{player.name} :: Card :: {card.card_info()}')

