import unittest
from arithmetic import calculate


class ArithmeticTests(unittest.TestCase):
    def test_precedence_and_negative_values(self):
        self.assertEqual(calculate('2 + 3 * 4'), 14)
        self.assertEqual(calculate('-(2 + 3) ** 2'), -25)
        self.assertEqual(calculate('10 // 3'), 3)

    def test_rejects_python_execution(self):
        for expression in ['__import__("os")', 'abs(-1)', '(1).__class__', '[1]', 'True']:
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                calculate(expression)

    def test_invalid_or_excessive_expressions(self):
        for expression in ['1/0', '2 ** 100000000', '9' * 300, '(-1)**0.5', '1e309', '2+']:
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                calculate(expression)


if __name__ == '__main__':
    unittest.main()
