class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, mid = len(nums1) + len(nums2), (len(nums1) + len(nums2)) // 2        
        #Do odd/even check here instead of kth. loose coupled design.
        if l % 2 == 1:
            return self.kthMin(nums1,nums2, mid)        
        else:
            return 0.5 * (self.kthMin(nums1,nums2, mid) + self.kthMin(nums1,nums2, mid - 1))
        

    def kthMin(self, a: List[int], b: List[int], k:int) -> float:
        if not a:
            return b[k]
        if not b:
            return a[k]
        
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]


        if ia + ib < k:
            # whole bigger list, and bigger half of smaller list.
            if ma > mb:
                return self.kth(a, b[ib+1:], k - ib -1)
            else:
                return self.kth(a[ia+1:], b, k - ia -1)
        else:        
            # whole smaller list, and smaller half of bigger list   
            if ma > mb:
                return self.kth(a[:ia], b, k) 
            else:
                return self.kth(a, b[:ib], k) 

