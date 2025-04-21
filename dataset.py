import pandas as pd
import random

# Define size generation rules based on observed data
def get_tshirt_size(height, weight):
    if height <= 160 and weight <= 63:
        return 'S'
    elif height <= 165 and weight <= 65:
        return 'L'
    else:
        return 'XL'

# Generate synthetic dataset
data = []
for _ in range(1000):
    height = random.randint(150, 190)  # height in cm
    weight = random.randint(50, 100)   # weight in kg
    size = get_tshirt_size(height, weight)
    data.append((height, weight, size))

# Create DataFrame
df = pd.DataFrame(data, columns=['Height (in cms)', 'Weight (in kgs)', 'T Shirt Size'])

df.to_csv("shirtsizes.csv")
