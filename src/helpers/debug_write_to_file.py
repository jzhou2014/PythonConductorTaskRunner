import os


def debug_write_to_file(data, filename, mode="w"):
    if os.environ.get("DEBUG") == "true":
        with open(filename, mode) as f:
            f.write(data)
