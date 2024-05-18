class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        pref = energy[:k] + [0] * (len(energy) - k)
        # print(pref)
        for i in range(k, len(energy)):
            pref[i] = max(energy[i], energy[i] + pref[i - k])
        # print(pref)
        # print(pref[-k-1:])
        return max(pref[-k:])
