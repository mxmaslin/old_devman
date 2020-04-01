import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_none(self):
        formatted = format_price(None)
        self.assertEqual(formatted, None)

    def test_string(self):
        formatted = format_price('abc')
        self.assertEqual(formatted, None)

    def test_bool_true(self):
        formatted = format_price(True)
        self.assertEqual(formatted, None)

    def test_bool_false(self):
        formatted = format_price(False)
        self.assertEqual(formatted, None)

    def test_string_int(self):
        formatted = format_price('100000')
        self.assertEqual(formatted, '100 000')

    def test_string_float(self):
        formatted = format_price('100000.10')
        self.assertEqual(formatted, '100 000.10')

    def test_zero(self):
        formatted = format_price(0)
        self.assertEqual(formatted, '0')

    def test_int1(self):
        formatted = format_price(1)
        self.assertEqual(formatted, '1')

    def test_int2(self):
        formatted = format_price(1000000)
        self.assertEqual(formatted, '1 000 000')

    def test_negative_int1(self):
        formatted = format_price(-1)
        self.assertEqual(formatted, '-1')

    def test_negative_int2(self):
        formatted = format_price(-1000000)
        self.assertEqual(formatted, '-1 000 000')

    def test_float1(self):
        formatted = format_price(1.00)
        self.assertEqual(formatted, '1')

    def test_float2(self):
        formatted = format_price(1.01)
        self.assertEqual(formatted, '1.01')

    def test_float3(self):
        formatted = format_price(1.001)
        self.assertEqual(formatted, '1')

    def test_float4(self):
        formatted = format_price(1.009)
        self.assertEqual(formatted, '1.01')

    def test_float5(self):
        formatted = format_price(1.1)
        self.assertEqual(formatted, '1.10')

    def test_float6(self):
        formatted = format_price(1.5)
        self.assertEqual(formatted, '1.50')

    def test_float7(self):
        formatted = format_price(1.555)
        self.assertEqual(formatted, '1.55')

    def test_float8(self):
        formatted = format_price(1.999)
        self.assertEqual(formatted, '2')

    def test_float9(self):
        formatted = format_price(1000.001)
        self.assertEqual(formatted, '1 000')

    def test_float10(self):
        formatted = format_price(1000.10)
        self.assertEqual(formatted, '1 000.10')

    def test_float11(self):
        formatted = format_price(1000.999)
        self.assertEqual(formatted, '1 001')

    def test_negative_float1(self):
        formatted = format_price(-1.00)
        self.assertEqual(formatted, '-1')

    def test_negative_float2(self):
        formatted = format_price(-1.01)
        self.assertEqual(formatted, '-1.01')

    def test_negative_float3(self):
        formatted = format_price(-1.001)
        self.assertEqual(formatted, '-1')

    def test_negative_float4(self):
        formatted = format_price(-1.009)
        self.assertEqual(formatted, '-1.01')

    def test_negative_float5(self):
        formatted = format_price(-1.1)
        self.assertEqual(formatted, '-1.10')

    def test_negative_float6(self):
        formatted = format_price(-1.5)
        self.assertEqual(formatted, '-1.50')

    def test_negative_float7(self):
        formatted = format_price(-1.555)
        self.assertEqual(formatted, '-1.55')

    def test_negative_float8(self):
        formatted = format_price(-1.999)
        self.assertEqual(formatted, '-2')

    def test_negative_float9(self):
        formatted = format_price(-1000.001)
        self.assertEqual(formatted, '-1 000')

    def test_negative_float10(self):
        formatted = format_price(-1000.10)
        self.assertEqual(formatted, '-1 000.10')

    def test_negative_float11(self):
        formatted = format_price(-1000.999)
        self.assertEqual(formatted, '-1 001')


if __name__ == '__main__':
    unittest.main()
