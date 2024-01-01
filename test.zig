const std = @import("std");

const basic_cast_test = @cImport(@cInclude("basic_cast_testing.c"));

pub fn main() void {
    const result: c_int = basic_cast_test.run();
    std.debug.print("Result: {}\n", .{result});
}
