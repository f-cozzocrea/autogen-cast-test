from itertools import permutations

ptr_vars = {
        "void*": "void_ptr",
        }

int_vars = {
        "intptr_t": "iptr",
        "uintptr_t": "uptr",
        "size_t": "size",
#        "bool": "boolean",
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
        }

float_vars = {
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

head = """\
#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
//#include <complex.h>

int run() {
"""

tail = """\
}

// run-translated-c
// c_frontend=aro,clang
// link_libc=true
"""

def main():
    # Body of the main function:
    body = ""

    # A dict of all number types
    num_vars = int_vars | float_vars

    # Add pointer types for all listed types
    for ctype in num_vars:
        ptr_type = ctype + '*'
        var = num_vars[ctype] + "_ptr"
        ptr_vars[ptr_type] = var

    # Declare the variables for each type
    var_decls = ""
    type_vars = ptr_vars | int_vars | float_vars
    for t in type_vars:
        var_decls += f"    {t} {type_vars[t]};\n"

    body += var_decls

    # Create permutations based on a loose idea of the combinations that are allowed
    intxptr_vars = int_vars | ptr_vars
    intxptr_list = [*intxptr_vars]
    intxptr_permutations = permutations(intxptr_list, 2)

    num_list = [*num_vars]
    num_permutations = permutations(num_list, 2)

    type_permutations = list(set([*intxptr_permutations, *num_permutations]))

    for i, p in enumerate(type_permutations):
        if (is_illegal_cast(p)):
            continue
        dest = p[0]
        src  = p[1]

        body += "\n"
        body += f"    {type_vars[src]} = ({src})80;\n"
        body += f"    {type_vars[dest]} = ({dest}){type_vars[src]};\n"
        body += f"    if ({type_vars[dest]} != 80) return {i+1};\n"

    body += "\n"
    body += "    return 0;\n"

    filename = "basic_cast_testing.c"
    with open(filename, 'w') as f:
        f.write(head)
        print(head)
        f.write(body)
        print(body)
        f.write(tail)
        print(tail)

# Detect whether a type cast is legal in C. ie. whether it will compile successfully.
def is_illegal_cast(permutation: tuple) -> bool:
    if len(permutation) != 2:
        raise ValueError(f"permutation had {len(permutation)} items. Must have 2. {permutation}")

    return False 


if __name__ == "__main__":
    main()

