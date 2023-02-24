"""
Scraper app
"""

import os
import pywebcopy
from pywebcopy import save_webpage

CURRENT_PATH = os.getcwd()
save_webpage(
      url="https://www.classcentral.com/",
      project_folder=CURRENT_PATH + "//web//pycopy",
      project_name="my_site",
      bypass_robots=True,
      debug=True,
      open_in_browser=True,
      delay=None,
      threaded=False,
)