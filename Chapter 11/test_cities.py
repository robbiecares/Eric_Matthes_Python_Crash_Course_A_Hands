import unittest
from cities import assemble_details

class CityTestCase(unittest.TestCase):
    """Tests for 'cities.py'."""

    def test_city_country(self):
        """Do cities like 'St. Paul' work?"""
        fulltext = assemble_details("KINSHASA","Republic of the Congo and Zaire",population = 14_342_439)
        self.assertEqual(fulltext,"Kinshasa, Republic of the Congo and Zaire - population 14342439")

if __name__ == "__main__":
    unittest.main()


