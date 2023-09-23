import boto3
from commandline import parse_command_line_flags
from const import CLOUD_WATCH_SERVICE_NAME


def main() -> int:
    """The core entrypoint to rdsmon."""
    _ = parse_command_line_flags()
    _ = boto3.client(CLOUD_WATCH_SERVICE_NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
