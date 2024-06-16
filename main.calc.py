def calculate_tri_values(value):
    try:
        value = float(value)
        min_value = value * 0.3
        avg_value = value * 0.6
        max_value = value * 0.9
        return f"{min_value}'{avg_value}'{max_value}"
    except ValueError:
        return "Error: Input must be a number."

def main():
    while True:
        try:
            user_input = input("Enter a number (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            result = calculate_tri_values(user_input)
            print(result)
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    main()