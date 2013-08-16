#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
import logging

"""
setup logger.
"""
logger = logging.getLogger('test.test_setup')
logger.setLevel(logging.DEBUG)

"""
Setup git environment.
"""
def git_env_setup(path):
  cur_path = os.path.join(os.getcwd(),path)
  # Remove current git repository
  git_env_remove(path)
  # Create new git repository
  logger.debug("Initializing git repository for test")
  subprocess.call("git init .",shell=True, cwd=cur_path)

"""
Remove git environment.
"""
def git_env_remove(path):
  # Remove current git repository
  cur_path = os.path.join(os.getcwd(),path)
  if os.path.exists(os.path.join(cur_path,".git")): 
    shutil.rmtree("%s/%s" % (cur_path,".git"))
    logger.debug("Git repository %s was vanished", cur_path)
  
