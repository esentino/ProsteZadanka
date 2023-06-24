import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def speed(distance, time):
    """Calculates and returns the average speed in meters per second.

    Args:
        distance (float): The distance in meters.
        time (float): The time in seconds.

    Returns:
        str: The average speed in meters per second.
    """
    if time == 0:
        logger.warning("Czas nie może być równy zero.")

    average_speed = distance / time
    logger.info(f"distance: {distance}, time: {time}")
    return f"average speed: {average_speed: .2f} m/s"


print(speed(100, 10))  # zwróci 10 m/s
print(speed(2, 10))  # zwróci 0.2 m/s
# print(speed(2, 0))  # zwróci 0.2 m/s
