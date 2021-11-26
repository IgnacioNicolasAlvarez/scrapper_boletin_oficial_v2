#from src.core.scheduler import run
from src.core.scrapper import extraer as run

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        exit(1)


