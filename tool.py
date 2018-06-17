#!/usr/bin/env

# Imports
import argparse, os, shutil, subprocess, sys

# Variables
# To be remove
folderToRm = ["/index/__pycache__", "/index/__pycache__", "/index/migrations/__pycache__", "/website/__pycache__"]
fileToRm = ["/server.log"]

# Functions
def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def start():
  with open("server.log","wb") as out:
    subprocess.Popen('python3 manage.py runserver', stdin=out, stdout=out, stderr=out, shell=True)


def stop():
  subprocess.run('ps -C \'python3 manage.py runserver\' -o pid= | xargs kill -9', stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)


def rmvFolder(path):
  cmpltePath = get_script_path() + path
  if os.path.isdir(cmpltePath) == True:
    shutil.rmtree(cmpltePath)


def rmvFile(path):
  cmpltePath = get_script_path() + path
  if os.path.isfile(cmpltePath) == True:
    os.remove(cmpltePath)


def clean():
  for folder in folderToRm:
    rmvFolder(folder)
  for file in fileToRm:
    rmvFile(file)


def restart():
  stop()
  clean()
  start()


def cmdDptchr(choice):
  if choice == 'start':
    start()
  elif choice == 'restart':
    restart()
  elif choice == 'stop':
    stop()
  elif choice == 'clean':
    clean()


def main(argv):
	parser = argparse.ArgumentParser(description='Tool to run the server. /usr/bin/python3 should be configured')
	parser.add_argument('cmd', choices=['start', 'stop', 'clean'], help='Either start, restart, stop or clean')
	args = parser.parse_args()
	cmdDptchr(args.cmd)


if __name__ == "__main__":
  main(sys.argv)