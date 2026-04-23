== checks value equality, meaning it compares whether two objects hold the same data. is, on the other hand, checks object identity, meaning it verifies whether both variables point to the exact same memory location.


Small integer interning: In CPython, integers from -5 to 256 (inclusive) are pre-cached as singleton objects. So any two variables assigned a value in that range will satisfy is.
Script vs REPL behavior for larger integers: Outside the cached range, whether is returns True depends on how the code is compiled. Single-file / pasted-as-a-block → compiler often interns identical literals (True). REPL line-by-line → separate compilation units, separate objects (False). This is a CPython implementation detail, not a language guarantee.
Why lists never behave like interned integers: Lists are mutable. If Python shared list objects silently, mutating one variable would corrupt the other. So every list literal always creates a fresh object. e = [1,2]; f = [1,2]; e is f is always False, regardless of how the code is run.
