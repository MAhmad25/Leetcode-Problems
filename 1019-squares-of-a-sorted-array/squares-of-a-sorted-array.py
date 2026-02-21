class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # First we have to split the array into positive and negative
        postive = []
        negative = []
        # Splitting the array
        for value in nums:
            # Positive Element Insertion
            if value >= 0:
                postive.append(value)
            # Negative Element Insertion
            else:
                negative.append(value)

        # Edge Case checking
        # Checking if positive array is emtpy then the element in nums(main) are only negative
        # array is only negative just take the square and reverse the array and return it
        if len(postive) == 0:
            point = 0
            while point <= len(nums) - 1:
                nums[point] = nums[point] * nums[point]
                point = point + 1
            nums.reverse()
            return nums
        # Checking if negative array is emtpy then the element in nums(main) are only positve
        # array is only postive just take the square  and return it
        if len(negative) == 0:
            point = 0
            while point <= len(nums) - 1:
                nums[point] = nums[point] * nums[point]
                point = point + 1
            return nums

        # Now above all edge case are handled now we have to merge the two arrays
        # with square and negative being reversed
        # Merging the array
        for index in range(len(postive)):
            postive[index] = postive[index] * postive[index]
        for index in range(len(negative)):
            negative[index] = negative[index] * negative[index]

        negative.reverse()
        p = len(postive)
        n = len(negative)
        p1, n1 = 0, 0
        res = []
        while p1 < p and n1 < n:
            if postive[p1] < negative[n1]:
                res.append(postive[p1])
                p1 = p1 + 1
            else:
                res.append(negative[n1])
                n1 = n1 + 1
            #     Handling if pointer in postitve and negative is out of the array and one array is still have element
        while p1 < p:
            res.append(postive[p1])
            p1 = p1 + 1
        while n1 < n:
            res.append(negative[n1])
            n1 = n1 + 1

        return res
