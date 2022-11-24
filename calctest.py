import unittest

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError('Не можна ділити на нуль!!!')
    return x / y


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 100), 100)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(0, 100), -100)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 50)
        self.assertEqual(multiply(-10, 2), -20)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 100), 0)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
