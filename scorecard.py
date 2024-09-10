"""
This code contains common errors that can be detected
by static type checking -- if the type is known!
Please do not fix this code by inspection.

Instead, add type hints and watch your IDE (or mypy) find errors.

Add these hints ONE AT A TIME.  SAVE the file after each one and run mypy.
Observe how the type hint helps it perform static checking.

1) add type to parameter:                `add_score(self, score: float)`
    scorecard.add_score(score) => "add_score" of "Scorecard" has incompatible type "str"; expected "float"

2) add type to return value of average:  `average(self) -> ???`
    "The average is " + scorecard.average() => Unsupported operand types for + ("str" and "float")

3) add type to self.scores attribute:    `self.scores: ???[???] = []`
4) add type hints for all parameters and return values.
   If a function does not return a value, don't write a type hint.
5) add type to the `suffixes` variable in `ordinal()` function. 
   Include the type of keys and values.

"""
from typing import List


class Scorecard:
    """Accumulate scores and compute their average."""

    def __init__(self):
        """Iniiialize a new Scorecard."""
        self.scores: List[float] = []

    def add_score(self, score: float):
        """Add a score to the Scorecard."""
        self.scores.append(score)

    def average(self) -> float:
        """Return the average of all scores, 0 if no scores."""
        return sum(self.scores)/max(1,len(self.scores))


def print_scores(score_card):
    """Print statistics for the scorecard and the actual scores."""

    # What changes to Scorecard are needed in order to make this code work?
    print(f"Scorecard contains {len(score_card)} scores.")
    print(f"Min score: {min(score_card)}  Max score: {max(score_card)}.")
    # What change to Scorecard is needed to make this work?
    for score in score_card:
        print(score)


def ordinal(num):
    """Return the ordinal value of an integer; works for numbers up to 20.

    For examples: ordinal(1) is '1st', ordinal(2) is '2nd'.
    """
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    return str(num) + suffixes.get(num, "th")


if __name__ == "__main__":
    # Interactively add scores and print some statistics.
    scorecard = Scorecard()

    print("Input 3 scores.")
    for count in range(1,4):
        score = input(f"input {ordinal(count)} score: ")
        scorecard.add_score(score)

    print("The average is " + scorecard.average())

    print_scores(scorecard)
