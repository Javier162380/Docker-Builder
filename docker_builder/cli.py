import argparse
import os


def cli():

    args = argparse.ArgumentParser(
        description="Welcome to Docker Builder. The tool for build your images in "
                    "a efficient way"
    )

    args.add_argument(
        "--build_timeout",
        required=False,
        default=600,
        type=int
    )

    args.add_argument(
        "--successful_job_timeout",
        required=False,
        default=36000,
        type=int
    )

    args.add_argument(
        "--failed_job_timeout",
        required=False,
        default=1314000,
        type=int
    )

    parse_args = args.__dict__()

    parse_args.update(**os.environ)

    return parse_args
