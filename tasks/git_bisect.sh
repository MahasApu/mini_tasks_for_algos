#!/bin/bash

cd $1

# print all commits
git log --pretty=format:'%h'

# read the latest good and bad commit
echo
echo "Enter two commits"
read start end

# read command to execute
echo "Enter the command to execute: "
read command

# get an array of all commits from start commit to end comm>
all_commits=$(git log $start..$end --pretty=format:'%h')

# add start commit to the end
commits="${all_commits} $start"
commits=($(echo $commits))

# init good and bad commits as last and first indexes in array
good=${#commits[@]}
bad=0

pivot=$((($good + $bad) / 2))
wanted=${commits[bad]}

while [ $(($good - $bad)) -gt 1 ]; do

  git checkout ${commits[$pivot]} -q >/dev/null
  $command
  result=$?

  if [ $result -eq 0 ]; then
    good=$pivot

  else
    bad=$pivot
    wanted=${commits[$pivot]}
  fi

  git checkout - -q >/dev/null
  pivot=$((($good + $bad) / 2))

done

echo "bad commit is"
echo $wanted
