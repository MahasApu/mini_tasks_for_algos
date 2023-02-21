#!/bin/bash

cd $1

#print all commits
git log --pretty=format:'%h'
echo
echo "Enter two commits"


#read the latest good and bad commit
read start end
good=`git log $start..HEAD --pretty=oneline | wc -l`
bad=`git log $end..HEAD --pretty=oneline | wc -l`
echo $good $bad

#expand range
if [ $good -gt $bad ]; then
    good=$[ $good + 1 ]
    bad=$[ $bad - 1 ]
else
    bad=$[ $bad + 1 ]
    good=$[ $good - 1 ]
fi

# all commits

# commits=($(git log --pretty=format:'%h'))

echo
echo "Enter the command to execute"
read command

pivot=$[($good + $bad) / 2]
wanted=$bad

while [ $[$good - $bad] -lt -1 ] | [ $[$good - $bad] -gt 1 ]
do

    revision=`git rev-parse HEAD~$pivot`  #change head to pivot commit
    git checkout $revision  -q > /dev/null # turn to pivot commit
    $command
    result=$?

    if [ $result -eq 0 ]; then
        good=$pivot
    else
        bad=$pivot
        wanted=$revision
    fi

    git checkout - -q > /dev/null
    pivot=$[($good + $bad) / 2]
done
echo "bad commit is"
echo $wanted