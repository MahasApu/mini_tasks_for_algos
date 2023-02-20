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

echo
echo "Enter the command to execute"
read command

pivot=$[($good + $bad) / 2]
wanted=$bad

while [ $[$good - $bad] -lt -1 -o $[$good - $bad] -gt 1 ]
do

    revision=`git rev-parse HEAD~$mid`
    git checkout $revision  -q > /dev/null
    $command
    result=$?

    if [ $result -eq 0 ]; then
        good=$mid
    else
        bad=$mid
        wanted=$revision
    fi

    git checkout - -q > /dev/null
    mid=$[($good + $bad) / 2]
done
echo "bad commit is"
echo $wanted