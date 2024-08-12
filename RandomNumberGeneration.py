import random

# 1. Random float between 0 and 1
rand_float = random.random()
print(f"Random float between 0 and 1: {rand_float}")

# 2. Random integer between 1 and 10
rand_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {rand_int}")

# 3. Random float between 1.5 and 5.5
rand_float_range = random.uniform(1.5, 5.5)
print(f"Random float between 1.5 and 5.5: {rand_float_range}")

# 4. Random integer between 0 and 100 (step 10)
rand_int_step = random.randrange(0, 101, 10)
print(f"Random integer between 0 and 100 (step 10): {rand_int_step}")

# 5. Random choice from a list
items = ['apple', 'banana', 'cherry', 'date']
rand_choice = random.choice(items)
print(f"Random choice from list: {rand_choice}")

# 6. Random choices from a list
rand_choices = random.choices(items, k=2)
print(f"Random choices from list: {rand_choices}")

# 7. Shuffle a list
random.shuffle(items)
print(f"Shuffled list: {items}")

# 8. Random number from Gaussian distribution (mean=0, std=1)
rand_gauss = random.gauss(0, 1)
print(f"Random number from Gaussian distribution (mean=0, std=1): {rand_gauss}")
