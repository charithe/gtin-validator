#!/usr/bin/env python

import unittest
from .validator import *


class GTINValidatorTest(unittest.TestCase):

    def test_incorrect_length_string(self):
        self.assertFalse(is_valid_GTIN("1234567"))

    def test_incorrect_length_string_valid_when_padded(self):
        self.assertFalse(is_valid_GTIN("123"))

    def test_incorrect_length_number(self):
        self.assertFalse(is_valid_GTIN(12345678910))

    def test_correct_length_string_with_spaces(self):
        self.assertFalse(is_valid_GTIN(" 1234567891 "))

    def test_correct_length_string_with_dashes(self):
        self.assertFalse(is_valid_GTIN("123-456-7890"))

    def test_alphanumeric_string(self):
        self.assertFalse(is_valid_GTIN("98795147A"))

    def test_valid_gtin8_string_no_leading_zeros(self):
        self.assertTrue(is_valid_GTIN("98795147"))

    def test_valid_gtin8_string_with_leading_zeros(self):
        self.assertTrue(is_valid_GTIN("0000098795147"))

    def test_valid_gtin8_string_with_leading_zeros_and_dashes(self):
        self.assertTrue(is_valid_GTIN("000-0-098-79514-7"))

    def test_valid_gtin8_number(self):
        self.assertTrue(is_valid_GTIN(98795147))

    def test_gtin8_invalid_check_digit(self):
        self.assertFalse(is_valid_GTIN("98795145"))

    def test_valid_gtin12_string_no_leading_zeros(self):
        self.assertTrue(is_valid_GTIN("951753852654"))

    def test_valid_gtin12_string_with_leading_zeros(self):
        self.assertTrue(is_valid_GTIN("0951753852654"))

    def test_valid_gtin12_string_with_leading_zeros_and_dashes(self):
        self.assertTrue(is_valid_GTIN("095-1-753-85265-4"))

    def test_valid_gtin12_number(self):
        self.assertTrue(is_valid_GTIN(951753852654))

    def test_gtin12_invalid_check_digit(self):
        self.assertFalse(is_valid_GTIN("951753852651"))

    def test_valid_gtin13_string(self):
        self.assertTrue(is_valid_GTIN("9780552133265"))

    def test_valid_gtin13_string_with_dashes(self):
        self.assertTrue(is_valid_GTIN("978-0-552-13326-5"))

    def test_valid_gtin13_number(self):
        self.assertTrue(is_valid_GTIN(9780552133265))

    def test_gtin13_invalid_check_digit(self):
        self.assertFalse(is_valid_GTIN("9780552133262"))

    def test_valid_gtin14_string(self):
        self.assertTrue(is_valid_GTIN("95135725845679"))

    def test_valid_gtin14_number(self):
        self.assertTrue(is_valid_GTIN(95135725845679))

    def test_gtin14_invalid_check_digit(self):
        self.assertFalse(is_valid_GTIN("95135725845672"))

    def test_checksum_multiple_of_ten(self):
        self.assertTrue(is_valid_GTIN("7896085864520"))

    def test_add_check_digit_gtin14_string(self):
        self.assertEquals(add_check_digit('9513572584567'), '95135725845679')

    def test_add_check_digit_gtin14_number(self):
        self.assertEquals(add_check_digit(9513572584567), '95135725845679')

    def test_add_check_digit_gtin13_string(self):
        self.assertEquals(add_check_digit('978055213326'), '09780552133265')

    def test_add_check_digit_gtin13_number(self):
        self.assertEquals(add_check_digit(978055213326), '09780552133265')

    def test_add_check_digit_gtin13_leading_zeros(self):
        self.assertEquals(add_check_digit('0978055213326'), '09780552133265')

    def test_add_check_digit_gtin12_string(self):
        self.assertEquals(add_check_digit('95175385265'), '00951753852654')

    def test_add_check_digit_gtin12_number(self):
        self.assertEquals(add_check_digit(95175385265), '00951753852654')

    def test_add_check_digit_gtin12_leading_zeros(self):
        self.assertEquals(add_check_digit('0095175385265'), '00951753852654')

    def test_add_check_digit_gtin8_string(self):
        self.assertEquals(add_check_digit('9879514'), '00000098795147')

    def test_add_check_digit_gtin8_number(self):
        self.assertEquals(add_check_digit(9879514), '00000098795147')

    def test_add_check_digit_gtin8_leading_zeros(self):
        self.assertEquals(add_check_digit('0000009879514'), '00000098795147')


if __name__ == '__main__':
    unittest.main()
