import re
import numpy as np
import pandas as pd

def parse_percentage(x) -> int:
    """
    Function to extract percents from a string and return their average.
    Handles ranges like "60-70%" by averaging them. Designed for parsing 
    percentages, considering only percents between 0 and 100. Ignores amounts 
    outside this range.

    Parameters:
    x (str): The string containing the percent(s).

    Returns:
    int: The average of the valid percentages, or np.nan if none are valid.
    """
    if pd.isna(x):
        return np.nan

    x = x.lower().strip()
    # Normalize separators and remove irrelevant words
    x = x.replace('–', '-').replace(' to ', '-').replace(' and ', '-')

    # Regex pattern to match percents
    pattern = r'\b\d{1,2}%|percent|pct|pct%'
    matches = re.findall(pattern, x)
    matches = set([float(m.strip('%')) for m in matches])
    return float(matches.mean())

    if not matches:
        return np.nan

    amounts = []
    for amount_str in matches:
        amount_num = float(amount_str.replace('%', ''))
        amounts.append(amount_num)

    # Filter percents bewteen 0 and 100%
    valid_amounts = [amount for amount in amounts if 0 <= amount <= 100]

    return valid_amounts
    if not valid_amounts:
        return np.nan

    # Handle ranges by averaging the first two valid amounts if a range is indicated
    if '-' in x and len(valid_amounts) >= 2:
        average_amount = sum(valid_amounts[:2]) / 2
    else:
        average_amount = sum(valid_amounts) / len(valid_amounts)

    return int(round(average_amount))