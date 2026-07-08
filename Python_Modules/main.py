# 1. Import the entire module professionally
import geometry_helper

# 2. Import a specific function directly from the module
from geometry_helper import calculate_rectangle_area

def run_application():
    # Print the welcome message from the module
    print(geometry_helper.welcome_message())
    print("-" * 40)

    # Using the first method: module_name.function_or_variable
    r = 5
    circle_area = geometry_helper.calculate_circle_area(r)
    print(f"The area of a circle with radius {r} is: {circle_area:.2f}")
    print(f"Value of PI used from module: {geometry_helper.PI}")
    
    print("-" * 40)

    # Using the second method: calling the imported function directly without module name
    l, w = 10, 4
    rect_area = calculate_rectangle_area(l, w)
    print(f"The area of a rectangle ({l}x{w}) is: {rect_area}")

if __name__ == "__main__":
    run_application()