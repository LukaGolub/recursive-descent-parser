# Recursive-Descent Parser (Grammar over {a, b, c})

A Python recursive-descent parser for a small context-free grammar over the alphabet `{a, b, c}`, which validates an input string and prints the sequence of grammar rules (nonterminal expansions) applied during parsing.

## Description

This program implements a predictive recursive-descent parser with four nonterminals (`S`, `A`, `B`, `C`), each corresponding to a Python function of the same name. The parser reads a string made up of the characters `a`, `b`, and `c` from standard input, then attempts to derive it starting from the grammar's start symbol `S`, consuming one input character at a time as it matches grammar rules. As it goes, it prints the name of every nonterminal it expands, showing the derivation trace. If the string is successfully parsed and every character is consumed, it reports success (`DA`, Croatian for "yes"); otherwise it reports failure (`NE`, "no").

## Grammar (as implemented)

Based on the parsing functions:

```
S -> a A B
   | b B A

A -> b C
   | a

B -> c c S b c
   | ε

C -> A A
```

- `S`, `A`, `B`, `C` are nonterminals; `a`, `b`, `c` are terminal symbols.
- `A` and `S` require a matching terminal to proceed; if the current input character doesn't match any expected alternative, a `ParseError` is raised and parsing fails.
- `B` only proceeds through its `c c S b c` branch if the current character is `c` at each expected step; if any expected `c`/`b` isn't present, it silently stops matching further (this is a quirk of the implementation rather than a formal grammar rule — see "Known Issues" below).

## Requirements

- Python 3.7+
- No external dependencies (standard library only: `sys`)

## Usage

```bash
python parser.py
```

The program reads a single line from standard input containing only the characters `a`, `b`, and `c`:

```bash
echo "abab" | python parser.py
```

or interactively:

```
$ python parser.py
abab
```

If the input line contains any character outside `{a, b, c}`, the program immediately prints `FAIL` and exits without attempting to parse.

## Output

As parsing proceeds, the program prints each nonterminal name as it's expanded (with no separators), e.g.:

```
SABCAAB
```

followed by the final verdict on a new line:

```
DA   # the string was successfully parsed (accepted)
NE   # the string was rejected (parse error, or input left over after parsing)
```

## Known Issues

- `B`'s implementation doesn't have an explicit "else" branch for a failed match — if the current character isn't `c` where expected, `B` just stops without consuming anything or raising an error, rather than treating it as strictly optional (`ε`) or as a parse failure. This means some inputs may be silently accepted or rejected in ways that don't perfectly match a formally specified grammar; treat the grammar listed above as a best-effort reconstruction from the code's control flow rather than a verified specification.
- The parser doesn't explicitly reject leftover/unmatched trailing input inside `S`/`A`/`B`/`C` — the overall success check only happens once at the end, by checking whether the current lookahead character is the newline terminator.
