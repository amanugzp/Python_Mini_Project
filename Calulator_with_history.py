import re
import math
from datetime import datetime

HISTORY_FILE = "history.txt"

# Input Normalization
def normalize_input(expression):
    return re.sub(r'([+\-*/^%()])', r' \1 ', expression)

# Show history with latest entry first
def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found.")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")

# Clear history file
def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print("History cleared.")

# Save history with timestamp
def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {equation} = {result}\n")

# Export history to another file
def export_history(filename):
    try:
        with open(HISTORY_FILE, 'r') as src, open(filename, 'w') as dest:
            dest.write(src.read())
        print(f"History exported to {filename}")
    except Exception as e:
        print(f"Export failed: {e}")

# Import history from a file
def import_history(filename):
    try:
        with open(filename, 'r') as src, open(HISTORY_FILE, 'a') as dest:
            dest.write(src.read())
        print(f"History imported from {filename}")
    except Exception as e:
        print(f"Import failed: {e}")

# Evaluate mathematical expression
def evaluate(expression):
    expression = normalize_input(expression)
    tokens = expression.split()

    try:
        # Handling custom operators
        if len(tokens) == 2 and tokens[0] == "sqrt":
            result = math.sqrt(float(tokens[1]))
        elif len(tokens) == 2 and tokens[0] in ("sin", "cos", "log"):
            num = float(tokens[1])
            if tokens[0] == "sin":
                result = math.sin(math.radians(num))
            elif tokens[0] == "cos":
                result = math.cos(math.radians(num))
            elif tokens[0] == "log":
                result = math.log10(num)
        else:
            # Safe eval for basic math expressions
            expression = expression.replace("^", "**")
            result = eval(expression)
        
        result = int(result) if isinstance(result, float) and result.is_integer() else result
        print("Result:", result)
        save_to_history(expression.strip(), result)
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Error: Invalid number format.")
    except Exception as e:
        print(f"Error: {e}")

# Command loop
def main():
    print("----- ENHANCED CALCULATOR -----")
    print("Commands: history | clear | exit | export <file> | import <file>")
    print("Supports: + - * / ^ %, sqrt, sin, cos, log")

    while True:
        user_input = input("Enter expression or command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye.")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input.startswith("export"):
            _, _, file = user_input.partition(" ")
            export_history(file.strip())
        elif user_input.startswith("import"):
            _, _, file = user_input.partition(" ")
            import_history(file.strip())
        else:
            evaluate(user_input)

if __name__ == "__main__":
    main()
