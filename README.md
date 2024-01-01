# autogen-cast-test
A short Python program to generate C source file that tries many different type casts. Used for testing Zig's translate-c functionality.

## Running auto generation
`python3 autogen.py`

## Running the test
`zig run -I. test.zig -lc`

