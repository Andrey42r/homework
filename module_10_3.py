from threading import Lock, Thread


class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()


def deposit_task(account, amount):
    for i in range(5):
        with account.lock:
            account.balance += amount
            print(f'Deposited {amount}, new balance is {account.balance}')


def withdraw_task(account, amount):
    for i in range(5):
        with account.lock:
            if account.balance >= amount:
                account.balance -= amount
                print(f'Withdrew {amount}, new balance is {account.balance}')


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
