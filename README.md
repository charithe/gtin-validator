GTIN Validator
==============

Validates GTIN (Global Trade Item Number) codes by calculating checksums.

GTIN comprises of GTIN-8, GTIN-12, GTIN-13 and GTIN-14 codes. EAN, UPC and ISBN can be thought of as subsets of GTIN. For more information, see: http://www.gs1.org/barcodes/technical/idkeys/gtin  and  http://en.wikipedia.org/wiki/Global_Trade_Item_Number

Usage
-----

The module exports a single function `is_valid_GTIN` - which accepts either string or integer arguments. Dashes in the code (commonly found in ISBN numbers) are supported. 

```python
from gtin_validator import *

if __name__ == '__main__':
    print is_valid_GTIN("9780552133265")
    print is_valid_GTIN("978-0-552-13326-5")
    print is_valid_GTIN(9780552133265)
```

