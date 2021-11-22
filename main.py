from src.core.scheduler import run


if __name__ == "__main__":
    try:
        run("2021-11-16")
    except KeyboardInterrupt:
        exit(1)
