class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def f(curr):
            for i in range(10):
                number = curr + str(i)
                number_int = int(number)
                if number_int <= n:
                    if number[0] != "0":
                        res.append(number_int)
                        f(number)
                else:
                    break

        f("")
        return res
