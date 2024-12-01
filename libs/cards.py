"""Module for cards games.

Attributes
----------
Card
    Define the suit and rank of cards.
Deck : ABC
    Base class for storing cards.
CardStack : Cards
    Class that implements stack for storing cards.

"""

import itertools
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

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
        Suit range from 1 to 5
    rank : int, default JOKER_RANK
        Rank range from 2 to 15

    """

    suit: int = JOKER_SUIT
    rank: int = JOKER_RANK

    def __post_init__(self) -> None:
        """Validate the values of the suit and rank.

        Raises
        ------
        ValueError
            If the values of the suit and rank are out of range, raise it.

        """
        min_suit = min(SUIT_NAMES.keys())
        min_rank = min(RANK_CHARS.keys())
        if not min_suit <= self.suit <= JOKER_SUIT:
            msg = f'Suit range from {min_suit} to {JOKER_SUIT}: {self.suit}'
            raise ValueError(msg)
        if not min_rank <= self.rank <= JOKER_RANK:
            msg = f'Rank range from {min_rank} to {JOKER_RANK}: {self.rank}'
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
        """If the ranks are equal, return 'True'.

        Raises
        ------
        TypeError
            If the argument is not a 'Card' class, raise it.

        """
        if not isinstance(other, Card):
            msg = "Argument is not 'Card' class."
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
            msg = "Argument is not 'Card' class."
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
            msg = "Argument is not 'Card' class."
            raise TypeError(msg)
        return (
            self.suit > other.suit if self == other else self.rank > other.rank
        )

    def __str__(self) -> str:
        """Return the suit name initial and rank char.

        If the rank is an empty string, the card is joker. Then return 'JK'.

        Returns
        -------
        str
            Suit name initial and rank char

        """
        return self.suit_name[0] + self.rank_char if self.rank_char else 'JK'


class Deck(ABC):
    """Base class for storing cards."""

    @abstractmethod
    def push_card(self, card: Card) -> None:
        """Add a card to instance variables."""


class CardStack(Deck):
    """Class that implements stack for storing cards.

    Attributes
    ----------
    __card_stack : list[Card]
        Card stack

    """

    def __init__(self) -> None:  # noqa: D107
        self.__card_stack: list[Card] = []

    def push_card(self, card: Card) -> None:
        """Add a card to the card stack.

        Raises
        ------
        TypeError
            If the argument is not a 'Card' class, raise it.

        """
        if not isinstance(card, Card):
            msg = "Argument is not 'Card' class."
            raise TypeError(msg)
        self.__card_stack.append(card)

    def pop_card(self) -> Card | None:
        """Pop the last card in the card stack.

        If the card stack is empty, return 'None'.

        Returns
        -------
        Card | None
            Last card in the card stack

        """
        return self.__card_stack.pop() if self.__card_stack else None

    def __str__(self) -> str:  # noqa: D105
        return ','.join(map(str, self.__card_stack))


class JokerSet(Enum):  # noqa: D101
    includes: int = 1
    excludes: int = 2


def set_shuffled_cards(
    deck: Deck, joker_set: JokerSet = JokerSet.includes
) -> None:
    """Set shuffled cards into the card deck.

    Parameters
    ----------
    deck : Deck
        Base class for storing cards.
    joker_set : JokerSet, default JokerSet.includes
        Include or exclude the joker set.

    """
    min_suit = min(SUIT_NAMES.keys())
    max_suit = max(SUIT_NAMES.keys())
    min_rank = min(RANK_CHARS.keys())
    max_rank = max(RANK_CHARS.keys())
    cards = [
        Card(suit, rank)
        for suit, rank in itertools.product(
            range(min_suit, max_suit + 1), range(min_rank, max_rank + 1)
        )
    ]
    if joker_set == JokerSet.includes:
        cards.append(Card())
    random.shuffle(cards)
    for card in cards:
        deck.push_card(card)


if __name__ == '__main__':
    card_stack = CardStack()
    set_shuffled_cards(card_stack)
    cnt = 0
    card = card_stack.pop_card()
    while card:
        cnt += 1
        card = card_stack.pop_card()
    print(cnt)
