from typing import Union


def fizz_buzz(x: int) -> Union[int, str]:
    try:
        assert isinstance(x, int)
    except Exception as error:
        raise error

    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


