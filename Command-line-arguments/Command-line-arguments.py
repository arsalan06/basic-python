import argparse
parser = argparse.ArgumentParser(
    description="provides a personal greeting"
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name is required"
)

args = parser.parse_args()
msg = f"Hello {args.name}!"
print(msg)
