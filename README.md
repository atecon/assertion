The "assertion" package
--

[![Build Status](https://travis-ci.org/atecon/assertion.svg?branch=master)](https://travis-ci.org/atecon/assertion)


Collection of assert-functions for writing (unit-)test cases and to detect test failure. Assert is a method useful in determining Pass or Fail status of a test case.

Please ask questions and report bugs on the gretl mailing list if possible -- otherwise here on github.com.

Currently, the most standard methods are supported:

1) assert_equal_num()
2) assert_not_equal_num()
3) assert_greater_equal_num()
4) assert_less_equal_num()
5) assert_almost_equal_num()
6) assert_not_almost_equal_num()
7) assert_equal_str()
8) assert_not_equal_str()
9) assert_true()
10) assert_false()
11) assert_is_type()
12) assert_is_not_type()

For details see the [help file](src/assertion_help.txt).

Install and load the package
--
```hansl
pkg install assertion
include assertion.gfn
```
