#!/bin/bash

echo "This will update this git project"
echo "Pleas enter the commit message:"

read mes

echo "adding files ..."
git add *

echo "removing useless files ..."

cd crowbar
git rm -r --cached __pycache__

cd extensions
git rm -r --cached __pycache__

cd ..
git rm -r --cached .gitignore
git rm -r --cached grabbo

echo "pushing ..."
git commit -m $mes
git push

echo "Updated :D"
