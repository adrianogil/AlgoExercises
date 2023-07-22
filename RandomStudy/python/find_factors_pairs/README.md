# Programming Challenge: Factor Pair Finder

## Problem

You are given a list of positive integers and a single target value, also a positive integer. Your task is to write a function that finds pairs of integers in the list which multiply together to give the target value.

Your function should have the following signature:

```python
def find_factor_pairs(number_list, target):
```

where:

- `number_list` is a list of positive integers. The length of `number_list` will be between 1 and 1000, and each integer will be between 1 and 10^6.
- `target` is a positive integer and is between 1 and 10^12.

Your function should return a list of tuples, where each tuple contains two factors from the `number_list` that multiply together to form the `target`. Each tuple should be ordered in the same order the factors appear in the `number_list`.

For example:

```python
find_factor_pairs([2, 4, 6, 8, 16], 32)
```

should return:

`[(2, 16), (4, 8)]`

since 2,16 and 4,8 both equal to 32. Please note that your function should not return duplicate pairs. If no pairs of factors are found, your function should return an empty list.