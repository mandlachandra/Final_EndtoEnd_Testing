import unittest

# function to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# unit test class
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)      # ✅ fixed
        self.assertEqual(add(-1, 1), 0)       # ✅ fixed

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # ✅ fixed
        self.assertEqual(subtract(-1, 1), -2) # 📝 fixed expected result

# run test
if __name__ == "__main__":
    unittest.main() #test runner
