import itertools
import math
from collections import namedtuple, defaultdict
from random import randint
from typing import List

__author__ = 'Mice Pápai'
__copyright__ = 'Copyright 2017, Mice Pápai'
__credits__ = ['Mice Pápai <mice@gorbekor.hu>']
__license__ = 'Apache-2.0'
__version__ = '1.0.2'


EloPlayer = namedtuple('EloPlayer', 'place elo')


def calc_s(player1, player2):
    if player1.place < player2.place:
        return 1.0
    if player1.place == player2.place:
        return 0.5
    return 0.0


def calc_ea(player1, player2):
    return 1 / (1.0 + math.pow(10.0, (player2.elo - player1.elo) / 400.0))


def calc_elo_change(player1, player2, k):
    s = calc_s(player1, player2)
    ea = calc_ea(player1, player2)
    return round(k * (s - ea))


def calc_new_elos(players: List[EloPlayer], k=32):
    n = len(players)

    player_to_player = list(itertools.permutations(range(n), 2))

    elo_changes = defaultdict(int)
    for i, j in player_to_player:
        elo_changes[i] += calc_elo_change(players[i], players[j], k)

    return [players[i].elo + elo_changes[i] for i in range(n)]


def main():
    # generate random players
    elo_players = [EloPlayer(place=place, elo=randint(1200, 1800))
                   for place in range(1, 5)]

    print('Original ELO scores:')
    for place, player in enumerate(elo_players, start=1):
        print(f'{place}: {player.elo}')

    # set the K factor
    k_factor = 16

    # calculate new ELO scores
    new_elos = calc_new_elos(elo_players, k_factor)

    print('\nNew ELO scores:')
    for place, new_elo in enumerate(new_elos, start=1):
        print(f'{place}: {new_elo}')


if __name__ == '__main__':
    main()
