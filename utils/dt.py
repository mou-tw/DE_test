from datetime import datetime

def get_today_date_string():
    """
    Return the current date as a string in the format YYYY-MM-DD.

    :return: A string representing today's date
    """
    # Get the current date
    today = datetime.today()
    
    # Format the date as a string in the format YYYY-MM-DD
    date_string = today.strftime('%Y%m%d')
    
    return date_string