import unittest

from synthetic_healthboard import degraded


class SyntheticHealthboardTest(unittest.TestCase):
    def test_flags_low_pass_rate(self):
        rows = [{"journey": "checkout", "status": "pass"}, {"journey": "checkout", "status": "fail"}]
        self.assertEqual(degraded(rows), ["checkout"])


if __name__ == "__main__":
    unittest.main()
