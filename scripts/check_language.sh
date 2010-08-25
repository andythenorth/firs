#!/bin/bash

file=""

#Try to find a language that matches the parameter (02, spa, any, etc)
if [ -n "$1" ]
then
	file="`find ../sprites/nfo/lang/ -iname "*$1*.pnfo"`"
fi

#If not found, use remove_defines.pnfo
if [ -z "$file" ]
then
	file="../sprites/nfo/lang/remove_defines.pnfo"
fi

echo "Missing strings at file $file"
for text in `grep "#define" ../sprites/nfo/lang/base_lang.pnfo | cut -f2 -d " "`; do
	value=`grep "$text" $file`
	if [ -z "$value" ]
	then
		echo "$text"
	fi
done

