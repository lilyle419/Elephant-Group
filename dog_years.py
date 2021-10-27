# this function determines the calendar of a dogs life compared to a human's life

def dog_years (dog_calendar):
    """"compute the human age of dog years
    
    Args:
        dog_calendar (int): age of dog in calendar years

    Raises:
        ValueError: specify the age when it is negative

    Returns:
        int: age of the dog in human years
    """

    human_years = 0
    if dog_calendar == 1: 
        human_years = 15
    elif dog_calendar == 2:
        human_years = 24
    elif dog_calendar > 2:
        human_years = 24 + (dog_calendar-2) * 5
    return human_years

if __name__ == "__main__":
    print(dog_years(4))
    print(dog_years(5))
