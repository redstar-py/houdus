🎲 houdus

A lightweight, zero-dependency Python package for generating random numbers and sequences with a clean, intuitive API.

✨ Features

🎲 Easy Random Generation – Generate random integers and floats with simple function calls.

🔢 Unique Sequences – Generate lists of unique random numbers within a specific range.

📊 Custom Step Ranges – Create sequences of numbers with custom steps.

🔐 Deterministic Results – Set seeds for completely reproducible random generation.

🚀 Zero Dependencies – Pure Python implementation utilizing only the standard library.

💡 Type Hints – Full type annotations for robust IDE support and static type checking.

📦 Ultra Lightweight – Minimal package size and memory footprint.

⚙️ Installation

Via pip (Recommended)

pip install houdus


From Source

git clone [https://github.com/redstar-py/houdus.git](https://github.com/redstar-py/houdus.git)
cd houdus
pip install .


For Development

git clone [https://github.com/redstar-py/houdus.git](https://github.com/redstar-py/houdus.git)
cd houdus
pip install -e ".[dev]"


🚀 Quick Start

from houdus import pick_int, pick_float, step_sequence, distinct_ints, assign_seed

# 1. Generate a random integer between 1 and 100 (inclusive)
print(pick_int(1, 100))  # Output: 42

# 2. Generate a random float between 0.0 and 1.0
print(pick_float(0.0, 1.0))  # Output: 0.8739...

# 3. Generate a list of 5 unique numbers between 1 and 50
print(distinct_ints(5, 1, 50))  # Output: [3, 15, 42, 28, 7]

# 4. Generate a sequence of numbers from 1 to 10 with step 2
print(step_sequence(1, 11, 2))  # Output: [1, 3, 5, 7, 9]

# 5. Set a seed for deterministic/reproducible results
assign_seed(42)
print(pick_int(1, 100))  # Always outputs the same number


📚 API Reference

Quick Lookup

Function

Return Type

Description

pick_int(min_val, max_val)

int

Random integer within a range (inclusive).

pick_float(min_val, max_val)

float

Random float within a range.

step_sequence(start, stop, step)

List[int]

Sequential list with custom steps (exclusive stop).

distinct_ints(count, min_val, max_val)

List[int]

Unique random integers without duplicates.

assign_seed(seed)

None

Set the seed for deterministic results.

select_item(sequence)

Any

Pick a random single item from a sequence.

select_items(sequence, k)

List[Any]

Pick k items with replacement (duplicates allowed).

mix_inplace(sequence)

None

Shuffle a list in-place (modifies original).

mixed_copy(sequence)

List[Any]

Return a shuffled copy (leaves original intact).

generate_text(length, charset)

str

Generate a random alphanumeric or custom string.

secure_password(length, use_special)

str

Generate a cryptographically secure random password.

pick_weighted(items, weights)

Any

Select an item based on relative probability weights.

batch_ints(count, min_val, max_val)

List[int]

Optimized batch generation of random integers.

batch_floats(count, min_val, max_val)

List[float]

Optimized batch generation of random floats.

🎲 Core Random Generation

pick_int(min_val: int, max_val: int) -> int

Generate a random integer between min_val and max_val (inclusive).

Raises: ValueError if min_val > max_val.

from houdus import pick_int
die_roll = pick_int(1, 6)


pick_float(min_val: float, max_val: float) -> float

Generate a random float between min_val and max_val.

Raises: ValueError if min_val > max_val.

from houdus import pick_float
temperature = pick_float(20.0, 25.0)


assign_seed(seed: Union[int, float, str, bytes, bytearray]) -> None

Set the global seed for the random number generator to ensure fully reproducible results.

from houdus import assign_seed, pick_int

assign_seed(42)
first_run = pick_int(1, 1000)

assign_seed(42)
second_run = pick_int(1, 1000)

assert first_run == second_run  # Always True


🔢 Sequences & Shuffling

step_sequence(start: int, stop: int, step: int = 1) -> List[int]

Generate a predictable list of numbers from start (inclusive) to stop (exclusive) incremented by step.

from houdus import step_sequence
evens = step_sequence(0, 10, 2)  # [0, 2, 4, 6, 8]


distinct_ints(count: int, min_val: int, max_val: int) -> List[int]

Generate a list of count unique random integers within the range [min_val, max_val].

Raises: ValueError if requested count is greater than the available range.

from houdus import distinct_ints
lottery_numbers = distinct_ints(6, 1, 49)


select_item(sequence: Sequence[Any]) -> Any

Select a single random element from a non-empty sequence.

from houdus import select_item
card = select_item(['Hearts', 'Diamonds', 'Clubs', 'Spades'])


select_items(sequence: Sequence[Any], k: int = 1) -> List[Any]

Select k random elements from a sequence with replacement (allows duplicates).

from houdus import select_items
rolls = select_items([1, 2, 3, 4, 5, 6], k=10)


mix_inplace(sequence: List[Any]) -> None

Shuffle a list in-place using the Fisher-Yates algorithm.

⚠️ Warning: This modifies the original list object and requires a mutable List.

from houdus import mix_inplace
deck = [1, 2, 3, 4, 5]
mix_inplace(deck)  # deck is now mutated (e.g., [3, 1, 5, 2, 4])


mixed_copy(sequence: Sequence[Any]) -> List[Any]

Return a completely shuffled copy of a sequence without modifying the original.

from houdus import mixed_copy
original = [1, 2, 3, 4, 5]
shuffled = mixed_copy(original)  # original remains unchanged


🔐 Strings & Security

generate_text(length: int = 10, charset: str = ...) -> str

Generate a random string of a specified length using alphanumeric characters or a custom charset.

from houdus import generate_text
hex_token = generate_text(32, charset="abcdef0123456789")


secure_password(length: int = 16, use_special: bool = True) -> str

Generate a secure random password with mixed character types.

Raises: ValueError if length < 4.

from houdus import secure_password
password = secure_password(20, use_special=True)


📊 Advanced & Batch Operations

pick_weighted(items: Sequence[Any], weights: Sequence[float]) -> Any

Select a random item based on relative probability distributions.

from houdus import pick_weighted
loot = pick_weighted(['common', 'rare', 'legendary'], [0.70, 0.25, 0.05])


batch_ints(count: int, min_val: int, max_val: int) -> List[int]

Efficiently generate a batch list of random integers.

from houdus import batch_ints
coin_flips = batch_ints(100, 0, 1)  # 100 results of 0 or 1


batch_floats(count: int, min_val: float, max_val: float) -> List[float]

Efficiently generate a batch list of random floats.

from houdus import batch_floats
x_coords = batch_floats(1000, 0.0, 100.0)


💡 Practical Use Cases

from houdus import pick_int, select_item, pick_weighted

# Simulate a standard D&D D20 roll
d20_roll = pick_int(1, 20)

# Randomly select NPC dialogue suit
npc_mood = select_item(['Friendly', 'Hostile', 'Neutral'])

# Enemy item drop rate calculation
dropped_item = pick_weighted(
    ['Gold Coin', 'Health Potion', 'Mythic Sword'], 
    [0.80, 0.18, 0.02]
)


from houdus import assign_seed, batch_ints, generate_text

# Reproducible test environments
assign_seed("mock_user_pipeline")
mock_user_ages = batch_ints(50, 18, 65)

# Session key generation
test_session_tokens = [generate_text(32) for _ in range(5)]


🛠️ Development & Contribution

Prerequisites

Python 3.8 or higher

pip or poetry

Setup Development Environment

# Clone and enter the repository
git clone [https://github.com/redstar-py/houdus.git](https://github.com/redstar-py/houdus.git)
cd houdus

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"


Running Tests & Coverage

# Run all unit tests
pytest

# Run tests with verbose output
pytest -v

# Generate a test coverage report
pytest --cov=houdus --cov-report=html
