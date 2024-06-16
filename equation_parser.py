def parse_equation(equation):
    parts = equation.split('=')
    if len(parts) != 2:
        return "Invalid equation format. Please use 'equation = result'."
    
    left, right = parts[0].strip(), parts[1].strip()
    left_parts = left.split('+')
    right_parts = right.split('-')
    
    try:
        left_sum = sum(float(part) for part in left_parts)
        right_diff = -sum(float(part) for part in right_parts)
        return f"Max (left): {left_sum}, Min (right): {right_diff}"
    except ValueError as ve:
        return f"Invalid value in equation: {ve}"

def main():
    while True:
        equation = input("Enter an equation (e.g., 1+2-3=x): ")
        if equation.lower() == 'exit':
            break
        
        result = parse_equation(equation)
        print(result)

        prompt = input("Do you want to parse another equation? (yes/no): ")
        if prompt.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

