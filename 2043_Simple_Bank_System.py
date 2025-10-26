class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def check(self, a1: int, a2: int = 1) -> bool:
        return not (a1 <= 0 or a2 <= 0 or a1 > len(self.balance) or a2 > len(self.balance))

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.check(account1, account2) or self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.check(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check(account) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)