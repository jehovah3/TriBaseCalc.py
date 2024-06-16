def parse_equation(equation):
    try:
        equation = equation.replace(" ", "")
        terms = equation.split("=")
        if len(terms) != 2:
            return "Invalid equation format. Use 'x+6*9-76+4=x' format."
        left, right = terms
        positives, negatives = left.split("+"), right.split("-")
        positive_sum = sum(eval(term) for term in positives if term)
        negative_sum = sum(-eval(term) for term in negatives if term)
        return positive_sum, negative_sum
    except Exception as e:
        return f"Error parsing equation: {e}"

def equation_main():
    while True:
        try:
            equation = input("Enter an equation (or 'exit' to quit): ")
            if equation.lower() == 'exit':
                break
            result = parse_equation(equation)
            print(f"Positive sum: {result[0]}")
            print(f"Negative sum: {result[1]}")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    equation_main()
