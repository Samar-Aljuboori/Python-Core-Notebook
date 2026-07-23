# ==============================================================================
# PYTHON POLYMORPHISM 
# ==============================================================================
# Polymorphism allows different payment classes to share the same method name
# 'pay()', but each processes the transaction in its own unique way.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Base Class (Parent)
# ------------------------------------------------------------------------------
class PaymentMethod:
    def pay(self, amount):
        print(f"Processing generic payment of ${amount}")


# ------------------------------------------------------------------------------
# 2. Child Classes implementing different payment types
# ------------------------------------------------------------------------------
class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    # Polymorphic Method: Specific implementation for Credit Card
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]} ")


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    # Polymorphic Method: Specific implementation for PayPal
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal account ({self.email}) ")


class CashOnDelivery(PaymentMethod):
    # Polymorphic Method: Specific implementation for Cash
    def pay(self, amount):
        print(f"Order confirmed! You will pay ${amount} in cash upon delivery ")


# ------------------------------------------------------------------------------
# 3. Execution & Output (Polymorphism in Action)
# ------------------------------------------------------------------------------

# Creating payment objects
payment1 = CreditCard("4111222233334444")
payment2 = PayPal("samar@example.com")
payment3 = CashOnDelivery()

# Standard variable total amount
cart_total = 150

# --- Individual Calls ---
payment1.pay(cart_total)
# Output:
# Paid $150 using Credit Card ending in 4444 

payment2.pay(cart_total)
# Output:
# Paid $150 via PayPal account (samar@example.com) 

payment3.pay(cart_total)
# Output:
# Order confirmed! You will pay $150 in cash upon delivery 


# --- Loop Processing (True Polymorphism) ---
# A checkout system processing multiple orders without knowing their payment types
print("\n--- Processing Order Queue ---")

order_payments = [payment1, payment2, payment3]

for method in order_payments:
    method.pay(75)

# Output:
# --- Processing Order Queue ---
# Paid $75 using Credit Card ending in 4444 
# Paid $75 via PayPal account (samar@example.com) 
# Order confirmed! You will pay $75 in cash upon delivery 