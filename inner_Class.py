# ==============================================================================
# PYTHON INNER / NESTED CLASSES 
# ==============================================================================
# An Inner Class is a class created inside another class.
# It is used to group classes that logically belong together.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Basic Inner Class Definition
# ------------------------------------------------------------------------------
class Phone:
    def __init__(self, brand):
        self.brand = brand

    # Inner Class representing a SIM Card
    class SIM:
        def __init__(self, carrier):
            self.carrier = carrier

        def show_network(self):
            print(f"Network connected to {self.carrier} ")


# --- Execution & Output for Manual Inner Class Instantiation ---
my_phone = Phone("iPhone 15")

# Creating an instance of the Inner Class using the Outer Class instance
my_sim = my_phone.SIM("Vodafone")
my_sim.show_network()
# Output:
# Network connected to Vodafone 


# ------------------------------------------------------------------------------
# 2. Advanced Inner Class (Automatic Internal Instantiation)
# ------------------------------------------------------------------------------
class Computer:
    def __init__(self, brand, cpu_name, cpu_cores):
        self.brand = brand
        # Instantiating the Inner Class directly inside the Outer Class __init__
        self.cpu = self.CPU(cpu_name, cpu_cores)

    def show_specs(self):
        print(f"Computer Brand: {self.brand}")

    # Inner Class representing the Processor
    class CPU:
        def __init__(self, name, cores):
            self.name = name
            self.cores = cores

        def display_cpu_info(self):
            print(f"Processor: {self.name} with {self.cores} Cores")


# --- Execution & Output for Automatic Inner Class Instantiation ---
my_laptop = Computer("Apple", "M3 Max", 16)

# Display Outer Class info
my_laptop.show_specs()
# Output:
# Computer Brand: Apple

# Access Inner Class method directly through the Outer Class attribute
my_laptop.cpu.display_cpu_info()
# Output:
# Processor: M3 Max with 16 Cores 