# GTIN validation routines
# Copyright 2011-2015 Charith Ellawala (charith@lucidelectricdreams.com)
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Validates GTIN (Global Trade Item Number) strings by calculating checksums.

Supports GTIN-8,GTIN-12,GTIN-13 and GTIN-14. Checksum calculation is done using
the method defined at http://www.gs1.org/barcodes/support/check_digit_calculator.

"""

import six

def is_valid_GTIN(code):
    """ Validates any GTIN-8, GTIN-12, GTIN-13 or GTIN-14 code. """
    cleaned_code = _clean(code)

    return _is_valid_code(cleaned_code)


def add_check_digit(code):
    """ Adds a check digit to the end of code. """
    cleaned_code = _clean(code).zfill(13)
    return cleaned_code + str(_gtin_checksum(cleaned_code))


def _clean(code, fill=14):
    if isinstance(code, six.integer_types):
        return str(code)
    elif isinstance(code, six.string_types):
        return code.replace("-", "").strip()
    else:
        raise TypeError("Expected string or integer type as input parameter")


def _is_valid_code(code):
    if not code.isdigit():
        return False
    elif len(code) not in (8, 12, 13, 14, 18):
        return False
    else:
        return _is_gtin_checksum_valid(code.zfill(14))


def _gtin_checksum(code):
    total = 0

    for (i, c) in enumerate(code):
        if i % 2 == 1:
            total = total + int(c)
        else:
            total = total + (3 * int(c))

    check_digit = (10 - (total % 10)) % 10
    return check_digit


def _is_gtin_checksum_valid(code):
    cleaned_code = code
    return int(code[-1]) == _gtin_checksum(code[:-1])
