import random
import string
from typing import Any, List, Sequence, Union
from .utils import verify_bounds  

def assign_seed(seed: Union[int, float, str, bytes, bytearray]) -> None:
    """Set the seed for deterministic random number generation."""
    random.seed(seed)

def pick_int(min_val: int, max_val: int) -> int:
    """Generate a random integer between min_val and max_val (inclusive)."""
    verify_bounds(min_val, max_val)
    return random.randint(min_val, max_val) 

def pick_float(min_val: float, max_val: float) -> float:
    """Generate a random float between min_val and max_val."""
    verify_bounds(min_val, max_val)
    return random.uniform(min_val, max_val)

def step_sequence(start: int, stop: int, step: int = 1) -> List[int]:
    """Generate a range of numbers as a list."""
    return list(range(start, stop, step))

def distinct_ints(count: int, min_val: int, max_val: int) -> List[int]:
    """Generate a list of unique random integers within a specific range."""
    verify_bounds(min_val, max_val)

    if count > (max_val - min_val + 1):
        raise ValueError("Count exceeds the number of available unique integers in the range.")

    return random.sample(range(min_val, max_val + 1), count)  

def select_item(sequence: Sequence[Any]) -> Any:
    """Select a random element from a non-empty sequence."""
    if not sequence:
        raise ValueError("Cannot choose from an empty sequence.")
    return random.choice(sequence)

def select_items(sequence: Sequence[Any], k: int = 1) -> List[Any]:
    """Select k random elements from a sequence with replacement."""
    if not sequence:
        raise ValueError("Cannot choose from an empty sequence.")
    if k < 0:
        raise ValueError("k must be non-negative.")
    return random.choices(sequence, k=k)

def mix_inplace(sequence: List[Any]) -> None:
    """Shuffle a list in-place using the Fisher-Yates algorithm."""
    if not isinstance(sequence, list):
        raise TypeError("mix_inplace() requires a list object.")
    random.shuffle(sequence)

def mixed_copy(sequence: Sequence[Any]) -> List[Any]:
    """Return a shuffled copy of a sequence."""
    if not sequence:
        return []
    sequence_copy = list(sequence)
    random.shuffle(sequence_copy)
    return sequence_copy

def generate_text(length: int = 10, charset: str = string.ascii_letters + string.digits) -> str:
    """Generate a random string of specified length using the given character set."""
    if length < 0:
        raise ValueError("length must be non-negative.")
    if not charset:
        raise ValueError("charset cannot be empty.")
    return "".join(random.choice(charset) for _ in range(length))

def secure_password(length: int = 16, use_special: bool = True) -> str:
    """Generate a secure random password of specified length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation if use_special else ""
    
    all_chars = lowercase + uppercase + digits + special
    
    # Ensure at least one of each required type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]
    
    if use_special:
        password_chars.append(random.choice(special))
    
    # Fill remaining length with random characters
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)
    return "".join(password_chars)

def pick_weighted(items: Sequence[Any], weights: Sequence[float]) -> Any:
    """Select a random item based on relative weights."""
    if not items:
        raise ValueError("items cannot be empty.")
    if not weights:
        raise ValueError("weights cannot be empty.")
    if len(items) != len(weights):
        raise ValueError("items and weights must have the same length.")
    if sum(weights) <= 0:
        raise ValueError("Sum of weights must be positive.")
    
    return random.choices(items, weights=weights, k=1)[0]

def batch_ints(count: int, min_val: int, max_val: int) -> List[int]:
    """Generate a list of random integers within a specified range."""
    if count < 0:
        raise ValueError("count must be non-negative.")
    verify_bounds(min_val, max_val)
    return [random.randint(min_val, max_val) for _ in range(count)]

def batch_floats(count: int, min_val: float, max_val: float) -> List[float]:
    """Generate a list of random floats within a specified range."""
    if count < 0:
        raise ValueError("count must be non-negative.")
    verify_bounds(min_val, max_val)
    return [random.uniform(min_val, max_val) for _ in range(count)]