# scope_rules.py
# ONE outside variable. THREE functions. Three different behaviors.
# Run this as a script. The output is the proof.

# ===========================================
# OUTSIDE world. The "outside" owns balance.
# ===========================================
balance = 100


# ===========================================
# FUNCTION 1 — only READS balance
# ===========================================
def show():
    # No assignment to `balance` anywhere in this function.
    # → Function does NOT own `balance`.
    # → Python uses LEGB: looks outside, finds balance = 100.
    print(f"[show] balance = {balance}")


# ===========================================
# FUNCTION 2 — tries to MODIFY balance (broken)
# ===========================================
def add_broken(amount):
    # The line below assigns to `balance`.
    # → Function OWNS `balance` for its whole body.
    # → The right side `balance + amount` reads function's own balance.
    # → Function's balance is empty (never filled).
    # → CRASH: UnboundLocalError.
    balance = balance + amount
    print(f"[add_broken] balance = {balance}")


# ===========================================
# FUNCTION 3 — properly modifies outside's balance
# ===========================================
def add_fixed(amount):
    global balance              # explicit: function does NOT own balance
                                # outside owns it; reach across.
    balance = balance + amount  # reads outside's, writes outside's
    print(f"[add_fixed] balance = {balance}")


# ===========================================
# Run them and watch what happens.
# ===========================================

print(f"Start: outside balance = {balance}")

show()                          # works — reads outside's 100

add_fixed(50)                   # works — modifies outside's balance to 150

print(f"After add_fixed: outside balance = {balance}")

# add_broken(20)                # would crash; uncomment to see the error

print(f"End: outside balance = {balance}")

"""If the function assigns to a name anywhere in its body → LEGB does NOT walk for that name. 
The function owns it; only the local slot is checked.
If the function never assigns to that name → LEGB walks outward and finds the value from outside."""