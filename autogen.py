from itertools import permutations

type_vars = {
        "void*": "void_ptr",
        "intptr_t": "iptr",
        "uintptr_t": "uptr",
        "size_t": "size",
        "bool": "boolean",
        "int8_t": "int8",
        "uint8_t": "uint8",
        "int16_t": "int16",
        "uint16_t": "uint16",
        "int32_t": "int32",
        "uint32_t": "uint32",
        "int64_t": "int64",
        "uint64_t": "uint64",
        ## "__int128": int128,
        ## "unsigned __int128": uint128,
        "signed char": "s_char",
        "unsigned char": "u_char",
        "short": "s_short",
        "unsigned short": "u_short",
        "int": "s_int",
        "unsigned int": "u_int",
        "long": "s_long",
        "unsigned long": "u_long",
        "long long": "s_longlong",
        "unsigned long long": "u_longlong",
        # "_Float16": fl16,
        "float": "fl",
        "double": "doub",
        "long double": "l_doub",
        # "_Float128": fl128,
        # TODO: Complex types not supported in zig yet.
        # "float complex": "fl_complex",
        # "double complex": "doub_complex",
        # "long double complex": "long_doub_complex",
        }

preamble = """
#include stdbool.h
#include stdint.h
#include stddef.h
//#include complex.h

int main() {

"""

def main():
    # Declare the variables for each type
    var_decls = ""
    type_list = []
    for t in type_vars:
        var_decls += f"    {t} {type_vars[t]};\n"
        type_list.append(t)
    
    type_permutations = permutations(type_list, 2)
    for p in type_permutations:
        if (is_illegal_cast(p)):
            continue

def is_illegal_cast(permutation: tuple) -> bool:
    if len(permutation) != 2:
        raise ValueError(f"permutation had {len(permutation)} items. Must have 2. {permutation}")

    return False 


if __name__ == "__main__":
    main()

