egrep -H -v -n "^Moodul|^M[1-9]|^A\**\.|^B\**\.|^C\**\.|^D\**\.|^E\**\." ?-klass.txt
egrep -h "^M[0-9][0-9]*-" ?-klass.txt | sed -e s/B\-/\-/ | sed -e s/A\-/\-/ | sort | uniq -c | egrep -v "^   3 "
