import os

# writing a python program to print the contents of the directory 
# using a os module . 

def print_directory_contents(directory):
    """
    This function prints the contents of the specified directory.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        print(item)

# Example usage:
# selecting which we want to print 

directory_path = 'C:\\Users\\divya\\OneDrive\\Desktop\\Language\\python\\chapter 1 basic and modules'  # Replace with your directory path

# giving value in the function which will print the items 
print_directory_contents(directory_path)
