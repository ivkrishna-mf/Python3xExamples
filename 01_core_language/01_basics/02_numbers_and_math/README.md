# Numbers: int, float, complex, Decimal, Fraction

**Introduced:** int/float 1.0 · unlimited ints merged 3.0 · `//` 2.2 · `Decimal` 2.4 · `Fraction` 2.6 · `1_000` 3.6

**In one line:** arbitrary-precision ints, IEEE floats, exact decimals and fractions, plus the `math` module.

## What it is
`int` never overflows. `/` is true division, `//` floor division, `%` modulo, `**` power,
`divmod()` both at once. `float` is binary floating point (0.1 + 0.2 != 0.3), so use
`decimal.Decimal` for money and `fractions.Fraction` for exact ratios.

## When to use
- `int` for counts/IDs, `float` for measurements/science.
- `Decimal` for currency and anything needing decimal rounding rules.
- `math.isclose()` to compare floats.

## When NOT to use
- Don't compare floats with `==`.
- Don't use `float` for money.

## Run
```bash
python examples.py
```
