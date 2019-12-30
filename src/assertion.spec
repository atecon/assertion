author = Artur Tarassow
email = atecon@posteo.de
version = 0.5
date = 2019-12-30
description = Assert functions for verifying expectations and values in gretl tests
tags = C81
min-version = 2018a
data-requirement = no-data-ok
public = assert_is_type assert_is_not_type assert_true assert_false \
  assert_equal_str assert_not_equal_str assert_equal_num assert_not_equal_num \
  assert_greater_equal_num assert_less_equal_num assert_almost_equal_num \
  assert_not_almost_equal_num
help = assertion_help.txt
sample-script = assertion_sample.inp
depends = string_utils extra
