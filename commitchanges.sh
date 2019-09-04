#!/bin/bash



git add .

read -p 'Commit Description: ' commitdesc
git commit -m "$commitdesc"

git status

git push

git pull

echo "Thank you, commit has been submitted with the description \"$commitdesc\""
