# Contributing to Core Promo

Thank you for considering contributing to Core Promo!

## Issues

1. **Search existing issues** before creating a new one. Duplicates will be closed and directed to the original.
2. **Report issues separately.** Do not combine multiple unrelated problems into a single report.
3. **Be concise.** Use bullet points and screenshots where possible.
4. **Include versions** for Frappe, ERPNext and Core Promo. Developers do not have access to your environment, so the more relevant information you provide, the faster the issue can be fixed.

The issue tracker is not the right place for general questions or discussions. Please use the [forum](https://discuss.frappe.io/) instead.

## Development Setup

Follow the [Development Setup](../README.md#development-setup) section in the README to get a local bench running with ERPNext and Core Promo installed.

## Code Style

This app uses [`pre-commit`](https://pre-commit.com/) for linting and formatting. Please install and enable it so checks run locally before every commit:

```bash
cd apps/core_promo
pre-commit install
```

Pre-commit runs ruff (lint + format), prettier, and several sanity checks (YAML/JSON/TOML validity, merge conflicts, trailing whitespace). The same checks run on every pull request via the Linters workflow.

Conventions:

- Tabs for indentation, double quotes, 110 character line limit (enforced by ruff).
- All business logic and validations belong on the server side.
- Use `frappe._()` for user-facing strings.

## Tests

Run the test suite before submitting a pull request:

```bash
bench --site <site> run-tests --app core_promo
```

Add or update tests for every behaviour change. Bug fixes should include a test that fails without the fix.

## Pull Requests

1. Send pull requests to the `main` branch only.
2. Follow the [Pull Request Checklist](https://github.com/frappe/erpnext/wiki/Pull-Request-Checklist) and [Contribution Guidelines](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines).
3. Put `closes #XXXX` in your PR description to auto-close the issue it fixes.
4. PRs that change Python files without touching any tests will be labelled `needs-tests` automatically.

## Security

Do not report security vulnerabilities through public issues. See [SECURITY.md](../SECURITY.md).
