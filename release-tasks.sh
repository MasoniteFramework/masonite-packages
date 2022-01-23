#!/bin/bash
# migrate db
python craft migrate --force
# re-compile assets
npm install
NODE_ENV=production npm run production