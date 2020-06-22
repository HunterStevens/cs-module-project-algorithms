'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque
def sliding_window_max(nums, k):
    # Your code here
    
    final = []
    window = deque()


    for l, n in enumerate(nums):
        while len(window) > 0 and n > window[-1]:
            window.pop()
            
        window.append(n)
        len_wind = l - k + 1
        if len_wind >= 0:
            final.append(window[0])

            if nums[len_wind] == window[0]:
                window.popleft()
            
        '''
        for i in window:
            if i > large:
                large = i   
        '''
        ''' 
        large= nums[l]
        for i in range(1,k):
            if nums[l+i] > large:
                large = nums[l+i]
        '''
        # window.clear()
        # final.append(large)
    
    return final

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
