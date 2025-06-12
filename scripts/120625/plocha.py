import sys

def calculate_area(length, width):
    return length * width

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ahoj.py <length> <width>")
        sys.exit(1)
    
    try:
        length = float(sys.argv[1])
        width = float(sys.argv[2])
        area = calculate_area(length, width)
        print(f"The area of the object is: {area}")
    except ValueError:
        print("Please provide valid numeric values for length and width.")
        sys.exit(1)
