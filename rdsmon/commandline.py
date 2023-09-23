import argparse

from configuration import Configuration


def parse_command_line_flags() -> Configuration:
    """Parse sys.argv into something meaningful.  This will be getting
    replaced with `typeR` later."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--region",
        "-r",
        dest="region",
        action="store",
        required=True,
        help="The region to look up rds instances within",
    )
    return Configuration(**vars(parser.parse_args()))
