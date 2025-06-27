import pytest

# --- Functions under test ---
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

# --- Test: Parameterized cases for correct output ---
@pytest.mark.parametrize("func, input_val, expected", [
    (square, 2, 4),
    (square, -3, 9),
    (cube, 3, 27),
    (cube, -2, -8),
    (fifth_power, 2, 32),
    (fifth_power, -1, -1),
    (square, 0, 0),
    (cube, 0, 0),
    (fifth_power, 0, 0),
    (square, 1_000, 1_000_000),         # large input
])
def test_power_calculations(func, input_val, expected):
    assert func(input_val) == expected

# --- Test: Float inputs (Type flexibility) ---
@pytest.mark.parametrize("func", [square, cube, fifth_power])
def test_with_float_input(func):
    result = func(2.0)
    assert isinstance(result, float)
    assert round(result) == func(2)    # Same output as integer

# --- Test: Invalid inputs ---
@pytest.mark.parametrize("invalid_input", ["string", None, [2], {"n": 2}])
@pytest.mark.parametrize("func", [square, cube, fifth_power])
def test_invalid_inputs(func, invalid_input):
    with pytest.raises(TypeError):
        func(invalid_input)

# --- Test: Output types ---
@pytest.mark.parametrize("func", [square, cube, fifth_power])
def test_output_type(func):
    assert isinstance(func(4), int)

# --- Edge case: Negative powers (should still be valid mathematically) ---
def test_fifth_power_negative():
    assert fifth_power(-2) == -32
