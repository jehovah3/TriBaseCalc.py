def tri_base_calculator(value):
    try:
        value = float(value)
        min_value = value * 0.3
        avg_value = value * 0.6
        max_value = value * 0.9
        return f"{min_value:.1f}'{avg_value:.1f}'{max_value:.1f}"
    except ValueError:
        return "Invalid input. Please enter a number."

def main():
    while True:
        try:
            value = input("Enter a number (or 'exit' to quit): ")
            if value.lower() == 'exit':
                break
            result = tri_base_calculator(value)
            print(f"Result: {result}")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    main()