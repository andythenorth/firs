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
for string_id in `grep "#define" ../sprites/nfo/lang/7F_any.pnfo | cut -f2 -d " "`; do
	translated_string_id=`grep "$string_id" $translation_file`
	if [ -z "$translated_string_id" ]
	then
		echo "$string_id"
	fi
done

#Use \n as field separator.
old_IFS=$IFS
IFS=$'\n'

echo "Strings modified since last update at file $translation_file"
declare -A revision_map
`hg blame $translation_file | grep "#define" > /tmp/lang_blame.txt`
for original_line in `hg blame ../sprites/nfo/lang/7F_any.pnfo | grep "#define" | sed 's/^ //'`; do
	original_string_id=`echo $original_line | cut -f3 -d " "`
	translated_line=`grep " $original_string_id " /tmp/lang_blame.txt | sed 's/^ //'`
	if [ -n "$translated_line" ]
	then
		original_revision=`echo $original_line | cut -f1 -d ":"`
		translated_revision=`echo $translated_line | cut -f1 -d ":"`
		if [ "$original_revision" -gt "$translated_revision" ]
		then
			echo "$original_string_id (Original: $original_revision, Translation: $translated_revision)"
		fi
	fi
done
#Restore the field separator.
IFS=$old_IFS

echo "Not required strings at file $translation_file"
for string_id in `grep "#define" $translation_file | cut -f2 -d " "`; do
	translated_string_id=`grep "$string_id" ../sprites/nfo/lang/7F_any.pnfo`
	if [ -z "$translated_string_id" ]
	then
		echo "$string_id"
	fi
done
