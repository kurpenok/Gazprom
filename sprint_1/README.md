### Sprint 1

#### Ideas for the first task:
- From the limitations on the 10^9 number of operations, an estimate for the linearity of this algorithm follows, since C++ performs approximately 10^9 operations per second (`We don't write in C++, but who writes restrictions for Python?`).
- The task would not be solved in one pass, since an assessment from two sides is needed.
- Hence the conclusion that it is necessary to implement an algorithm of oncoming traffic.

#### Ideas for the second task:
- There are no serious restrictions as such, but it is rather boring and inefficient to solve by brute force.
- For time optimization, we will use HashMap, since the order of the digits is not important to us anyway (which may initially confuse).
- Let's add a condition for clicking to solve the problem.

#### Notes to the code
- Always use type hints.
- If possible, use Python's built-in functions more often, since they are implemented in C and work noticeably faster.
- A good I/O is a satisfied user (if he is not a machine).
- It would be possible to write comments, but I'm a little lazy + there is a readme with a description of the algorithm of work.
