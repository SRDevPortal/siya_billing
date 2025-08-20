# Siya Billing (Frappe App)

Install on a Frappe/ERPNext site:

```bash
bench get-app siya_billing https://github.com/SRDevPortal/siya_billing.git
bench --site <yoursite> install-app siya_billing

new line

### Siya Billing

Auto create Patient/Customer/Address/Contact, Sales Invoice & Payment

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app siya_billing
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/siya_billing
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit