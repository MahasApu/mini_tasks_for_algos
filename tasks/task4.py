#
# cd $1
#
# #print all commits
# git log --pretty=format:'%h'
# echo
# echo "Enter two commits"
#
#
# #read the latest good and bad commit
# read start end
# good=`git log $start..HEAD --pretty=oneline | wc -l`
# bad=`git log $end..HEAD --pretty=oneline | wc -l`
# echo $good $bad
#
# #expand range by one to make binary search include the given revisions
# if [ $good -gt $bad ]; then
#     good=$[ $good + 1 ]
#     bad=$[ $bad - 1 ]
# else
#     bad=$[ $bad + 1 ]
#     good=$[ $good - 1 ]
# fi
#
# # all commits
# commits=($(git log --pretty=format:'%h'))
#
#
# #for (( i=$good; i<$bad; i++));
# #do
# #       echo "${commits[$i]}"
# #done
#
# echo
# echo "Enter the command to execute"
# read command
#
# # execute the command
# $command
# echo $?
#
# pivot=$[($good + $bad) / 2]
#
# revision=`git rev-parse HEAD~$mid`
# echo $revision
#
#
# << 'MULTILINE-COMMENT'
# while [ $[$good - $bad] -lt -1 -o $[$goot - $bad] -gt 1]
# do
#         revision=`git rev-parse HEAD~$mid`
#         pretty_revision=`git show --pretty=format:'%C(auto)%H %s %Cblue%cn %Cgre>        head=`git rev-parse HEAD`
#         git checkout $revision  -q > /dev/null
#         result=$?
#         if [ $result -eq 0 ]; then
#                 good=$mid
#         else
#                 bad=$mid
#         mid=$[($good + $bad) / 2]
# done
# MULTILINE-COMMENTa