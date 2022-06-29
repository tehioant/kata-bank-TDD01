import pytest

from fizzbuzzapp.main import fizz_buzz


class TestFizzBuzz:
    def test_raise_exception_when_input_is_not_an_integer(self):
        # Given
        x = "error"
        # When-Then
        with pytest.raises(AssertionError):
            fizz_buzz(x)

    def test_return_input_when_it_is_not_a_multiple_of_3_and_5_and_15(self):
        # Given
        x = 1
        # When-Then
        assert fizz_buzz(x) == x

    def test_return_fizz_when_input_is_a_multiple_of_3(self):
        # Given
        x = 3
        # Then
        assert fizz_buzz(x) == "Fizz"

    def test_return_buzz_when_input_is_a_multiple_of_5(self):
        # Given
        x = 5
        # Then
        assert fizz_buzz(x) == "Buzz"

    def test_return_fizzbuzz_when_input_is_a_multiple_of_15(self):
        # Given
        x = 15
        # Then
        assert fizz_buzz(x) == "FizzBuzz"

    @pytest.mark.parametrize("x, output", [(9, "Fizz"), (10, "Buzz"), (30, "FizzBuzz"), (19, 19)])
    def test_return_fizzbuzz_with_several_inputs(self, x, output):
        # Then
        assert fizz_buzz(x) == output
