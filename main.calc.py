def tri_base_calculator(value):
    if value == 0:
        return f"0'0'0"
    factor = value if value != 0 else 1
    min_value = factor * 0.3
    avg_value = factor * 0.6
    max_value = factor * 0.9
    return f"{min_value:.1f}'{avg_value:.1f}'{max_value:.1f}"

# Testing the function with the example given
result = tri_base_calculator(17)
print(result)  # Should print: 5.1'10.2'15.3

# Additional test with three values provided
values = [17, 5, 99, 0]
for value in values:
    result = tri_base_calculator(value)
    print(f"For {value}: {result}")