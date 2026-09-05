<div align="center">
	<h2>Core Promo</h2>
	<p align="center">
		<p>Social media promotion tracking and payouts for ERPNext</p>
	</p>

[![CI](https://github.com/Sanjesh2254/Core-Promo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Sanjesh2254/Core-Promo/actions/workflows/ci.yml)
[![Linters](https://github.com/Sanjesh2254/Core-Promo/actions/workflows/linters.yml/badge.svg?branch=main)](https://github.com/Sanjesh2254/Core-Promo/actions/workflows/linters.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](license.txt)
</div>

<div align="center">
	<a href="https://github.com/Sanjesh2254/Core-Promo">Repository</a>
</div>

## Core Promo

Core Promo is a Frappe app that tracks social media promotion work on top of ERPNext Projects and Tasks. Promotion tasks (likes, retweets, comments, quote tweets) are logged per project, amounts are calculated automatically from configured project rates, and a project dashboard summarizes the work. A Telegram bot integration receives interaction events and logs them for reporting.

### Motivation

Social media promotion campaigns are run as a set of small repeated tasks (like, retweet, comment) across many projects, and contributors are paid per task at project-specific rates. Generic project tools do not capture this workflow, and spreadsheets quickly break down as projects and contributors grow.

ERPNext already has Projects, Tasks and accounting. Core Promo adds the promo-specific layer on top: task types, work logs with automatic amount calculation, project rate settings, interaction metrics and a dashboard, so promo work and payouts live in the same system as the rest of the business.

### Key Features

- **Task Work Log**: Log promotion work per project and task. Rates and amounts are computed automatically on save from the project's configured rate.
- **Payment Settings**: Map each project to its per-task rate in one place; every work log picks it up.
- **Promo Task Types**: Like, Retweet, Comment and Quote Tweet task types are created automatically on install and migrate.
- **Interaction Metrics**: Metrics captured from incoming interaction events, available for reporting.
- **Telegram Bot Integration**: A webhook receiver for Telegram bot events, configurable through Core Promo Settings (bot key, bot name, enable flag).
- **Project Dashboard**: A dedicated dashboard page summarizing promotion work across projects.
- **Task Extensions**: Custom fields on the ERPNext Task doctype, applied idempotently on install and migrate.

### Under the Hood

- [**Frappe Framework**](https://github.com/frappe/frappe): A full-stack web application framework written in Python and JavaScript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.

- [**ERPNext**](https://github.com/frappe/erpnext): Provides Projects and Tasks, which Core Promo extends with promotion tracking and payout calculation.

### Compatibility

| Frappe Version | ERPNext Version | Python Version |
| -------------- | --------------- | -------------- |
| v16            | v16             | 3.14+          |

## Production Setup

### Self Hosting

Install on an existing bench with ERPNext already set up:

```bash
bench get-app https://github.com/Sanjesh2254/Core-Promo --branch main
bench --site <site> install-app core_promo
```

## Development Setup

### Local

1. Set up bench by following the [Installation Steps](https://docs.frappe.io/framework/user/en/installation) and keep the server running
	```sh
	$ bench start
	```
2. In a separate terminal window, run the following commands:
	```sh
	$ bench new-site corepromo.localhost
	$ bench get-app erpnext
	$ bench --site corepromo.localhost install-app erpnext
	$ bench get-app https://github.com/Sanjesh2254/Core-Promo
	$ bench --site corepromo.localhost install-app core_promo
	$ bench --site corepromo.localhost add-to-hosts
	```
3. Access the site at `http://corepromo.localhost:8000/app`

## Learning and Community

1. [Frappe School](https://frappe.school) - Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. [Official documentation](https://docs.frappe.io/framework) - Extensive documentation for Frappe Framework.
3. [Discussion Forum](https://discuss.frappe.io/) - Engage with the community of ERPNext users and service providers.

## Contributing

1. [Contributing Guide](.github/CONTRIBUTING.md)
2. [Issue Guidelines](https://github.com/frappe/erpnext/wiki/Issue-Guidelines)
3. [Pull Request Requirements](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines)
4. Report security vulnerabilities privately: see [SECURITY.md](SECURITY.md)
5. Send pull requests to the `main` branch only.

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/core_promo
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## License

MIT. See [license.txt](license.txt).
