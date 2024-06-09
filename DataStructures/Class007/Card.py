from CardColor import CardColor


class Card:
    def __init__(self, color, number):
        if isinstance(color, CardColor):
            self.color = color
            self.number = number

        else:
            raise TypeError("Color must be an instance of CardColor")

    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.color, self.number) == (other.color, other.number)

    def __repr__(self):
        return f"[{self.color}, {self.number}]"
