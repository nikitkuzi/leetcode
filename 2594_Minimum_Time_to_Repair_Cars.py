# class Solution:
#     def repairCars(self, ranks: List[int], cars: int) -> int:
#         # The minimum possible time is 1,
#         # and the maximum possible time is when the slowest mechanic (highest rank) repairs all cars.
#         low, high = 1, cars * cars * ranks[0]

#         # Perform binary search to find the minimum time required.
#         while low < high:
#             mid = (low + high) // 2
#             cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

#             # If the total cars repaired is less than required, increase the time.
#             if cars_repaired < cars:
#                 low = mid + 1
#             else:
#                 high = mid  # Otherwise, try a smaller time.

#         return low
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # The minimum possible time is 1,
        # and the maximum possible time is when the slowest mechanic (highest rank) repairs all cars.
        low, high = 1, cars * cars * ranks[0]

        # Perform binary search to find the minimum time required.
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            # If the total cars repaired is less than required, increase the time.
            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid  # Otherwise, try a smaller time.

        return low