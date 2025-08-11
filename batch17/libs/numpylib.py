import numpy as np

# Initialize the 8x8 matrix
arr = np.ones((8, 8), dtype=int)

# Function to set individual cell
def set_individual(row, col, val):
    arr[row][col] = val

# Function to set entire array to a number
def set_arr_to(num):
    global arr
    arr = np.full((8, 8), num, dtype=int)

# Function to set a column to a value
def set_col_to(col, val):
    arr[:, col] = val

# Function to set a row to a value
def set_row_to(row, val):
    arr[row, :] = val

# Function to count arrested terrorists
def count_arrests():
    return np.count_nonzero(arr == 0)

# Function to print the matrix
def print_arr():
    for row in arr:
        print("  ".join(map(str, row)))

# Main function logic
def main():
    set_arr_to(1)
    print("Each house in the matrix has a terrorist")
    print("--------------------------")
    print_arr()
    print("--------------------------")

    no_of_heli = int(input("Enter helicopter count: "))

    h = 0
    while h < no_of_heli:
        try:
            x, y = map(int, input(f"Enter coordinates (x, y) for helicopter {h + 1}: ").split())
            x -= 1
            y -= 1

            if 0 <= x < 8 and 0 <= y < 8:
                set_individual(x, y, 0)
                set_row_to(x, 0)
                set_col_to(y, 0)

                print("Indian army landnow....")
                print_arr()

                arrests = count_arrests()
                print(f"\n{arrests} terrorist have been arrested after helicopter {h + 1}.......")
                h += 1
            else:
                print("Invalid coordinates. Please enter coordinates within the matrix.")
        except ValueError:
            print("Invalid input. Please enter two integers.")

# Run the main function
if __name__ == "__main__":
    main()
