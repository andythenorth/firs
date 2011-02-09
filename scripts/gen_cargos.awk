BEGIN {	FS = "," } 
 {
	print "-1 * 0  0C \"Defining "$(n_id)"\""
	print "#define THIS_CARGO_ID CARGO_"remove_white($(n_id))
	print "#define THIS_CARGO_BITMASK CARGO_"remove_white($(n_id))
	print "#define THIS_CARGO_STR_CTYPE STR_CRG_"remove_white($(n_id))"_CTYPE"
	print "#define THIS_CARGO_STR_1TYPE STR_CRG_"remove_white($(n_id))"_1TYPE"
	print "#define THIS_CARGO_STR_CARGOUNITS STR_CRG_"remove_white($(n_id))"_CARGOUNITS"
	print "#define THIS_CARGO_STR_CARGOAMOUNT STR_CRG_"remove_white($(n_id))"_CARGOAMOUNT"
	print "#define THIS_CARGO_STR_TABBR STR_CRG_"remove_white($(n_id))"_TABBR"
	print "#define THIS_CARGO_SPRITENO "$(n_spriteno)
	print "#define THIS_CARGO_WEIGHT \\b"int($(n_weight))
	print "#define THIS_CARGO_COLOUR \\b"int($(n_colour))
	print "#define THIS_CARGO_FREIGHTSTATUS \\b"int($(n_freightstatus))
	print "#define THIS_CARGO_CARGOCLASSES \\w"get_cargoclass($(n_cargoclass))
	print "#define THIS_CARGO_CLABEL CLABEL_"remove_white($(n_id))
	print "#define THIS_CARGO_SUBST_TOWNGROWTH "$(n_subst_town)
	print "#define THIS_CARGO_MULT_TOWNGROWTH \\w"int($(n_mult_town))
	print "#define THIS_CARGO_CALLBACKFLAGS \\b"int($(n_callbackflags))
	print "#define THIS_CARGO_CLIMATE "$(n_climate)
	print "#include \"cargos.template\""
}

function bin2hex(bin) {
	return sprintf("%02X",bin)
}

function remove_white(string) {
	sub(/[	]+$/,"",string)
	sub(/^[ 	]+|[	]+$/,"",string)
	return string
}

function get_cargoclass(string) {
	string = tolower(string)
	flags = 0
	flags += (index(string,"pax") != 0)         *   01
	flags += (index(string,"passenger") != 0)   *   01
	flags += (index(string,"mail") != 0)        *   02
	flags += (index(string,"express") != 0)     *   04
	flags += (index(string,"armored") != 0)     *   08
	flags += (index(string,"bulk") != 0)        *   16
	flags += (index(string,"piece") != 0)       *   32
	flags += (index(string,"goods") != 0)       *   32
	flags += (index(string,"liquid") != 0)      *   64
	flags += (index(string,"refrigerate") != 0) *  128
	flags += (index(string,"hazardous") != 0)   *  256
	flags += (index(string,"covered") != 0)     *  512
	flags += (index(string,"sheltered") != 0)   *  512
	flags += (index(string,"oversized") != 0)   * 1024
	return flags
}
