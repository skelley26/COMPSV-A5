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
- Best-case: O(n^2) 
- Worst-case: O(n!)
- Average-case: O(n^2)
- Space complexity: O(n) because it's counting the values in the list and creating a set.
- Why this approach? Because a set is usually used in cases of finding duplicates. 
- Could it be optimized? Yes, I looked it up and stack overflow said to use: return max(set(lst), key=lst.count) but I am not entirely sure why that works.
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

remove_duplicates([4, 5, 4, 6, 5, 7])

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(2^n)
- Average-case: O(log n)
- Space complexity: O(n)
- Why this approach? makes a dict for the list, then turns it back into a list, instead of keeping the duplicate list from above, which would be an extra loop.
- Could it be optimized? With fromkeys being used, I think it is already optomized.
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
- Best-case: O(n)
- Worst-case: O(n^2)
- Space complexity: O(n)
- Why this approach? Using combinations, I can get ordered pairs, only if the sum of said pair == the target. The code is abreviated so it doesn't take up several lines. 
- Could it be optimized? It might be able to be optimized, especially if there is a database full of values to go over. 
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
    for i in range(n):
        items.append(i)
        print(items)
#add_n_items(6)

#items =v [1, 2, 3, 4] * n
#Used this and it basically printed what was already in the list n times (so 6 times in this case.)
"""
Time and Space Analysis for problem 4:
- When do resizes happen? When python runs out of space. It usually doubles but, here, i set it to 6 like the example.
- What is the worst-case for a single append? O(n)
- What is the amortized time per append overall? O(1)
- Space complexity: O(1)
- Why does doubling reduce the cost overall? Because they only have one step. 
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
    total = [sum(nums[:i+1]) for i in range(len(nums))]
    print(total)
    
#running_total([1, 2, 3, 4])

# nums[:i+1] is iterating through the list one by one, sourced by nums
# range = however many numbers are in nums (given by length of nums) 

"""
Time and Space Analysis for problem 5:
- Best-case: O(n^2)
- Worst-case: O(n^2)
- Average-case: O(n^2)
- Space complexity: O(n)
- Why this approach? It's more compact to use, loops through the list once because of the for. Stores it in a new list as well. 
- Could it be optimized? Yes, we could optimize the time complexity with an operator like +=
"""


# https://www.geeksforgeeks.org/python/how-to-find-duplicates-in-a-list-python/
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# https://www.geeksforgeeks.org/python/python-program-to-find-all-possible-pairs-with-given-sum/
# https://www.geeksforgeeks.org/python/python-program-to-find-cumulative-sum-of-a-list/
# https://stackoverflow.com/questions/311775/create-a-list-with-initial-capacity-in-python