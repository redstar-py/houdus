houdus

A lightweight, zero-dependency Python package for generating random numbers and sequences with a clean, intuitive API.

Features

🎲 Easy Random Number Generation - Generate random integers and floats with simple function calls

🔢 Unique Number Sequences - Generate lists of unique random numbers within a range

📊 Number Ranges - Create sequences of numbers with custom steps

🔐 Deterministic Results - Set seeds for reproducible random number generation

🚀 Zero Dependencies - Pure Python implementation with no external requirements

💡 Type Hints - Full type annotations for better IDE support and type checking

📦 Lightweight - Minimal package size and memory footprint

Installation

Via pip (from PyPI)

pip install houdus


From Source

git clone [https://github.com/yourusername/houdus.git](https://github.com/yourusername/houdus.git)
cd houdus
pip install .


Development Installation

git clone [https://github.com/yourusername/houdus.git](https://github.com/yourusername/houdus.git)
cd houdus
pip install -e ".[dev]"


Quick Start

from houdus import pick_int, pick_float, step_sequence, distinct_ints, assign_seed

# Generate a random integer between 1 and 100 (inclusive)
print(pick_int(1, 100))  # Output: 42 (example)

# Generate a random float between 0 and 1
print(pick_float(0.0, 1.0))  # Output: 0.8739... (example)

# Generate a list of 5 unique numbers between 1 and 50
print(distinct_ints(5, 1, 50))  # Output: [3, 15, 42, 28, 7] (example)

# Generate a sequence of numbers from 1 to 10 with step 2
print(step_sequence(1, 11, 2))  # Output: [1, 3, 5, 7, 9]

# Set a seed for deterministic/reproducible results
assign_seed(42)
print(pick_int(1, 100))  # Always outputs the same number
assign_seed(42)
print(pick_int(1, 100))  # Outputs the same number again


API Reference

pick_int(min_val: int, max_val: int) -> int

Generate a random integer between min_val and max_val (inclusive).

Parameters:

min_val (int): Minimum value (inclusive)

max_val (int): Maximum value (inclusive)

Returns: int - A random integer within the specified range

Raises: ValueError - If min_val > max_val

Example:

from houdus import pick_int

die_roll = pick_int(1, 6)  # Simulates rolling a die


pick_float(min_val: float, max_val: float) -> float

Generate a random float between min_val and max_val.

Parameters:

min_val (float): Minimum value

max_val (float): Maximum value

Returns: float - A random float within the specified range

Raises: ValueError - If min_val > max_val

Example:

from houdus import pick_float

temperature = pick_float(20.0, 25.0)  # Random temperature


step_sequence(start: int, stop: int, step: int = 1) -> List[int]

Generate a list of numbers from start to stop (exclusive) with a given step.

Parameters:

start (int): Starting value (inclusive)

stop (int): Ending value (exclusive)

step (int): Step between values (default: 1)

Returns: List[int] - A list of integers in the specified range

Example:

from houdus import step_sequence

evens = step_sequence(0, 10, 2)  # [0, 2, 4, 6, 8]
odds = step_sequence(1, 10, 2)   # [1, 3, 5, 7, 9]


distinct_ints(count: int, min_val: int, max_val: int) -> List[int]

Generate a list of count unique random integers within the range [min_val, max_val].

Parameters:

count (int): Number of unique integers to generate

min_val (int): Minimum value (inclusive)

max_val (int): Maximum value (inclusive)

Returns: List[int] - A list of unique random integers

Raises: ValueError - If count > (max_val - min_val + 1)

Example:

from houdus import distinct_ints

lottery_numbers = distinct_ints(6, 1, 49)  # Pick 6 unique numbers from 1 to 49


assign_seed(seed: Union[int, float, str, bytes, bytearray]) -> None

Set the seed for the random number generator to produce deterministic/reproducible results.

Parameters:

seed: A seed value (int, float, str, bytes, or bytearray)

Returns: None

Example:

from houdus import assign_seed, pick_int

assign_seed(42)
first_run = pick_int(1, 1000)

assign_seed(42)
second_run = pick_int(1, 1000)

assert first_run == second_run  # Always True


select_item(sequence: Sequence[Any]) -> Any

Select a random element from a non-empty sequence.

Parameters:

sequence: Any sequence (list, tuple, string, etc.)

Returns: Any - A random element from the sequence

Raises: ValueError - If sequence is empty

Example:

from houdus import select_item

card = select_item(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
element = select_item([1, 2, 3, 4, 5])


select_items(sequence: Sequence[Any], k: int = 1) -> List[Any]

Select k random elements from a sequence with replacement (allows duplicates).

Parameters:

sequence: Any sequence

k (int): Number of elements to select (default: 1)

Returns: List[Any] - A list of k random elements

Raises: ValueError - If sequence is empty or k is negative

Example:

from houdus import select_items

# Rolling a die 10 times
rolls = select_items([1, 2, 3, 4, 5, 6], k=10)

# Random colors with replacement
colors = select_items(['red', 'blue', 'green'], k=5)


mix_inplace(sequence: List[Any]) -> None

Shuffle a list in-place using the Fisher-Yates algorithm (modifies original list).

Parameters:

sequence: A list to shuffle (must be a list, not tuple or other sequences)

Returns: None (modifies list in-place)

Raises: TypeError - If sequence is not a list

Example:

from houdus import mix_inplace

deck = [1, 2, 3, 4, 5]
mix_inplace(deck)
print(deck)  # [3, 1, 5, 2, 4] (shuffled in-place)


mixed_copy(sequence: Sequence[Any]) -> List[Any]

Return a shuffled copy of a sequence without modifying the original.

Parameters:

sequence: Any sequence

Returns: List[Any] - A shuffled copy of the sequence

Example:

from houdus import mixed_copy

original = [1, 2, 3, 4, 5]
shuffled_copy = mixed_copy(original)
print(original)      # [1, 2, 3, 4, 5] (unchanged)
print(shuffled_copy) # [3, 1, 5, 2, 4] (shuffled)


generate_text(length: int = 10, charset: str = ...) -> str

Generate a random string of specified length using alphanumeric characters (or custom charset).

Parameters:

length (int): Length of the string (default: 10)

charset (str): Characters to use for generation (default: letters + digits)

Returns: str - A random string

Raises: ValueError - If length is negative or charset is empty

Example:

from houdus import generate_text

code = generate_text(8)           # 'aBc3DeF2'
token = generate_text(32)         # Random 32-char token
custom = generate_text(5, 'ABCD') # Random 5-char from ABCD


secure_password(length: int = 16, use_special: bool = True) -> str

Generate a secure random password with mixed character types.

Parameters:

length (int): Password length (default: 16, minimum: 4)

use_special (bool): Include special characters (default: True)

Returns: str - A secure random password

Raises: ValueError - If length < 4

Example:

from houdus import secure_password

# Generate a strong password
password = secure_password(20)  # 'xK#9mL$pQ@2bF!vRnT8J'

# Generate alphanumeric-only password
simple_password = secure_password(12, use_special=False)  # 'xK9mLpQ2bFvRn'


pick_weighted(items: Sequence[Any], weights: Sequence[float]) -> Any

Select a random item based on relative weights (probability).

Parameters:

items: Sequence of items to choose from

weights: Sequence of weights (probabilities) for each item

Returns: Any - A randomly selected item

Raises: ValueError - If items/weights empty, mismatched lengths, or sum of weights ≤ 0

Example:

from houdus import pick_weighted

# Weighted dice (biased toward higher numbers)
roll = pick_weighted([1, 2, 3, 4, 5, 6], [1, 1, 1, 2, 2, 3])

# Weighted selection
loot = pick_weighted(
    ['common', 'rare', 'legendary'],
    [0.7, 0.25, 0.05]
)


batch_ints(count: int, min_val: int, max_val: int) -> List[int]

Generate a list of random integers (batch operation).

Parameters:

count (int): Number of integers to generate

min_val (int): Minimum value (inclusive)

max_val (int): Maximum value (inclusive)

Returns: List[int] - List of random integers

Raises: ValueError - If count is negative or invalid range

Example:

from houdus import batch_ints

# Generate 10 random test values
test_data = batch_ints(10, 1, 100)

# Simulate 100 coin flips (1 = heads, 0 = tails)
flips = batch_ints(100, 0, 1)


batch_floats(count: int, min_val: float, max_val: float) -> List[float]

Generate a list of random floats (batch operation).

Parameters:

count (int): Number of floats to generate

min_val (float): Minimum value

max_val (float): Maximum value

Returns: List[float] - List of random floats

Raises: ValueError - If count is negative or invalid range

Example:

from houdus import batch_floats

# Generate 100 random coordinates
x_coords = batch_floats(100, 0.0, 100.0)
y_coords = batch_floats(100, 0.0, 100.0)

# Generate random temperatures
temps = batch_floats(30, 15.0, 35.0)  # 30 days of temperature


Use Cases

Games & Simulations

from houdus import pick_int, distinct_ints, select_item, mixed_copy, pick_weighted

# Dice roll
roll = pick_int(1, 6)

# Card shuffling (picking 5 unique cards from 52)
cards = distinct_ints(5, 1, 52)

# Random card suit
suit = select_item(['♠', '♥', '♦', '♣'])

# Shuffle a deck of cards
deck = list(range(1, 53))
shuffled_deck = mixed_copy(deck)

# Weighted loot drop (rarer items less likely)
loot = pick_weighted(['common', 'rare', 'epic', 'legendary'], [0.6, 0.25, 0.12, 0.03])


Testing & Quality Assurance

from houdus import assign_seed, pick_int, batch_ints, secure_password

# Reproducible test scenarios
assign_seed("test_scenario_001")
test_data = batch_ints(10, 1, 100)  # Batch generation

# Generate test user passwords
test_passwords = [secure_password(12) for _ in range(5)]


Data Generation

from houdus import pick_float, batch_floats, step_sequence, generate_text

# Generate sample coordinates efficiently
x_coords = batch_floats(100, 0, 100)
y_coords = batch_floats(100, 0, 100)
coordinates = list(zip(x_coords, y_coords))

# Generate batch IDs
batch_ids = step_sequence(1000, 1100)  # 1000 sequential IDs

# Generate random test tokens
tokens = [generate_text(32) for _ in range(10)]


Security & Authentication

from houdus import secure_password, generate_text

# Generate secure passwords for users
user_password = secure_password(20, use_special=True)

# Generate secure API tokens
api_token = generate_text(64, 'abcdef0123456789')  # Hex string

# Generate secure session IDs
session_id = generate_text(32)


Shuffling & Randomization

from houdus import mix_inplace, mixed_copy, select_item, select_items

# Shuffle survey questions to avoid bias
questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
shuffled_questions = mixed_copy(questions)

# Random playlist order
playlist = ['song1', 'song2', 'song3', 'song4', 'song5']
mix_inplace(playlist)
print(f"Playing: {select_item(playlist)}")

# Batch sampling with replacement
samples = select_items(range(1, 100), k=50)


Development

Prerequisites

Python 3.8 or higher

pip or poetry

Setup Development Environment

# Clone the repository
git clone [https://github.com/yourusername/houdus.git](https://github.com/yourusername/houdus.git)
cd houdus

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install development dependencies
pip install -e ".[dev]"


Running Tests

# Run all tests
pytest

# Run tests with coverage
pytest --cov=houdus

# Run tests with verbose output
pytest -v


Code Quality

# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/


Testing

The project uses pytest for testing. All functions are covered with comprehensive unit tests.

# Run tests
pytest

# Run specific test file
pytest tests/test_generator.py

# Run specific test function
pytest tests/test_generator.py::test_pick_int

# Run with coverage report
pytest --cov=houdus --cov-report=html


Performance

Houdus is lightweight and performant:

No external dependencies - Pure Python with standard library only

Minimal overhead - Simple wrapper around Python's built-in random module

Small memory footprint - Minimal package size

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git origin feature/AmazingFeature)

Open a Pull Request

Guidelines

Follow PEP 8 style guide

Use Black for code formatting

Add tests for any new functionality

Update documentation as needed

License

This project is licensed under the MIT License - see the LICENSE file for details.

Support

If you encounter any issues or have questions:

Check the GitHub Issues

Create a new issue with a clear description

Include Python version and relevant code snippets

Changelog

See RELEASES for version history and changes.

Acknowledgments

Built with Python's standard library

Inspired by the need for a simple, lightweight random number generation utility

Made with ❤️ by the Houdus Team