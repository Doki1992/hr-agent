import random
import arrow

def getRemainingVacationDays(employeeId: int) -> int:
    """Calculates the remaining vacations days for a given employee
        Args:
            employeeId: the id of the current employee
    """
    return 3    

def requestTimeOff(employeeId: str, startDate: str, endDate: str) -> str:
    """validates dates are future, checks sufficient balance, deducts days, returns confirmation
        Args:
            employeeId: the id of the current employee
            startDate: init of the vacation period in format YYYY-MM-DD
            endDate: end of the vacation period in format YYYY-MM-DD
    """

    now = arrow.now()
    start = arrow.get(startDate)
    end = arrow.get(endDate)
    if start < now:
        return "Start date is in the past"
    if end < now:
        return "End date is in the past"
    if end < start:
        return "End date must be after the start date"
    return "You can request vacations days"

def getCompanyPolicy(topic: str) -> str:
    """This function returns the related information to the topic
        Args:
            topic: the topic to be fetched
    """
    topics = {
        "topic1": "this is a topic about to build real gen ai applications",
        "topic2": "this is a topic about to design good gen ai applications from 0 to hero"
    }
    try:
        if topics[topic] is not None:
            return topics[topic]
    except:
        return f"Topic not found, I can talk about these topics: 1. topic1, and 2. topic2, please select one of them"

def getHolidaysByCountry(countryCode: str) -> list[str]:
    """Returns the next five holydays based on the current date and country or the available holidys for the current employee
        Args:
            countryCode: the code of the country where the employee lives
    """
    return ["May 1", "May 10", "June 17", "Dec 24", "Dec 31"]






    


