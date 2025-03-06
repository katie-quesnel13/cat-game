import json
import random

from describecat import describe
from cat_creation_methods import get_prefix, get_suffix, random_genestring


def create_cat_entry():
    genes = random_genestring()
    appearance = describe(genes)
    prefix = get_prefix(appearance)
    age = int(random.random() ** 1.5 * 167) + 1
    suffix = get_suffix(prefix, age)
    print(f"{prefix}{suffix}, {appearance}. {age} moons old")


def main():
    clansize = input("How many cats would you like to generate?")
    for _ in range(int(clansize)):
        create_cat_entry()


if __name__ == "__main__":
    main()
