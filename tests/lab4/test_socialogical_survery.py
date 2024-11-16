import unittest

from src.lab4.sociological_survey import *


class TestAgeGroup(unittest.TestCase):
    def test_contains(self):
        group = AgeGroup(18, 65)
        self.assertTrue(group.contains(20))
        self.assertFalse(group.contains(17))
        self.assertFalse(group.contains(66))

    def test_str(self):
        group = AgeGroup(18, 65)
        self.assertEqual(group.str(), "18-65")
        group = AgeGroup(101, 101, last=True)
        self.assertEqual(group.str(), "101+")


class TestRespondent(unittest.TestCase):
    def test_str(self):
        respondent = Respondent("Иванов Иван Иванович", 30)
        self.assertEqual(respondent.str(), "Иванов Иван Иванович (30)")


class TestAgeGroupDivider(unittest.TestCase):
    def setUp(self):
        self.age_groups = [AgeGroup(0, 10), AgeGroup(11, 20), AgeGroup(21, 30)]
        self.divider = AgeGroupDivider(self.age_groups)

    def test_add_respondent(self):
        respondent = Respondent("Сидоров Владимир Иванович", 15)
        self.divider.add_respondent(respondent)
        self.assertIn(respondent, self.divider.grouped_respondents[self.age_groups[1]])


class TestParseAgeGroups(unittest.TestCase):
    def test_parse_age_groups(self):
        args = ["20", "40", "60"]
        needed = ["0-20", "21-40", "41-60", "61+"]
        actual_age_groups = [age_group.str() for age_group in parse_age_groups(args)]
        self.assertEqual(actual_age_groups, needed)


if __name__ == "__main__":
    unittest.main()
