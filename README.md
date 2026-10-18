# Password Strength Checker

A small command-line Python program that checks whether a password meets a
basic set of strength requirements.

## Requirements

- Python 3
- No third-party packages

## Run

From this folder, run:

```powershell
python password-strength-checker.py
```

Enter a password when prompted. The checker reports the first requirement that
is not met, or confirms that the password passes all current checks.

## Current checks

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one character from `!@#$%^&*()-+`

## Merits

- The validation logic is kept in a dedicated function, so it can be reused
  independently of the command-line interface.
- The checks are short and readable, making the program easy to understand and
  maintain.
- Regular expressions provide concise checks for character categories.
- The `if __name__ == "__main__"` guard allows the module to be imported without
  immediately prompting for input.
- The project uses only Python's standard library.

## Areas for improvement

- **Broaden special-character handling:** The accepted characters are limited
  to a fixed set. Consider defining the accepted policy explicitly and testing
  punctuation and other symbols against it.
- **Report all unmet rules:** The function currently returns only the first
  failure. Returning a list of unmet requirements could help users improve
  their password in one attempt.
- **Add automated tests:** Tests should cover each rule, boundary lengths,
  passwords that satisfy all rules, and input edge cases.
- **Clarify whitespace policy:** Decide whether leading and trailing spaces are
  valid password characters. Avoid silently trimming them unless that is an
  intentional part of the policy.
- **Improve input handling:** The function assumes it receives a string.
  Consider documenting that contract or validating input explicitly if the
  function will be used by other code.
- **Set expectations about the result:** This program checks a small set of
  composition rules; it does not estimate resistance to guessing or determine
  whether a password has appeared in a breach. It should not be treated as a
  complete security assessment.

## Contributing

For changes, keep the requirements clear and add tests for new or changed
validation behavior. Do not include real passwords in examples, tests, or
repository history.
