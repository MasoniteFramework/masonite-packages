#!/bin/bash
# migrate db
python craft migrate --force
# at deploy find new packages and update packages (when PR#514 merged)
# python schedule:run --force