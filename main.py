import random

def simulate_boy_girl_paradox(sample_size):
    # Create the 200 families as specified
    families = []
    x=0

    # First 50: GG
    for x in range(50):
        families.append(['G', 'G'])

    # Next 50: BG
    for x in range(50):
        families.append(['B', 'G'])

    # Next 50: GB
    for x in range(50):
        families.append(['G', 'B'])

    # Last 50: BB (not GG as mentioned in your description - I assume this was a typo)
    for x in range(50):
        families.append(['B', 'B'])

    # Initialize counters
    initial_girl = 0
    initial_girl_then_girl = 0
    initial_girl_then_boy = 0

    initial_boy = 0
    initial_boy_then_boy = 0
    initial_boy_then_girl = 0

    # Run the simulation
    for x in range(sample_size):
        # Randomly select a family
        family_index = random.randint(0, 199)
        selected_family = families[family_index]

        # Randomly select a child (0 or 1)
        child_index = random.randint(0, 1)
        first_child = selected_family[child_index]

        # Get the other child
        other_child_index = 1 - child_index
        second_child = selected_family[other_child_index]

        if first_child == 'G':
            initial_girl += 1
            if second_child == 'G':
                initial_girl_then_girl += 1
                print("I have one child who is a girl. The other child is also a girl.")
            else:  # second_child == 'B'
                initial_girl_then_boy += 1
                print("I have one child who is a girl. The other child is a boy.")
        else:  # first_child == 'B'
            initial_boy += 1
            if second_child == 'B':
                initial_boy_then_boy += 1
                print("I have one child who is a boy. The other child is also a boy.")
            else:  # second_child == 'G'
                initial_boy_then_girl += 1
                print("I have one child who is a boy. The other child is a girl.")

    # Calculate probabilities
    prob_girl_then_girl = initial_girl_then_girl / initial_girl if initial_girl > 0 else 0
    prob_girl_then_boy = initial_girl_then_boy / initial_girl if initial_girl > 0 else 0
    prob_boy_then_boy = initial_boy_then_boy / initial_boy if initial_boy > 0 else 0
    prob_boy_then_girl = initial_boy_then_girl / initial_boy if initial_boy > 0 else 0

    # Print results
    print(f"Sample Size: {sample_size}")
    print("\nWhen first child mentioned is a GIRL:")
    print(f"  Total cases: {initial_girl}")
    print(f"  Girl then Girl: {initial_girl_then_girl} ({prob_girl_then_girl:.3f})")
    print(f"  Girl then Boy: {initial_girl_then_boy} ({prob_girl_then_boy:.3f})")

    print("\nWhen first child mentioned is a BOY:")
    print(f"  Total cases: {initial_boy}")
    print(f"  Boy then Boy: {initial_boy_then_boy} ({prob_boy_then_boy:.3f})")
    print(f"  Boy then Girl: {initial_boy_then_girl} ({prob_boy_then_girl:.3f})")

    print(f"\nTotal families sampled: {sample_size}")
    print(f"Total girl-first cases: {initial_girl}")
    print(f"Total boy-first cases: {initial_boy}")

    return {
        'initial_girl': initial_girl,
        'initial_girl_then_girl': initial_girl_then_girl,
        'initial_girl_then_boy': initial_girl_then_boy,
        'initial_boy': initial_boy,
        'initial_boy_then_boy': initial_boy_then_boy,
        'initial_boy_then_girl': initial_boy_then_girl
    }

# Run the simulation with different sample sizes
sample_sizes = [100, 1000, 10000, 100000]

for size in sample_sizes:
    results = simulate_boy_girl_paradox(size)
    print("=" * 50)

