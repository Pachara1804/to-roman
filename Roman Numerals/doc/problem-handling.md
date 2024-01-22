# Handle problems.

## the number is out-of-range
0
-1

### Approaches to hander
#### Output something indicating problems.
##### Output choices
1. ""
2. "Out-of-range"
3. None

#### raise exception
##### exception choices
1. Standard exceptin: (ValueError)
2. (*)Extention of standard exception:
    NumberOutOfRange : ValueError
3. Project-specific exception
    NumberOutOfRange : Exception