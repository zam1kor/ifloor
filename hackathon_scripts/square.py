import logging
import time
import sys
from assets2036py import AssetManager, AssetNotFoundError


# credentials to access floor
BROKER = "10.163.31.2"
# BROKER = "backend.fac6310.btia.emea.ide.rb"
PORT = 1883
NAMESPACE = "arena2036"
ASSET_NAME = "intelligent_floor"

# floor properties
MAX_ROW_IDX = 22
MAX_COL_IDX = 24

# colors
# IMPORTANT!! Using brightness values >100 can cause fuses to fry if used with to many tiles!
RED = {"r": 100, "g": 0, "b": 0}
GREEN = {"r": 0, "g": 100, "b": 0}
BLUE = {"r": 0, "g": 0, "b": 100}
YELLOW = {"r": 100, "g": 100, "b": 0}
WHITE = {"r": 100, "g": 100, "b": 100}
PURPLE = {"r":80, "g":0 , "b":80}
BLACK = {"r":0, "g":0 , "b":0}

list_of_colors = [RED, GREEN, BLUE, YELLOW, PURPLE]

_logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO)

    mgr = AssetManager(BROKER, PORT, NAMESPACE, "ifloor_starterkit")
    try:
        ifloor = mgr.create_asset_proxy(NAMESPACE, ASSET_NAME)
        _logger.info("connected to floor")
    except AssetNotFoundError:
        _logger.error("%s/%s could not be found! Exiting")
        sys.exit(-1)

    # Issue commands to intelligent floor.
    # Important!! Use keyword arguments!!!

    for col in range(12, 20):
        for row in range(11, 19): 
            for color in list_of_colors:
            # draw rectangle
                ifloor.AssetControl.DrawRectangle(
                row1=row, col1=row, row2=col, col2=col, color=color, fill=False, layer=0)
                time.sleep(0.25)

    for col in range(20, 12):
        for row in range(19, 11): 
            for color in list_of_colors:
            # draw rectangle
                ifloor.AssetControl.DrawRectangle(
                row1=row, col1=row, row2=col, col2=col, color=color, fill=False, layer=0)
                time.sleep(0.25)

    _logger.info("good bye")
    mgr.disconnect()


if __name__ == "__main__":
    main()