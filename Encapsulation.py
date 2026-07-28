# ==============================================================================
# PYTHON ENCAPSULATION 
# ==============================================================================
# Encapsulation restricts direct access to an object's variables and methods
# to prevent accidental modification of data.
# 
# Access Modifiers in Python:
# 1. Public:      self.brand      (Accessible from anywhere)
# 2. Protected:   self._model      (Convention: Internal or child use only)
# 3. Private:     self.__battery   (Strictly hidden inside the class)
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Public vs Protected vs Private Attributes
# ------------------------------------------------------------------------------
class Device:
    def __init__(self, brand, model, battery):
        self.brand = brand          # Public property
        self._model = model        # Protected property (single underscore)
        self.__battery = battery    # Private property (double underscore)


# --- Execution & Output for Access Levels ---
my_device = Device("Apple", "iPhone 15", 80)

# Accessing Public Property
print(my_device.brand)
# Output:
# Apple

# Accessing Protected Property (Works, but discouraged outside class/subclasses)
print(my_device._model)
# Output:
# iPhone 15

# Accessing Private Property directly raises an AttributeError
try:
    print(my_device.__battery)
except AttributeError as e:
    print(f"Access Denied: {e}")
# Output:
# Access Denied: 'Device' object has no attribute '__battery'


# ------------------------------------------------------------------------------
# 2. Encapsulation using Getters & Setters (Safe Access)
# ------------------------------------------------------------------------------
class Phone:
    def __init__(self, brand, initial_battery=50):
        self.brand = brand
        self.__battery = initial_battery  # Private property to prevent direct tampering

    # Getter Method: Safely read the private battery percentage
    def get_battery(self):
        return f"{self.brand} Battery: {self.__battery}%"

    # Setter Method: Safely charge battery with validation logic
    def charge(self, amount):
        if amount <= 0:
            print("Error: Charge amount must be positive!")
        elif self.__battery + amount > 100:
            self.__battery = 100
            print("Battery fully charged to 100%!")
        else:
            self.__battery += amount
            print(f"Successfully charged +{amount}%")

    # Setter Method: Safely use battery with validation logic
    def use_phone(self, amount):
        if 0 < amount <= self.__battery:
            self.__battery -= amount
            print(f"Used phone for {amount}% battery.")
        else:
            print("Error: Not enough battery remaining or invalid amount!")


# --- Execution & Output for Getters & Setters ---
my_phone = Phone("Samsung", 50)

# Read battery via Getter
print(my_phone.get_battery())
# Output:
# Samsung Battery: 50%

# Valid Charge via Setter
my_phone.charge(30)
# Output:
# Successfully charged +30%

print(my_phone.get_battery())
# Output:
# Samsung Battery: 80%

# Invalid Usage Attempt (Validation Test)
my_phone.use_phone(90)
# Output:
# Error: Not enough battery remaining or invalid amount!

# Valid Usage
my_phone.use_phone(40)
# Output:
# Used phone for 40% battery.

print(my_phone.get_battery())
# Output:
# Samsung Battery: 40%

# Overcharging Test
my_phone.charge(80)
# Output:
# Battery fully charged to 100%!

print(my_phone.get_battery())
# Output:
# Samsung Battery: 100%