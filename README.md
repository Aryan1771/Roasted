# Roasted

An educational, rule-based Python chatbot for the terminal. Roasted matches input against predefined phrases and provides arithmetic, practice questions, dictionary lookups, browser search, and date/time responses.

## Features

- Interactive conversation with keyword-based response selection.
- Multiplication tables, arithmetic expressions, and generated math questions.
- Word meanings, synonyms, and antonyms through PyDictionary.
- Browser-based Google search.
- Local CSV signup and login demonstration.

## Setup

Run these commands from the repository root with Python 3:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Follow the account prompts, then enter a message such as `hello`, `table 5`, or `calculate 2 + 3`. Use `Ctrl+C` to end the session. Dictionary queries need internet access and depend on the external service used by PyDictionary.

## Project layout

| File | Purpose |
| --- | --- |
| `main.py` | Conversation rules, account flow, and command handlers |
| `arithmetic.py` | Bounded arithmetic parser; rejects code, calls, and oversized expressions |
| `Login.csv` | Local account demonstration data |
| `requirements.txt` | Third-party Python dependencies |

## Tests

Run the arithmetic regression checks from the repository root:

```bash
python -m unittest discover -s tests
```

The suite checks precedence, negative values, division by zero, invalid syntax, code-execution attempts, and oversized expressions.

## Current limitations

This is a learning project, not a language model or production authentication system. The CSV account implementation stores passwords in plaintext; use demonstration credentials only. Arithmetic accepts numeric operators and parentheses with limits on expression size, exponents, and result magnitude. Account storage and command parsing require further hardening before wider distribution.

## License

See [LICENSE](LICENSE) for the GNU GPL v3 terms.
