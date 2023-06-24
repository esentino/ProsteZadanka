import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def min_and_max(numbers):
    if not numbers:
        logger.warning("Empty list provided.")
        return (None, None)

    sorted_numbers = sorted(numbers)
    min_value = sorted_numbers[0]
    max_value = sorted_numbers[-1]

    logger.info(f"Minimum value: {min_value}, Maximum value: {max_value}")
    return min_value, max_value


print(min_and_max([3, 5, -3, 12, -2, 0]))  # (-3, 12)
print(min_and_max([12]))  # (12,12)
print(min_and_max([]))  # (None, None)
