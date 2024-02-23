# Bầu Cua Tôm Cá: A Lunar New Year Game
## Background
This is a python-based version of a Vietnamese gambling game, [Bầu Cua Tôm Cá](https://en.wikipedia.org/wiki/Bầu_cua_cá_c%E1%BB%8Dp), that can be played in the command-line. The game is played during Vietnamese Lunar New Year celebrations known as [Tết](https://en.wikipedia.org/wiki/Tết).

## Rules
The game is played with three six-sided dice and board or mat with six spaces. Each space on the board has one of six characters: gourd, crab, shrimp, fish, deer or rooster. On each di, each face also shows one of these characters. The objective of the game is to win money by betting on which space's character will be rolled by the dice.<br/>
The game is played in rounds for as long as players have money or want to keep playing. In each round the following steps take place:
1. Each player makes a bet by placing any amount of money on a space. More than one player can bet on a single space.
2. A dealer rolls all three dice together. The face-up side of each di determines the winning spaces for the round. If a space's character is not rolled, then that spaces loses the round.
3. The dealer collects money from losing spaces and pays the players that bet on winning spaces.
### Scoring
When a space wins, the amount that a player wins is equal to their bet plus their bet times the number of dice that match their space. If one di shows the winning space, then each player on the winning space gets to keep their bet and is payed 1x their bet amount by the dealer. The winnings are not divided among players; each player get paid based on how much they individually bet. If two dice show same winning space, then the winners get their money back and are paid 2x their bet amount by the dealer. If all three dice show the same winning space, then the winners keep their bet and are paid 3x their bet amount.

### Example


A dealer, who runs the game, rolls all three dice

<br/><br/>
picture of dice
picture of board

# References
[wiki](https://en.wikipedia.org/wiki/Bầu_cua_cá_c%E1%BB%8Dp)
