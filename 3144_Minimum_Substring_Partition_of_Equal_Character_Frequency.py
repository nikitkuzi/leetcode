class Solution:
    def minimumSubstringsInPartition(self, s):
        # Initialize an array to store the maximum frequency of each character
        max_frequency = [0] * 26
        for char in s:
            max_frequency[ord(char) - ord('a')] += 1

        # dp[i] represents the minimum number of partitions needed for the first i characters
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0  # Base case: no characters, no partitions needed

        for i in range(1, len(s) + 1):
            freq = [0] * 26
            max_in_window = 0

            # Check all substrings that end at position i
            for j in range(i, 0, -1):
                index = ord(s[j - 1]) - ord('a')
                freq[index] += 1
                max_in_window = max(max_in_window, freq[index])

                # Check if the current window can form a balanced substring
                valid = True
                for k in range(26):
                    if freq[k] > 0 and freq[k] < max_in_window:
                        valid = False
                        break

                if valid:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[len(s)]