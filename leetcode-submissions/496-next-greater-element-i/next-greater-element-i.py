class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st = []
        hashMap = {}
        for i in range(n-1, -1, -1):
            while len(st) > 0 and st[-1] <= nums2[i]:
                st.pop()
            if len(st) == 0:
                hashMap[nums2[i]] = -1
            else:
                hashMap[nums2[i]] = st[-1]
            st.append(nums2[i])
        
        return list(map(lambda x: hashMap[x], nums1))

        