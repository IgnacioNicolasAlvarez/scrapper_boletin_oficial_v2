import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def loggear(mensaje, tipo):
    if tipo == "info":
        logging.info(mensaje)
    elif tipo == "warning":
        logging.warning(mensaje)
    elif tipo == "error":
        logging.error(mensaje)
    elif tipo == "debug":
        logging.debug(mensaje)
