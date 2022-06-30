import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-p",
    "--port",
    type=str,
    default="8000",
    help="port to serve the HTTP server (default: 8000)",
)

def main(args):
    f = open("ID.txt", "w")
    f.write(str(args.id))
    f.close()
    f = open("ID.txt", "r")
    print(f.read())


if __name__ == "__main__":

    main(parser.parse_args())
