"""Module for cards games.

Attributes
----------
Card
    Define the suit and rank of cards.

"""

import itertools
import random
from dataclasses import dataclass

SUIT_NAMES: dict[int, str] = {
    1: 'club',
    2: 'diamond',
    3: 'heart',
    4: 'spade',
}
JOKER_SUIT: int = 5

RANK_CHARS: dict[int, str] = {n: str(n) for n in range(2, 10)}
RANK_CHARS.update(
    {
        10: 'T',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
    }
)
JOKER_RANK: int = 15


@dataclass(frozen=True)
class Card:
    """Define the suit and rank.

    Attributes
    ----------
    suit : int, default JOKER_SUIT
        Suit values range from 1 to 5.
    rank : int, default JOKER_RANK
        Rank values range from 2 to 15.

    """

    suit: int = JOKER_SUIT
    rank: int = JOKER_RANK

    def __post_init__(self) -> None:
        """Validate the values of suit and rank."""
        min_suit = min(SUIT_NAMES.keys())
        min_rank = min(RANK_CHARS.keys())
        if not min_suit <= self.suit <= JOKER_SUIT:
            msg = (
                f'Suit values range from {min_suit} to {JOKER_SUIT}:',
                self.suit,
            )
            raise ValueError(msg)
        if not min_rank <= self.rank <= JOKER_RANK:
            msg = (
                f'Rank values range from {min_rank} to {JOKER_RANK}:',
                self.rank,
            )
            raise ValueError(msg)

    @property
    def suit_name(self) -> str:
        """Return the suit name.

        'JOKER_SUIT' not in 'SUIT_NAMES'. If the suit is 'JOKER_SUIT', return
        'joker'.

        Returns
        -------
        str
            Suit name

        """
        return SUIT_NAMES.get(self.suit, 'joker')

    @property
    def rank_char(self) -> str:
        """Return the rank char.

        'JOKER_RANK' not in 'RANK_CHARS'. If the rank is 'JOKER_RANK', return
        an empty string.

        Returns
        -------
        str
            Rank char

        """
        return RANK_CHARS.get(self.rank, '')

    def __eq__(self, other: object) -> bool:
        """If the ranks are equal, return true.

        Raises
        ------
        TypeError
            If the argument is not a 'Card' class, raise it.

        """
        if not isinstance(other, Card):
            msg = "The argument is not a 'Card' class."
            raise TypeError(msg)
        return self.rank == other.rank

    def __lt__(self, other: object) -> bool:
        """Compare the ranks.

        If the ranks are equal, compare the suits.

        Raises
        ------
        TypeError
            If the argument is not a 'Card' class, raise it.

        """
        if not isinstance(other, Card):
            msg = "The argument is not a 'Card' class."
            raise TypeError(msg)
        return (
            self.suit < other.suit if self == other else self.rank < other.rank
        )

    def __gt__(self, other: object) -> bool:
        """Compare the ranks.

        If the ranks are equal, compare the suits.

        Raises
        ------
        TypeError
            If the argument is not a 'Card' class, raise it.

        """
        if not isinstance(other, Card):
            msg = "The argument is not a 'Card' class."
            raise TypeError(msg)
        return (
            self.suit > other.suit if self == other else self.rank > other.rank
        )

    def __str__(self) -> str:
        """Return the suit name initial and rank char.

        If the rank is an empty string, the card is a joker. Then return 'JK'.

        Returns
        -------
        str
            Suit name initial and rank char

        """
        return self.suit_name[0] + self.rank_char if self.rank_char else 'JK'


# TODO: Define an abstract class named 'CardHolder'.
class CardDeck:
    """カードを生成し、カードの保持と取り出しを行う。

    Attributes
    ----------
    __cards : list[Card]
        カードデッキ

    """

    def __init__(self, *, joker_includes: bool = True) -> None:
        """カードを生成する。

        Parameters
        ----------
        joker_includes : bool
            True: Jokerを生成する, False: Jokerを生成しない, by default True

        """
        suit_iter: range = range(
            min(SUIT_NAMES.keys()), max(SUIT_NAMES.keys()) + 1
        )
        rank_iter: range = range(
            min(RANK_CHARS.keys()), max(RANK_CHARS.keys()) + 1
        )
        cards: list[Card] = [
            Card(suit, rank)
            for suit, rank in itertools.product(suit_iter, rank_iter)
        ]
        if joker_includes:
            cards.append(Card())
        random.shuffle(cards)

        self.__cards: list[Card] = cards

    def __str__(self) -> str:
        """カードをカンマで結合する。"""
        return ','.join(map(str, self.__cards))

    def card_exists(self) -> bool:
        """カードの有無を判定する。"""
        return self.__cards != []

    def pop_card(self) -> Card:
        """カードデッキからカードを取り出す。"""
        return self.__cards.pop()


if __name__ == '__main__':
    print('Generating a new card deck.')
    card_deck: CardDeck = CardDeck()
    print(card_deck)
    print('(in card deck)')

    print('Take out the 1st card.')
    card_1: Card = card_deck.pop_card()
    print(card_deck)
    print('(in card deck)')

    print('Take out the 2nd card and compare two cards.')
    card_2: Card = card_deck.pop_card()
    print(card_1, '(1st card)')
    print(card_2, '(2nd card)')
    print(card_1, '=', card_2, '->', card_1 == card_2)
    print(card_1, '<', card_2, '->', card_1 < card_2)
    print(card_1, '>', card_2, '->', card_1 > card_2)

    print('Take out the last card.')
    while card_deck.card_exists():
        card_deck.pop_card()
    print(card_deck)
    print('(in card deck)')

    print('Generating a new card deck without Joker.')
    card_deck = CardDeck(joker_includes=False)
    print(card_deck)
    print('(in card deck)')
    print('in Joker ->', 'JK' in str(card_deck))
