# ==============================================================================
#  PYTHON INHERITANCE 
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Parent Class Definition
# ------------------------------------------------------------------------------
class Haus:
    def __init__(self, color, area, address):
        self.color = color
        self.area = area
        self.address = address

    def about(self):
        print(f"Haus Info -> Color: {self.color}, Area: {self.area}m², Address: {self.address}")


# --- Execution & Output for Parent Class ---
infoHaus1 = Haus("White", 100, "Stuttgart")
infoHaus1.about()
# Output:
# Haus Info -> Color: White, Area: 100m², Address: Stuttgart


# ------------------------------------------------------------------------------
# 2. Child Class with 'pass' (Simple Inheritance)
# ------------------------------------------------------------------------------
class BigHaus(Haus):
    pass


# --- Execution & Output for Child Class with 'pass' ---
infoBig = BigHaus("Blue", 250, "Munich")
infoBig.about()
# Output:
# Haus Info -> Color: Blue, Area: 250m², Address: Munich


# ------------------------------------------------------------------------------
# 3. Child Class using super(), New Properties & Method Overriding
# ------------------------------------------------------------------------------
class SmallHaus(Haus):
    def __init__(self, color, area, address, windows):
        super().__init__(color, area, address)
        self.windows = windows

    def about(self):
        print(f"Small Haus -> Color: {self.color}, Windows: {self.windows}, Address: {self.address}")

    def show_windows(self):
        print(f"Number of windows: {self.windows}")


# --- Execution & Output for SmallHaus ---
infoHaus2 = SmallHaus("Black", 99, "Hamburg", "Three")

# Calling overridden method
infoHaus2.about()
# Output:
# Small Haus -> Color: Black, Windows: Three, Address: Hamburg

# Accessing property directly
print(infoHaus2.windows)
# Output:
# Three

# Calling child-specific method
infoHaus2.show_windows()
# Output:
# Number of windows: Three


# ------------------------------------------------------------------------------
# 4. Multiple Inheritance (Inheriting from Two Parent Classes)
# ------------------------------------------------------------------------------
class EnergyRating:
    def __init__(self, rating):
        self.rating = rating

    def get_energy(self):
        print(f"Energy Efficiency Rating: {self.rating}")


class EcoHaus(SmallHaus, EnergyRating):
    def __init__(self, color, area, address, windows, rating, solar_panels):
        SmallHaus.__init__(self, color, area, address, windows)
        EnergyRating.__init__(self, rating)
        self.solar_panels = solar_panels


# --- Execution & Output for Multiple Inheritance ---
eco1 = EcoHaus("Green", 110, "Berlin", "Four", "A+++", 6)

eco1.about()
# Output:
# Small Haus -> Color: Green, Windows: Four, Address: Berlin

eco1.get_energy()
# Output:
# Energy Efficiency Rating: A+++

print(f"Solar Panels: {eco1.solar_panels}")
# Output:
# Solar Panels: 6