def verify_bounds(min_val: int | float, max_val: int | float):
    """Utility function to validate that the minimum value is not greater than the maximum."""
    if min_val > max_val:
        raise ValueError(f"min_val ({min_val}) cannot be greater than max_val ({max_val})")