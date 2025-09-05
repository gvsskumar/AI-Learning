import unittest

# Function to test
def add(a, b):
    return a + b

# Test case
class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()

# Steps to write a unittest case
# assertEqual(a, b) → check a == b
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIs(a, b) → same object
# assertIsNone(x)
# assertIn(a, b) → a in b
#assertRaises(Exception, func, *args)
# assertRaisesRegex(Exception, regex, func, *args)
# assertWarns(warning, func, *args)
# assertWarnsRegex(warning, regex, func, *args)
# assertLogs(logger, level)
# assertLogs(logger, level, msg)
# assertLogs(logger, level, msg, regex)
# assertCountEqual(a, b)
# assertSequenceEqual(a, b)
# assertTupleEqual(a, b)
# assertListEqual(a, b)
# assertDictEqual(a, b)
# assertSetEqual(a, b)
# assertMultiLineEqual(a, b)