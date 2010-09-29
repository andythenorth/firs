#!/bin/bash

translation_file=""

cd `dirname $0`

#Try to find a language that matches the parameter (02, spa, any, etc)
if [ -n "$1" ]
then
	translation_file="`find ../sprites/nfo/lang/ -iname "*$1*.pnfo"`"
fi

#If not found, use remove_defines.pnfo
if [ -z "$translation_file" ]
then
	translation_file="../sprites/nfo/lang/remove_defines.pnfo"
fi

echo "Missing strings at file $translation_file"
for string_id in `grep -v "^//" ../sprites/nfo/lang/7F_any.pnfo | cut -f2 -s -d " "`; do
	translated_string_id=`grep "$string_id" $translation_file`
	if [ -z "$translated_string_id" ]
	then
		echo "$string_id"
	fi
done

