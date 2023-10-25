# Creates 3 T-Poses on the intelligent floor.

import logging
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
BLACK = {"r":0, "g":0 , "b":0}

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

    # draw line from (row1/col1) to (row2/col2)

    # T-Pose Nr.1
    #  Draws the column  
    ifloor.AssetControl.DrawLine(
        row1=19, col1=8, row2=19, col2=12, color=GREEN, layer=0)
    # Draws the row
    ifloor.AssetControl.DrawLine(
        row1=19, col1=10, row2=16, col2=10, color=GREEN, layer=0)

    # T- Pose Nr. 2
    # Draws the column
    ifloor.AssetControl.DrawLine(
        row1=14, col1=16, row2=10, col2=16, color=GREEN, layer=0)
    # Draws the row
    ifloor.AssetControl.DrawLine(
        row1=12, col1=16, row2=12, col2=13, color=GREEN, layer=0)
    
    # T- Pose Nr. 3
    # Draws the column
    ifloor.AssetControl.DrawLine(
        row1=9, col1=11, row2=3, col2=11, color=GREEN, layer=0)
    # Draws the row
    ifloor.AssetControl.DrawLine(
        row1=6, col1=9, row2=6, col2=13, color=GREEN, layer=0)
    
    # draw rectangle
    # ifloor.AssetControl.DrawRectangle(
    #   row1=5, col1=5, row2=17, col2=17, color=BLUE, fill=False, layer=0)

    # clear Layer after 10 secs
    
    # time.sleep(20)
    # ifloor.AssetControl.ClearLayer(layer=0)

    _logger.info("good bye")
    mgr.disconnect()


if __name__ == "__main__":
    main()