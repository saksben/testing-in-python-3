import approvaltests

import scorer
from scorer import get_score, IceCream, get_score_with_weather


def print_get_score(args, result):
    return f"{args} => {result}\n"


def test_get_score_with_weather():
    weathers = [True, False]
    flavours = [IceCream.Strawberry, IceCream.Chocolate, IceCream.Vanilla, None]
    approvaltests.verify_all_combinations(
        get_score_with_weather,
        [
            weathers,
            flavours,
        ],
        formatter=print_get_score
    )

