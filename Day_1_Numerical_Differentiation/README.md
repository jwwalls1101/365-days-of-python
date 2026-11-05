# Day 1 - Numerical Differentiation

## Objective:
Develop a Python program to approximate the first derivative of a function using numerical methods.

## Methods:
Two finite-difference methods were implemented:

Forward Difference:
$$f'(x) \approx \frac{f(x+h)+f(x)}{h}$$

Central Difference:
$$f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$$

## Implementation
The program uses Python functions to approximate derivatives and compare them against their analytical solution. 

It evaluates 100 logarithmically spaced step sizes between $$10^{-1}$$ and $$10^{-12}$$ and identifies the step sizes that produce the smallest absolute error.

## Results
Central Difference produces more accurate approximations than Forward Difference because it has second-order truncation error. Both methods experience increased floating-point roundoff error at very small step sizes.

## Takeaway
Decreasing the step size does not always improve numerical accuracy because floating-point roundoff error eventually dominates truncation error.
