# [medium/codebase_src_fmt.zig] - Chunk 0

**Type:** implementation
**Keywords:** union, struct, type inference, string formatting, error handling
**Symbols:** FormatArg, FormatArg.int, FormatArg.uint, FormatArg.f16, FormatArg.f32, FormatArg.f64, FormatArg.f80, FormatArg.f128, FormatArg.string, FormatArg.nullTerminatedString, FormatArg.formatFunction, FormatArg.err, FormatArg.anyFormatFunction, FormatArg.fromAnytype, Placeholder, Placeholder.specifierArg, Placeholder.fill, Placeholder.alignment, Placeholder.argPos, Placeholder.width, Placeholder.precision, Placeholder.parse
**Concepts:** formatted string parsing, format argument handling

## Summary
Defines a union for format arguments and a struct for parsing placeholders in formatted strings.

## Explanation
The chunk defines two main components: `FormatArg` and `Placeholder`. The `FormatArg` union can hold various types of values such as integers, floats, strings, custom formatting functions, and error sets. It includes a method `fromAnytype` to convert any type into a `FormatArg` based on its type information. For example, if the input is an integer or float, it will be converted accordingly; for pointers, it checks specific conditions like array size and child types to determine whether it should be treated as a string or null-terminated string. If the type has a custom format function declared (`format`), it uses that function; otherwise, it falls back to a generic format function that prints the value using `{any}` format specifier.

The `Placeholder` struct is used for parsing format specifiers in strings, extracting details like fill characters, alignment, width, and precision. It provides a static method `parse` to construct a `Placeholder` from a byte slice representing the format specifier. The `parse` method first extracts the argument position and specifier argument, then checks for an alignment character (left `<`, center `^`, right `>`), followed by optional width and precision parameters. If unexpected characters are encountered during parsing, it logs an error and returns an appropriate error code.

Specifically, the `Placeholder.parse` method works as follows:
- It first extracts the argument position using `parser.number()`.
- Then it reads the specifier argument until a colon (`:`) is found.
- If a fill character (e.g., `<`, `^`, `>`) or an alignment character (e.g., `<`, `^`, `>`) is present, it parses them accordingly. For example, if the next character after the colon is one of these characters, it consumes and processes it to determine the alignment.
- If a width parameter follows the alignment character, it reads that as well using `parser.number()`.
- Similarly, if a precision parameter follows a dot (`.`), it also parses that using `parser.number()`. 

If any unexpected characters are encountered during parsing (e.g., an extraneous trailing character after all parameters have been parsed), the method logs an error and returns `error.UnexpectedCharacter`.

## Code Example
```zig
pub inline fn fromAnytype(T: type, val: *const T) FormatArg {
		switch (@typeInfo(T)) {
			.comptime_int => return .{.int = val.*},
			.int => |int| {
				if (int.signedness == .unsigned) {
					return .{.uint = val.*};
				}
				return .{.int = val.*};
			},
			.comptime_float => return .{.f128 = val.*},
			.float => return @unionInit(FormatArg, @typeName(T), val.*),
			.pointer => |ptr| {
				if (ptr.size == .one and @typeInfo(ptr.child) == .array and @typeInfo(ptr.child).array.child == u8) return .{.string = val.*};
				if (ptr.size == .slice and ptr.child == u8) return .{.string = val.*};
				if (((ptr.size == .many and ptr.sentinel() != null) or ptr.size == .c) and ptr.child == u8) return .{.nullTerminatedString = val.*};

				if (ptr.size == .one) return .fromAnytype(ptr.child, val.*);
			},
			.@"struct", .@"enum", .@"union", .@"opaque" => {
				if (@hasDecl(T, "format")) {
					const typeErasedFormat = struct {
						fn typeErasedFormat(ptr: *const anyopaque, writer: *std.Io.Writer) std.Io.Writer.Error!void {
							return T.format(@as(*const T, @ptrCast(@alignCast(ptr))).*, writer);
						}
					}.typeErasedFormat;
					return .{.formatFunction = .{.val = val, .function = typeErasedFormat}};
				}
			},
			.error_set => return .{.err = val.*},
			else => {},
		}

		// Not sure what to do with the rest, so I'll just assume 'any'.
		const genericFormat = struct {
			fn genericFormat(ptr: *const anyopaque, writer: *std.Io.Writer) std.Io.Writer.Error!void {
				try writer.print("{any}", .{@as(*const T, @ptrCast(@alignCast(ptr))).*});
			}
		}.genericFormat;
		return .{.anyFormatFunction = .{.val = @ptrCast(val), .function = genericFormat}};
	}
```

## Related Questions
-  What types of values can be stored in a FormatArg?
-  How does the fromAnytype function determine which variant of FormatArg to use?
-  What are the fields of the Placeholder struct?
-  How is the parse method of Placeholder used?
-  What happens if an unexpected character is found while parsing a placeholder?
-  Can you explain how the alignment and fill characters are parsed in the Placeholder struct?

*Source: unknown | chunk_id: codebase_src_fmt.zig_chunk_0*
