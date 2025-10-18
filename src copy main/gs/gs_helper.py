import global_constants


class GSHelper(object):
    # GS-specific methods for formatting etc in chameleon templates, this is only for things not handled in industry.py or utils.py

    def get_economy_fingerprint(self, firs, economy):
        result = ""
        # as of August 2021, port and wharf were sufficiently unique, and at least one of them is in every economy
        # !! this could use a guard to enforce uniqueness
        for industry in firs.industry_manager:
            if industry.id in ["port", "wharf"]:
                if industry.economy_variations[economy.id].enabled:
                    fingerprint_industry = industry
                    break
        result = (
            result
            + "Accepts: "
            + " ".join(sorted(fingerprint_industry.get_accepted_cargo_labels_by_economy(economy)))
        )
        result = result + " Produces:"
        for cargo_label, prod_multiplier in sorted(
            fingerprint_industry.get_prod_cargo_types(economy)
        ):
            result = result + " " + cargo_label
        return result

    def get_grfid(self):
        return "0x" + global_constants.grfid

    def gs_list_repr(self, _list):
        # chameleon will render lists as ['foo', 'cabbage', '3']; squirrel wants them as ["foo", "cabbage", 3]
        result = []
        for item in _list:
            if isinstance(item, list):
                # this attempts to handle recursive items
                result.append(self.gs_list_repr(item))
            elif isinstance(item, (int, float)):
                result.append(str(item))
            elif isinstance(item, str):
                # strings need double quotes, whereas python repr will single quote them
                result.append('"' + item + '"')
            else:
                # extend if more types are needed
                raise Exception("gs_list_repr. Don't know what to do with " + str(item))
        return "[" + ",".join(result) + "]"

    def gs_table_repr(self, _dict):
        # chameleon will render dicts as {'foo': 'cabbage', 'ham': 'eggs'}; squirrel wants them as tables in the form {"foo" = "cabbage", "ham" = "eggs"}
        # although it wasn't a problem here as of May 2024, note that, as far as testing shows, strings can't be used as table slot ids (keys) in Squirrel
        # this works because chameleon renders the python literal strings out as ids in the .nut, which is fine
        result = []
        for key, value in _dict.items():
            kv_result = key + " = "
            if value == None:
                kv_result = kv_result + "null"
            elif isinstance(value, list):
                # this attempts to handle recursive items
                kv_result = kv_result + self.gs_list_repr(value)
            elif isinstance(value, dict):
                # this attempts to handle recursive items
                kv_result = kv_result + self.gs_table_repr(value)
            elif isinstance(value, bool):
                # python uses 'True' and 'False', squirrel uses 'true' and 'false'
                # note that bool must be checked before int/float, as True and False are also instances of int/float
                kv_result = kv_result + str(value).lower()
            elif isinstance(value, (int, float)):
                kv_result = kv_result + str(value)
            elif isinstance(value, str):
                # strings need double quotes, whereas python repr will single quote them
                kv_result = kv_result + '"' + value + '"'
            else:
                # extend if more types are needed
                raise Exception(
                    "gs_table_repr. Don't know what to do with " + str(value)
                )
            result.append(kv_result)

        return "{" + ",".join(result) + "}"
