# PlogLine

A `PlogLine` allows the capture a subset of information within an open `PlogBlock`. Generally a string to capture starts with a value, and ends with a _newline_. A single `PlogLine` applies this captured information to the referenced block line.

```py
from patterns import PlogLine, PlogBlock
ip_address = PlogLine('IP address:')
block.add_lines(ip=ip_address)
```

The keyword `ip` defines the name of the value in the result `dict` once parsed. More expressively:

```
line = PlogLine(ref='ip')
line.startswith('IP address:')
block.add_line(line)

blocks = plog.run()
{'ip': '10.243.14.48', 'device_id': 'SEP001F9EAB59F1'}
```

Any `PlogLine` with a `ref` will appear in the result block.

## API

Methods exist to help capture text and understand when to terminate a line. Under-the-hood regex is compiled and ran against the block

### start_of_line()

Asset the start of a given statement occurs in the pattern. If anything occurs within the match text before the `start_of_line` the line is not valid.

`PlogLine().start_of_line().then('$')`

For an easier API, this is wrapped into the PlogLine constructor.

`PlogLine('$')`

This is syntactically the same as `startswith('$')` as the first statement


### startswith(value)

Start a line with an explicit value, ensuring no text can exist before the captured value.

`PlogLine().startswith('$')`

is the same as:

`PlogLine('$')`


### anything_but(value)

Capture any value except the given value `PlogLine().anything_but('ERROR')`

### anything()

Capture any valid character without precedence. `PlogLine().find('Weeee').anything()`

This is useful for capturing a line without a return value - utilizing it as a marker or `header`/`footer`.

### end_of_line()

assert the end of the line for a given expression. Anything after this point is considered a captured value, or the termination of a line.

### multiline(bool)

Flat a line is spread over multiple lines.

Most methods assist manipulating a working regex string to execute on the block text. This method hints to the validator an open block will persist over many lines.

To note - a line may contain another _line_ underneath a caught position. The `multiline()` method ensures input strings such as streamed text may terminate early.

For capture of a string with terminators - such as a chat log, with `\n\r` or other terminators, `search_one_line(False)` produces a correct regex flag.

### add(value)

Concatenate a literal string to the pattern.

```
windows_drive = \b[a-z]:\\
PlogLine().word().add(windows_drive)
```

### any(value)

Find any part of the given string. `foo` will match `f` and `o`.

### maybe(value)

Apply a potential match of the given value. `PlogLine("foo").maybe("bar")`

### find(value)
### then(value)

Match the given value as regex or a literal string: `PlogLine().find("bar")`

### range(a[, b])

Apply a alphanumeric range using numbers or regex literal characters

numerical:

    >>> L().range(1).valid('1')
    True
    >>> L().range(1).valid('0')
    False
    >>> L().range(1).valid('2')
    False
    >>> L().range(1, 8).valid('2')
    True
    >>> L().range(1, 8).valid('9')
    False

lowercase:

    >>> L().range('a', 'z').valid('9')
    False
    >>> L().range('a', 'z').valid('b')
    True
    >>> L().range('a', 'z').valid('C')
    False

Bad expressions yield `sre.constants.error: Bad character range`


    File "C:\Python27\lib\re.py", line 251, in _compile
        raise error, v # invalid expression
    sre_constants.error: bad character range
    >>> L().range('a', 'Z').valid('C')


More interesting combinations are viable:

    L().range('A', 'Z', 0)

* Match a single character present in the list below `[A-Z0]`
    * A character in the range between "A" and "Z" (case sensitive) `A-Z`
    * The literal character "0" `0`


### line_break()

Expect a line break `\n` or `\r\n`

### tab()

Expect a tab string `\t`

### word(value)

Accept any ASCII letter, digit or underscore word with unlimited length.


### OR(value)

Test and entire negation to the already expressed line. `PlogLine().word("cake").OR("death")`

### with_any_case(bool)

A general modifier for the line, used at compile time on the entire line pattern.
Provide a boolean switch (default `True`) to action the modifier.

```py
PlogLine().find('unicorn').maybe(' ').with_any_case()
```

### search_one_line(bool)

Ensure the executed pattern occurs on a single line terminating with a standard `line_break()`. If `True`, `multiline()` may not function correctly.

A general modifier for the line, used at compile time on the entire line pattern.
Provide a boolean switch (default `False`) to action the modifier.

```py
PlogLine().find('unicorn').maybe(' ').search_one_line()
```

