"""
カードモジュール

Classes
-------
Card
    スートとランクを保持する。
CardDeck
    カードを生成し、カードの保持と取り出しを行う。

"""

import itertools
import random
from dataclasses import dataclass

# スートの名称
SUIT_NAMES: dict[int, str] = {1: "club", 2: "diamond", 3: "heart", 4: "spade"}
JOKER_SUIT: int = 5

# ランクの表記
RANK_CHARS: dict[int, str] = {rank: str(rank) for rank in range(2, 10)}
RANK_CHARS.update({10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"})
JOKER_RANK: int = 15


@dataclass(frozen=True)
class Card:
    """
    スートとランクを保持する。

    Attributes
    ----------
    suit : int
        1 to 5, by default JOKER_SUIT = 5
    rank : int
        2 to 15, by default JOKER_RANK = 15

    """

    suit: int = JOKER_SUIT
    rank: int = JOKER_RANK

    def __post_init__(self) -> None:
        """
        バリデーション

        Raises
        ------
        CardValueError
            スートの値が1以上5以下ではない場合
        CardValueError
            ランクの値が2以上15以下ではない場合

        """
        if not (min(SUIT_NAMES.keys()) <= self.suit <= JOKER_SUIT):
            raise CardValueError(msg="Suit value is out of range.")
        if not (min(RANK_CHARS.keys()) <= self.rank <= JOKER_RANK):
            raise CardValueError(msg="Rank value is out of range.")

    @property
    def suit_name(self) -> str:
        """スートの名称"""
        return SUIT_NAMES.get(self.suit, "joker")

    @property
    def rank_char(self) -> str:
        """ランクの表記"""
        return RANK_CHARS.get(self.rank, "")

    def __str__(self) -> str:
        """
        スートの名称の頭文字とランクの表記を結合する。

        Returns
        -------
        str
            Jokerの場合には、"JK"を返す。

        """
        return self.suit_name[0] + self.rank_char if self.rank_char else "JK"

    def __eq__(self, other: object) -> bool:
        """
        ランクが等しい場合に同値とする。

        Raises
        ------
        CardTypeError
            比較対象がCardクラス、またはCardの派生クラスではない場合

        """
        if not isinstance(other, Card):
            raise CardTypeError(msg="Argument is not a Card class.")
        return self.rank == other.rank

    def __lt__(self, other: object) -> bool:
        """
        ランクが等しい場合には、スートの大小を比較する。

        Raises
        ------
        CardTypeError
            比較対象がCardクラス、またはCardの派生クラスではない場合

        """
        if not isinstance(other, Card):
            raise CardTypeError(msg="Argument is not a Card class.")
        return self.suit < other.suit if self == other else self.rank < other.rank

    def __gt__(self, other: object) -> bool:
        """
        ランクが等しい場合には、スートの大小を比較する。

        Raises
        ------
        CardTypeError
            比較対象がCardクラス、またはCardの派生クラスではない場合

        """
        if not isinstance(other, Card):
            raise CardTypeError(msg="Argument is not a Card class.")
        return self.suit > other.suit if self == other else self.rank > other.rank


class CardValueError(ValueError):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class CardTypeError(TypeError):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class CardDeck:
    """
    カードを生成し、カードの保持と取り出しを行う。

    Attributes
    ----------
    __cards : list[Card]
        カードデッキ

    """

    def __init__(self, *, joker_includes: bool = True) -> None:
        """
        カードを生成する。

        Parameters
        ----------
        joker_includes : bool
            True: Jokerを生成する, False: Jokerを生成しない, by default True

        """
        suit_iter: range = range(min(SUIT_NAMES.keys()), max(SUIT_NAMES.keys()) + 1)
        rank_iter: range = range(min(RANK_CHARS.keys()), max(RANK_CHARS.keys()) + 1)
        cards: list[Card] = [Card(suit, rank) for suit, rank in itertools.product(suit_iter, rank_iter)]
        if joker_includes:
            cards.append(Card())
        random.shuffle(cards)

        self.__cards: list[Card] = cards

    def __str__(self) -> str:
        """カードをカンマで結合する。"""
        return ",".join(map(str, self.__cards))

    def card_exists(self) -> bool:
        """カードの有無を判定する。"""
        return self.__cards != []

    def pop_card(self) -> Card:
        """カードデッキからカードを取り出す。"""
        return self.__cards.pop()


if __name__ == "__main__":
    print("Generating a new card deck.")
    card_deck: CardDeck = CardDeck()
    print(card_deck)
    print("(in card deck)")

    print("Take out the 1st card.")
    card_1: Card = card_deck.pop_card()
    print(card_deck)
    print("(in card deck)")

    print("Take out the 2nd card and compare two cards.")
    card_2: Card = card_deck.pop_card()
    print(card_1, "(1st card)")
    print(card_2, "(2nd card)")
    print(card_1, "=", card_2, "->", card_1 == card_2)
    print(card_1, "<", card_2, "->", card_1 < card_2)
    print(card_1, ">", card_2, "->", card_1 > card_2)

    print("Take out the last card.")
    while card_deck.card_exists():
        card_deck.pop_card()
    print(card_deck)
    print("(in card deck)")

    print("Generating a new card deck without Joker.")
    card_deck = CardDeck(joker_includes=False)
    print(card_deck)
    print("(in card deck)")
    print("in Joker ->", "JK" in str(card_deck))
