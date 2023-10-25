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
    ifloor.AssetControl.DrawLine(
        row1=6, col1=12, row2=18, col2=12, color=YELLOW, layer=0)
    ifloor.AssetControl.DrawLine(
        row1=12, col1=6, row2=12, col2=16, color=RED, layer=0)

    # draw rectangle
    ifloor.AssetControl.DrawRectangle(
        row1=5, col1=5, row2=17, col2=17, color=BLUE, fill=True, layer=0)

    # clear Layer after 10 secs
    # while True:
    #     time.sleep(10)
    ifloor.AssetControl.ClearLayer(layer=0)

    _logger.info("good bye")
    mgr.disconnect()


if __name__ == "__main__":
    main()
