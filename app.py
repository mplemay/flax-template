from absl import app, flags
from ml_collections import config_flags

FLAGS = flags.FLAGS

config_flags.DEFINE_config_file(
    "config",
    default="configs/default.py",
    lock_config=True,
)


def main(_) -> None:
    pass


if __name__ == "__main__":
    app.run(main)
