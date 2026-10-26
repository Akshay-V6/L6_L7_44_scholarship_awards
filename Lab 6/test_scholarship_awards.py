import pytest
from scholarship_awards import award_amount, is_eligible, application_status

# Example test cases:
def test_below_cutoff_marks():
    assert award_amount("merit", 70, "low", False) == 0

def test_is_eligible():
    assert is_eligible(90, 0, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.
