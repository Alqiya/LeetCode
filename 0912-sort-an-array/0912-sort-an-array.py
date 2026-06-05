class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #using merge sort

        def merge(arr, L, M, R):
            #separating the two arrays into left and right part
            left, right = arr[L:M+1], arr[M+1:R+1]
            
            # i is for the main array
            # j and k is for left and right subarray respectively
            i, j, k = L, 0, 0

            #this merging is similar to the problem 'merge a sorted array' (topics:-two pointers)
            
            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1

            while j<len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            
            while k<len(right):
                arr[i] = right[k]
                k+=1
                i+=1


        def mergeSort(arr, l, r):
            if l>=r:
                return
            
            #Divide by recursion
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)

            #conquer using merge
            merge(arr, l, mid, r)

        mergeSort(nums, 0, len(nums)-1)
        return nums