import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def loggear(mensaje, tipo):
    if tipo == "info":
        print(f"INFO: - {mensaje}")
        logging.info(mensaje)
    elif tipo == "warning":
        print(f"WARNING: - {mensaje}")
        logging.warning(mensaje)
    elif tipo == "error":
        print(f"ERROR: - {mensaje}")
        logging.error(mensaje)
    elif tipo == "debug":
        print(f"DEBUG: - {mensaje}")
        logging.debug(mensaje)
