'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# *** Original answer ***
# def sliding_window_max(nums, k):
#     new_arr = []
#     for i in range(0, len(nums) - k + 1):
#         max = nums[i]
#         for j in nums[i:i+k]:
#             if j > max:
#                 max = j
#         new_arr.append(max)
#     return new_arr

# *** using max() time is less than half ***
# def sliding_window_max(nums, k):
#     new_arr = []
#     for i in range(0, len(nums) - k + 1):
#         new_arr.append(max(nums[i:i+k]))
#     return new_arr

def sliding_window_max(nums, k):
    # set up array that will be used as queue
    q = []
    # set up array that will be returned at the end of the function
    answer = []

    # create the value in q for the first window
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    
    # iterate through nums for later windows
    for i in range(k, len(nums)):
        # append value for previous window to answer
        answer.append(nums[q[0]])
        while q and q[0] <= i - k:
            q.pop(0)
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    
    answer.append(nums[q[0]])
    
    return answer




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
