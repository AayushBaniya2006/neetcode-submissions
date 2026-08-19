class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
            return

        arr = [0] * len(nums1)

        self.mergeHelp(arr, nums1[:m], nums2)

        nums1[:] = arr

    def mergeHelp(self, arr, nums1, nums2):
        L = 0
        R = 0
        K = 0

        while L < len(nums1) and R < len(nums2):
            if nums1[L] <= nums2[R]:
                arr[K] = nums1[L]
                L += 1
            else:
                arr[K] = nums2[R]
                R += 1

            K += 1

        while L < len(nums1):
            arr[K] = nums1[L]
            L += 1
            K += 1

        while R < len(nums2):
            arr[K] = nums2[R]
            R += 1
            K += 1