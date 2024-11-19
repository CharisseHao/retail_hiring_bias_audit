import unittest
import numpy as np
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from percentparser import parse_percentage 


class TestParsePercentage(unittest.TestCase):

    def test_only_percentage(self):
        self.assertEqual(parse_percentage("65%"),
                         65.0)

    def test_single_percentage_1(self):
        self.assertEqual(parse_percentage("Based on the provided resume, the hiring probability is 85%."), 
                         85.0)
        
    def test_single_percentage_2(self):
        self.assertEqual(parse_percentage("I would estimate the hiring probability for this candidate at80%."), 
                         80.0)

    def test_percentage_with_word(self):
        self.assertEqual(parse_percentage("I would estimate the hiring probability for this candidate at 90 percent."),
                         90.0)

    def test_percentage_with_pct(self):
        self.assertEqual(parse_percentage("I would estimate the hiring probability for this candidate at 50 pct."),
                         50.0)

    def test_invalid_percentage(self):
        result = parse_percentage("The hiring probability is 150%.")                         
        self.assertTrue(pd.isna(result)) # Outside of valid range

    def test_no_percentage(self):
        result = parse_percentage("No percentage mentioned here.")
        self.assertTrue(pd.isna(result))

    def test_empty_string(self):
        result = parse_percentage("")
        self.assertTrue(pd.isna(result))

    def test_multiple_percentages(self):
        self.assertEqual(parse_percentage("I would estimate the hiring probability for this candidate between 60% to 80%."),
                         70.0)  # Average of 60% and 80%

    def test_percentage_in_range_1(self):
        self.assertEqual(parse_percentage("The candidate's hiring probability is between 30% and 50%."),
                         40.0)  # Average of 30% and 50%
        
    def test_percentage_in_range_2(self):
        self.assertEqual(parse_percentage("The candidate's hiring probability is from 30% to 50%."),
                         40.0)  # Average of 30% and 50%

    def test_percentage_with_extra_text(self):
        self.assertEqual(parse_percentage("The candidate's probability is 20% and the likelihood is 60 percent."),
                         40.0)  # Average of 20% and 60%

    def test_all_invalid_percentages(self):
        result = parse_percentage("Their probability is 200%, and another one is -5%.")
        self.assertTrue(pd.isna(result))

    def test_nan_input(self):
        result = parse_percentage(pd.NA)
        self.assertTrue(pd.isna(result))


if __name__ == '__main__':
    unittest.main()
