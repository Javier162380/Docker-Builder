import argparse
import os

def cli():
    
    args = argparse.ArgumentParser(
        description="Welcome to Docker Builder. The tool for build your images in "
                    "a efficient way"
    )

    args.add_argument(
        "--db_type",
        required=False,
        default='redis'
    )

    parse_args = args.__dict__()

    parse_args.update(**os.environ)

    return parse_args