#!/bin/bash
# Send and deploy your last commits to OVH
# we need git bundle because Hébergés OVH can't access internet from SSH sessions

# A repository have been created first, from a full bundle on the Hébergé                    

git bundle create prj.bundle last_bundle..mastergit  # you need a tag 'last_bundle' already set
tag -f last_bundle master  # sets the tag for next bundle
scp prj.bundle $user-ovh@ssh.clusterXXX.ovh.net:

CMDS=$(cat <<EOF
cd prj
git pull
./manage.py migrate
./manage.py collectstatic --no-input
EOF
)

ssh $user-ovh@ssh.clusterXXX.ovh.net "$CMDS"