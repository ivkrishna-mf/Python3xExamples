# secrets — Python 3.6 (PEP 506)

**In one line:** cryptographically strong random tokens, passwords and choices.

## What it is
`secrets` uses the OS's secure random source. Use it instead of `random` for anything
security-related.

## When to use
- Password-reset / email-verification / API tokens.
- Session IDs, CSRF tokens, one-time codes.
- Generating random passwords.
- Comparing secrets safely with `compare_digest` (constant-time).

## When NOT to use
- Simulations, games, sampling, shuffling test data → `random` is faster and seedable.

## Run
```bash
python examples.py
```
