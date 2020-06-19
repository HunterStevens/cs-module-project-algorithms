'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    final = []
    for l in range(len(nums)-k+1):
        window = nums[l:l+k]
        large = window[0]
        for i in window:
            if i > large:
                large = i   
        
        
        ''' 
        large= nums[l]
        for i in range(1,k):
            if nums[l+i] > large:
                large = nums[l+i]
        '''

        final.append(large)
    
    return final

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
