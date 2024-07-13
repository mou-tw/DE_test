import logging

from datetime import datetime
from utils import ensure_directory_exists

file_base_path = "/DE_TEST"
def set_logger(log_file_name, dt ):
    """
    Check if a directory exists at the given path. If the directory does not exist, create it.

    :param path: The path of the directory to check or create
    """
    log_dir = file_base_path + "/logs/" + dt + "/" 
    ensure_directory_exists(log_dir)
    logging.basicConfig(filename=log_dir + log_file_name + datetime.today().strftime('%Y%m%d-%s')+ ".log", 
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(log_file_name)
