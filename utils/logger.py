import logging, os
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

def setup_logger(name: str, log_dir: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(log_dir, f"{datetime.now():%Y%m%d}.log")
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(_ColorFmt())

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

class _ColorFmt(logging.Formatter):
    _MAP = {
        logging.DEBUG:    Fore.CYAN,
        logging.INFO:     Fore.GREEN,
        logging.WARNING:  Fore.YELLOW,
        logging.ERROR:    Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }
    def format(self, r):
        return f"{self._MAP.get(r.levelno,'')}{super().format(r)}{Style.RESET_ALL}"
