# GTIN validation routines
# Copyright 2011 Charith Ellawala (charith@lucidelectricdreams.com)
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

def is_valid_GTIN(code):
  """ Validates any GTIN-8, GTIN-12, GTIN-13 or GTIN-14 code. """
  cleaned_code = _clean(code)

  return _is_valid_code(cleaned_code)


def _clean(code):
  if isinstance(code,(int,long)):
        return str(code).zfill(14)
  elif isinstance(code,basestring):
        return code.replace("-","").strip().zfill(14)
  else:
        raise TypeError("Expected string or integer type as input parameter")


def _is_valid_code(code):
  code_length = len(code)

  if not code.isdigit():
        return False
  elif not ((code_length == 8) or (code_length == 12) or (code_length == 13) or (code_length == 14) or (code_length == 18)):
        return False
  else:
        return _is_gtin_checksum_valid(code)


def _is_gtin_checksum_valid(code):
  code_length = len(code)
  total = 0

  for i in xrange(1,code_length):
        if i % 2 == 0:
          total = total + int(code[i-1])
        else:
          total = total + (3 * int(code[i-1]))

  check_digit = (10 - (total % 10)) % 10
  return int(code[code_length - 1]) == check_digit







