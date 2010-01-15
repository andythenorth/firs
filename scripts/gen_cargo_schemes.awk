BEGIN {	FS = "," } 
 {
	print "-1 * 0  0C \"Defining "$(n_id)"\""
	print "#define THIS_CARGO_ID CARGO_"remove_white($(n_id))
	print "#define THIS_CARGO_SCHEME SCHEME_"remove_white($(n_scheme))
	print "#define THIS_CARGO_T1 \\b"int($(n_t1))
	print "#define THIS_CARGO_T2 \\b"int($(n_t2))
	print "#define THIS_CARGO_BASEPRICE \\d"int($(n_baseprice))
	print "#define THIS_COMMENT "remove_white($(n_id))" with "remove_white($(n_scheme))" scheme. "
	print "#include \"cargo_schemes.template\"" 
}

function remove_white(string) {
	sub(/[	]+$/,"",string)
	sub(/^[ 	]+|[	]+$/,"",string)
	return string
}