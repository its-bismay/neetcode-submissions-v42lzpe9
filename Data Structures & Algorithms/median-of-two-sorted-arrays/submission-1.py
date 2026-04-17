class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        
        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1

        while True:
            idxa = l + ((r - l) // 2)
            idxb = half - (idxa + 1) - 1

            a_left = a[idxa] if idxa >= 0 else float("-infinity")
            a_right = a[idxa + 1] if idxa + 1 < len(a) else float("infinity")

            b_left = b[idxb] if idxb >= 0 else float("-infinity")
            b_right = b[idxb + 1] if idxb + 1 < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = idxa - 1
            else:
                l = idxa + 1

        