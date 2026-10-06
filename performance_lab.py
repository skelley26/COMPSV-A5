from itertools import combinations

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    duplicates = [i for i in set(numbers) if numbers.count(i) > 1]
    print(duplicates)
    
#most_frequent([1, 3, 2, 3, 4, 1, 3])

# Started with what I know, but i found that on GeeksforGeeks, there is an even more efficient way to write it.
#     s = set()
#     duplicates = []
#     for i in numbers:
#         if i in s:
#             duplicates.append(i)
#         else:
#             s.add(i)
#     print(duplicates)

 
        
    

"""
Time and Space Analysis for problem 1:
- Best-case: It loops once through the dataset and quickly spits out the duplicates
- Worst-case: Loops several times over the dataset and takes forever to spit out the duplicates
- Average-case: Loops, sorts the duplicates into a set and the rest of the numbers in a list.
- Space complexity: O[1] because it's counting the values in the list and creating a set.
- Why this approach? 
- Could it be optimized? I imagine it could be since it has to loop through each item on the list.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    nums = list(dict.fromkeys(nums))
    print(nums)

#remove_duplicates([4, 5, 4, 6, 5, 7])

"""
Time and Space Analysis for problem 2:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity: 
- Why this approach? makes a dict for the list, then turns it back into a list, instead of keeping the duplicate list from above, which would be an extra loop.
- Could it be optimized?
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
  return[pair for pair in combinations(nums, 2) if sum(pair) == target]

nums = [1, 2, 3, 4]
target = 5
#print(find_pairs(nums, target))
        
    
    
    
    

"""
Time and Space Analysis for problem 3:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    items = []
    for i in range(5):
        items.append(n)
add_n_items(6)
"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    nums = []
    total = sum(nums)

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


# https://www.geeksforgeeks.org/python/how-to-find-duplicates-in-a-list-python/
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# https://www.geeksforgeeks.org/python/python-program-to-find-all-possible-pairs-with-given-sum/