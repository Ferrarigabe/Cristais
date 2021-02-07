#!/bin/bash
git init
git add .
git commit -m "$1"
git remote add origin https://github.com/Ferrarigabe/Cristais.git
git push origin master
