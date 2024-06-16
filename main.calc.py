def tri_base_calculator(value):
    min_value = value * 0.3
    avg_value = value * 0.6
    max_value = value * 0.9
    return f"{min_value:.1f}'{avg_value:.1f}'{max_value:.1f}"

def main():
    while True:
        try:
            value = float(input("Enter a number to calculate its tri-base values (or type 'exit' to quit): "))
            result = tri_base_calculator(value)
            print(f"Tri-base values: {result}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            
        prompt = input("Do you want to calculate another number? (yes/no): ")
        if prompt.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
