author = Artur Tarassow
email = atecon@posteo.de
version = 0.5
date = 2019-12-29
description = Assert functions for verifying expectations and values in gretl tests
tags = C81
min-version = 2018a
data-requirement = no-data-ok
public = assertIsType assertIsNotType assertTrue assertFalse \
  assertEqualStr assertNotEqualStr assertEqualNum assertNotEqualNum \
  assertGreaterEqualNum assertLessEqualNum assertAlmostEqualNum \
  assertNotAlmostEqualNum
help = assertion_help.txt
sample-script = assertion_sample.inp
depends = string_utils extra
