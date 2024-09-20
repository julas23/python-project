import os
import shutil

class Terminal:
    def __init__(self):
        self.current_directory = os.getcwd()
        print(f"Initialized in directory: {self.current_directory}")
    
    def list_files(self):
        print("Listing files and directories:")
        for item in os.listdir(self.current_directory):
            print(item)

    def create_directory(self, directory_name):
        new_dir_path = os.path.join(self.current_directory, directory_name)
        try:
            os.mkdir(new_dir_path)
            print(f"Directory '{directory_name}' created.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
    
    def rename_directory(self, old_name, new_name):
        old_dir_path = os.path.join(self.current_directory, old_name)
        new_dir_path = os.path.join(self.current_directory, new_name)
        try:
            os.rename(old_dir_path, new_dir_path)
            print(f"Directory renamed from '{old_name}' to '{new_name}'.")
        except FileNotFoundError:
            print(f"Directory '{old_name}' not found.")
    
    def remove_directory(self, directory_name):
        dir_path = os.path.join(self.current_directory, directory_name)
        try:
            shutil.rmtree(dir_path)
            print(f"Directory '{directory_name}' removed.")
        except FileNotFoundError:
            print(f"Directory '{directory_name}' not found.")
        except OSError as e:
            print(f"Error removing directory '{directory_name}': {e}")

class Environment:
    def __init__(self, variable_name):
        self.variable_name = variable_name
        self.value = os.getenv(variable_name)
        print(f"Environment variable '{variable_name}' initialized with value: {self.value}")
    
    def get_variable(self):
        value = os.getenv(self.variable_name)
        print(f"Value of '{self.variable_name}': {value}")
        return value
    
    def set_variable(self, value):
        os.environ[self.variable_name] = value
        print(f"Set '{self.variable_name}' to '{value}'")

def main():
    directory_name = input("Enter the name of the directory to create: ")
    
    terminal = Terminal()
    
    terminal.list_files()
    
    terminal.create_directory(directory_name)
    
    renamed_directory = input(f"Enter the new name for the directory '{directory_name}': ")
    terminal.rename_directory(directory_name, renamed_directory)
    
    terminal.remove_directory(renamed_directory)
    
    variable_name = input("Enter the name of the environment variable: ")
    
    environment = Environment(variable_name)
    
    environment.get_variable()
    
    new_value = input(f"Enter the new value for the environment variable '{variable_name}': ")
    environment.set_variable(new_value)
    
    environment.get_variable()

if __name__ == "__main__":
    main()
