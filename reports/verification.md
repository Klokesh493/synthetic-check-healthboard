# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 synthetic_healthboard.py sample_checks.csv
checkout
test_flags_low_pass_rate (test_synthetic_healthboard.SyntheticHealthboardTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
