import math
from main import calculate_pi


def test_pi_5_digits():
    """Test that calculate_pi returns pi accurate to 5 decimal places"""
    calculated = calculate_pi(5)
    actual_pi = math.pi
    
    # Round both to 5 decimal places for comparison
    calculated_rounded = round(calculated, 5)
    actual_rounded = round(actual_pi, 5)
    
    print(f"Calculated Pi: {calculated}")
    print(f"Actual Pi:     {actual_pi}")
    print(f"Calculated (5 digits): {calculated_rounded}")
    print(f"Actual (5 digits):     {actual_rounded}")
    
    assert calculated_rounded == actual_rounded, f"Expected {actual_rounded}, got {calculated_rounded}"
    print("✓ Test passed: Pi calculated to 5 decimal places correctly!")


def test_pi_different_precisions():
    """Test calculate_pi with different precision levels"""
    test_cases = [
        (1, 3.1),
        (2, 3.14),
        (3, 3.142),
        (4, 3.1416),
        (5, 3.14159),
    ]
    
    print("\nTesting different precisions:")
    for digits, expected in test_cases:
        calculated = calculate_pi(digits)
        calculated_rounded = round(calculated, digits)
        print(f"  {digits} digits: {calculated_rounded} (expected: {expected})")
        assert calculated_rounded == expected, f"Failed for {digits} digits"
    
    print("✓ All precision tests passed!")


def test_pi_range():
    """Test that calculated pi is within reasonable range"""
    calculated = calculate_pi(5)
    
    # Pi should be between 3.14 and 3.15
    assert 3.14 < calculated < 3.15, f"Pi {calculated} is out of expected range"
    print("\n✓ Range test passed!")


def test_pi_accuracy():
    """Test the absolute difference between calculated and actual pi"""
    calculated = calculate_pi(5)
    actual_pi = math.pi
    
    # The difference should be very small (less than 0.00001 for 5 digits)
    difference = abs(calculated - actual_pi)
    print(f"\nAbsolute difference: {difference}")
    
    assert difference < 0.00001, f"Difference {difference} is too large"
    print("✓ Accuracy test passed!")


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Pi Calculation Function")
    print("=" * 60)
    
    try:
        test_pi_5_digits()
        test_pi_different_precisions()
        test_pi_range()
        test_pi_accuracy()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
