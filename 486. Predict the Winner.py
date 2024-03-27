# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 03:09:31 2023


You are given an integer array nums. Two players are playing a game with this array: player 1 and
 player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with 
a score of 0. At each turn, the player takes one of the numbers from either end of the array 
(i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. 
he player adds the chosen number to their score. The game ends when there are no more elements in
 the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still
 the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

@author: IlYA
"""

nums = [1,5,233,5, 33,7]
#nums = [1,6,3]


def PredictTheWinner(nums) -> bool:
        n = len(nums)
        # Create a two-dimensional array to store the optimal score differences.
        dp = [[0] * n for _ in range(n)]

        # Fill in the values for subarrays of length 1.
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill in the values for subarrays of larger length.
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                choose_left = nums[i] - dp[i + 1][j]
                choose_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(choose_left, choose_right)
                print(str(i)+'--'+str(j))
                print(choose_left)
                print(choose_right)
                print(dp)
                print('--------------')
        # Player 1 wins if their optimal score difference is non-negative.
        return dp[0][n - 1] >= 0

print(PredictTheWinner(nums))

# Solution with recursion 

def PredictTheWinner(nums):
    """
    Determine if Player 1 can win the game with the given integer array.

    Args:
        nums (List[int]): The input integer array.

    Returns:
        bool: True if Player 1 can win the game, False otherwise.
    """
    memo = {}
    player1_score = recursive_score(nums, 0, len(nums) - 1, memo)
    return player1_score >= 0

def recursive_score(nums, left, right, memo):
    """
    Recursively calculates the optimal score difference for Player 1 starting with the given subarray.

    Args:
        nums (List[int]): The input integer array.
        left (int): The left index of the subarray.
        right (int): The right index of the subarray.
        memo (dict): The memoization dictionary to store previously computed results.

    Returns:
        int: The optimal score difference for Player 1.
    """
    #print(str(left)+'--'+str(right))
    if left == right:
    
        return nums[left]

    if (left, right) in memo:
        
        return memo[(left, right)]

    
    choose_left = nums[left] - recursive_score(nums, left + 1, right, memo)
        
    choose_right = nums[right] - recursive_score(nums, left, right - 1, memo)
    
    memo[(left, right)] = max(choose_left, choose_right)
    
    
    return memo[(left, right)]


print(PredictTheWinner(nums))
