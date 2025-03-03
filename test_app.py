import unittest
from datetime import datetime

# Import functions from app.py
from app import get_player_id, get_player_stats

class TestMLBStatsApp(unittest.TestCase):
    
    def test_date_format_validation(self):
        """Test that invalid date formats are rejected."""
        stats, error = get_player_stats("Mike Trout", "invalid-date")
        self.assertTrue(stats.empty)
        self.assertIn("Invalid date format", error)
    
    def test_player_name_validation(self):
        """Test that player names need first and last name."""
        player_id, error = get_player_id("Trout")
        self.assertIsNone(player_id)
        self.assertIn("Please provide both first and last name", error)
    
    def test_date_parsing(self):
        """Test that valid dates are parsed correctly."""
        date_str = "2023-07-15"
        selected_date = datetime.strptime(date_str, "%Y-%m-%d")
        self.assertEqual(selected_date.year, 2023)
        self.assertEqual(selected_date.month, 7)
        self.assertEqual(selected_date.day, 15)

if __name__ == "__main__":
    unittest.main() 