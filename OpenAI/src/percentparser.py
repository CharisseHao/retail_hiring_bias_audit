import re
import numpy as np
import pandas as pd

def parse_percentage(x) -> int:
    """
    Function to extract percents from a string and return their average.
    Designed for parsing percentages, considering only percents between 
    0 and 100. Ignores amounts outside this range.

    Parameters:
    x (str): The string containing the percent(s).

    Returns:
    int: The average of the valid percentages, or np.nan if none are valid.
    """
    if pd.isna(x) or (len(x) == 0):
        return np.nan

    x = x.lower().strip()

    # Regex pattern to match percents
    pattern = r'-?\d+(?:%| pct| percent|pct%)?' #r'-?\d*%|percent|pct|pct%'
    matches = re.findall(pattern, x)

    # Extract numbers
    valid_amounts = []
    for match in matches:
        # Strip non-numeric parts and convert to float
        number = re.search(r'-?\d*', match).group()
        if len(number) > 0:
            number = float(number)
            if 0 <= number <= 100:
                valid_amounts.append(number)

    if valid_amounts:
        return sum(valid_amounts) / len(valid_amounts)
    return np.nan