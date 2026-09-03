import time
from functools import wraps

total_balance = 0
transaction_count = 0

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


count = make_counter()


def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished -> result={result}")
        return result
    return wrapper


def require_positive_amount(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        amount = kwargs.get("amount", args[0] if args else None)
        if amount is None or amount <= 0:
            print(f"[ERROR] {func.__name__} blocked, amount must be positive, got {amount}")
            return None
        return func(*args, **kwargs)
    return wrapper


def track_calls(func):
    call_count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        wrapper.call_count = call_count
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


@track_calls
@log_transaction
@require_positive_amount
def deposit(amount):
    global total_balance, transaction_count
    total_balance += amount
    transaction_count = count()
    return total_balance


@track_calls
@log_transaction
@require_positive_amount
def withdraw(amount):
    global total_balance, transaction_count
    total_balance -= amount
    transaction_count = count()
    return total_balance


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        time_takes = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} took {time_takes:.6f}s")
        return res
    return wrapper


@timer
@log_transaction
@require_positive_amount
def sample_transaction_a(amount):
    return amount


@require_positive_amount
@log_transaction
@timer
def sample_transaction_b(amount):
    return amount


if __name__ == "__main__":
    print("--- decorator order demo ---")
    sample_transaction_a(100)
    sample_transaction_a(-50)
    sample_transaction_b(100)
    sample_transaction_b(-50)

    print("\n--- transactions ---")
    deposit(500)
    withdraw(200)
    deposit(-100)
    withdraw(1000)
    deposit(50)
    withdraw(-25)

    print("\n--- final report ---")
    print(f"Final total_balance: {total_balance}")
    print(f"Total transaction count: {transaction_count}")
    print(f"deposit() called {deposit.call_count} times")
    print(f"withdraw() called {withdraw.call_count} times")
