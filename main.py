from src.core import scrapper


if __name__ == '__main__':
    try:
        scrapper.run('2021-11-16')
    except KeyboardInterrupt:
        scrapper.stop()