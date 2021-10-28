import unittest


def score_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80 & score < 90:
        return 'B'
    elif score >= 70 & score < 80:
        return 'C'
    elif score >= 60 & score < 70:
        return 'D'


class TestScore(unittest.TestCase):

    def test_score(self):
        self.assertEqual(score_grade(90), 'A')
