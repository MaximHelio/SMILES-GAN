import random


def generate_random_molecule(length=5):
    elements = ['C', 'O', 'N', 'H']
    molecule = random.choices(elements, k=length)
    return ''.join(molecule)


if __name__ == "__main__":
    num_molecules = 5

    print("Generated Molecules:")
    for _ in range(num_molecules):
        molecule = generate_random_molecule(length=random.randint(3, 8))
        print(molecule)
