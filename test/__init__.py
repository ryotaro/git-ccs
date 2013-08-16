#!/usr/bin/env python

import logging
import test_setup

"""
logger setup.
""" 
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s (%(levelname)s|%(name)s) %(message)s '))
logger.addHandler(ch)
logger.debug("Root logger for test has been launched.")

"""
package setup.
"""
def setup_package():
  # git repository setup
  test_setup.git_env_setup('.')

"""
package finilize.
"""
def teardown_package():
  # git repository remove
  test_setup.git_env_remove('.')
