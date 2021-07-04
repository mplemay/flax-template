from absl import app, flags, logging
from ml_collections import config_flags

FLAGS = flags.FLAGS

config_flags.DEFINE_config_file(
    "config",
    default="configs/default.py",
    lock_config=True,
)


def main(argv: list) -> None:
    if len(argv) > 1:
        raise app.UsageError("Too many command-line arguments!")

    logging.set_verbosity(logging.ERROR)


if __name__ == "__main__":
    app.run(main)
