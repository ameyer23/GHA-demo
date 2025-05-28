"""Script for printing hello world"""

def hello_world(name: str = "Player") -> None:
    """
    Print a friendly greeting with the given name.

    Parameters:
        name (str): The name to include in the greeting. Defaults to "Player".

    Returns:
        None
    """
    print(f"Hello world, {name}!")  # Output the greeting with the provided name


if __name__ == "__main__":
    hello_world()  # Call the function with default name if script is run directly
