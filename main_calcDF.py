def tri_base_calculator(value):
    min_value = value * 0.3
    avg_value = value * 0.6
    max_value = value * 0.9
    return f"{min_value}'{avg_value}'{max_value}"

# Testing the function with the example given
result = tri_base_calculator(17)
print(result)  # Should print: 5.1'10.2'15.3

# Additional test with three values provided
values = [17, 5, 99]
for value in values:
    result = tri_base_calculator(value)
    print(f"For {value}: {result}")

# Calculate TriImperial values
def tri_imperial_calculator(value):
    return tri_base_calculator(value)

# Testing the TriImperial calculator
tri_imperial_values = [tri_imperial_calculator(value) for value in values]
for value, result in zip(values, tri_imperial_values):
    print(f"For {value}: {result}")

# Predictive analytics and mathematical concepts
# For demonstration purposes, let's calculate the average TriBase value for a series of numbers
numbers = [4, 23, 6, 21, 23, 629, 8, 7, 62849]
average_tri_base_values = [tri_base_calculator(number) for number in numbers]
average_tri_base_value = sum(average_tri_base_values) / len(numbers)
print(f"Average TriBase value: {average_tri_base_value}")
