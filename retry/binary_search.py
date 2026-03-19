class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # print(
            #     f"mid: {mid}, left: {l}, right: {r}, current: {nums[mid]}, target: {target}"
            # )
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4

    question = Solution()
    print(question.search(nums, target))
