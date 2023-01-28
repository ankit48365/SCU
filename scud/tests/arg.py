import argparse

parser = argparse.ArgumentParser(
    description='This program prints a color HEX value'
)

parser.add_argument('-c', '--color', metavar='color', required=True, help='the color to search for')

args = parser.parse_args()

print(args.color) # 'red'