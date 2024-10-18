class Solution:
	def countPairs(self, nums: List[int]) -> int:

		result = 0

		for i in range(len(nums) - 1):

			for j in range(i + 1 , len(nums)):

				n1 = str(nums[i])
				n2 = str(nums[j])

				if len(n1) < len(n2):

					n1 = '0' * (len(n2) - len(n1)) + n1

				if len(n1) > len(n2):

					n2 = '0' * (len(n1) - len(n2)) + n2

				count = 0

				for index in range(len(n2)):

					if n1[index] != n2[index]:
						count = count + 1

				if count <= 2 and Counter(n1) == Counter(n2):

					result = result + 1

		return result