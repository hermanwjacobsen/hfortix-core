import sys
from pathlib import Path

# Add pytest directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from hfortix_fortios._helpers.validators import (
    validate_schedule_name,
    validate_time_format,
    validate_day_names,
)


def test_validate_schedule_name():
    """Test: Validate schedule name (max 31 characters)"""
    # Valid schedule names
    validate_schedule_name("daily_backup", "create")
    validate_schedule_name("weekly_maintenance", "update")
    validate_schedule_name("a" * 31, "delete")  # Max length
    
    # Invalid schedule names
    try:
        validate_schedule_name(None, "create")
        assert False, "Should raise ValueError for None name"
    except ValueError as e:
        assert "required" in str(e)
    
    try:
        validate_schedule_name("", "create")
        assert False, "Should raise ValueError for empty string"
    except ValueError as e:
        assert "empty" in str(e)
    
    try:
        validate_schedule_name("a" * 32, "create")  # Too long
        assert False, "Should raise ValueError for name > 31 chars"
    except ValueError as e:
        assert "31" in str(e)


def test_validate_time_format():
    """Test: Validate time format is HH:MM (00:00-23:59)"""
    # Valid time formats
    validate_time_format("00:00", "start_time")
    validate_time_format("12:30", "end_time")
    validate_time_format("23:59", "time")
    validate_time_format("09:15", "schedule_time")
    
    # Invalid time formats
    try:
        validate_time_format("", "time")
        assert False, "Should raise ValueError for empty time"
    except ValueError as e:
        assert "required" in str(e)
    
    try:
        validate_time_format("24:00", "time")  # Invalid hour
        assert False, "Should raise ValueError for hour >= 24"
    except ValueError:
        pass
    
    try:
        validate_time_format("12:60", "time")  # Invalid minute
        assert False, "Should raise ValueError for minute >= 60"
    except ValueError:
        pass
    
    try:
        validate_time_format("12-30", "time")  # Wrong separator
        assert False, "Should raise ValueError for wrong separator"
    except ValueError:
        pass
    
    try:
        validate_time_format("1230", "time")  # Missing colon
        assert False, "Should raise ValueError for missing colon"
    except ValueError:
        pass
    
    try:
        validate_time_format("invalid", "time")
        assert False, "Should raise ValueError for invalid format"
    except ValueError:
        pass


def test_validate_day_names():
    """Test: Validate day names for recurring schedule"""
    # Valid day names
    validate_day_names("monday")
    validate_day_names("monday tuesday wednesday")
    validate_day_names("saturday sunday")
    validate_day_names("monday tuesday wednesday thursday friday")
    validate_day_names("none")  # Special case
    validate_day_names("MONDAY")  # Case insensitive
    validate_day_names("Monday Tuesday")  # Mixed case
    
    # Invalid day names
    try:
        validate_day_names("")
        assert False, "Should raise ValueError for empty day string"
    except ValueError as e:
        assert "at least one day" in str(e).lower()
    
    try:
        validate_day_names("invalid_day")
        assert False, "Should raise ValueError for invalid day name"
    except ValueError as e:
        assert "Invalid day" in str(e)
    
    try:
        validate_day_names("monday invalid_day")
        assert False, "Should raise ValueError for one invalid day in list"
    except ValueError as e:
        assert "Invalid day" in str(e)
    
    try:
        validate_day_names("mon")  # Abbreviated form not allowed
        assert False, "Should raise ValueError for abbreviated day"
    except ValueError as e:
        assert "Invalid day" in str(e)


if __name__ == "__main__":
    test_validate_schedule_name()
    print("✓ test_validate_schedule_name passed")
    
    test_validate_time_format()
    print("✓ test_validate_time_format passed")
    
    test_validate_day_names()
    print("✓ test_validate_day_names passed")
    
    print("\n✓ All schedule validator tests passed!")
