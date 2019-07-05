# def lottery_ticket(n, m):
#     if n > 5 and m < 100:
#         return ("u won 100")
#
#     elif n > 100 and m < 201:
#         return "u won 200"
#     else:
#         return Falsee
#
# print(lottery_ticket(101,200 ))
import pytest


def lottery_ticket(n, m):
    if n > 5 and m <= 100:
        return "u won 100"
    elif n > 100 and m <= 200:
        return "u won 200"
    return False


#
# print(lottery_ticket(100, 200))
a = [6,55]

def test_lottery_ticket():
    check = lottery_ticket(*a)
    print(check)
    expected = False
    assert check == expected

test_lottery_ticket()

