import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-p",
    "--port",
    type=int,
    default="8000",
    help="port to serve the HTTP server (default: 8000)",
)

def main(args):
    print(args)
    print(args.port)


if __name__ == "__main__":

    main(parser.parse_args())
