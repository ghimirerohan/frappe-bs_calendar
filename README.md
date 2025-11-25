<p align="center">
  <img src="https://img.shields.io/badge/Frappe-v15-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTUtMTAtNXpNMiAxN2wxMCA1IDEwLTV2LTJMMTIgMTUgMiAxMHY3eiIvPjwvc3ZnPg==" />
  <img src="https://img.shields.io/badge/ERPNext-Compatible-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🇳🇵_Nepal-BS_Calendar-c41e3a?style=for-the-badge" />
</p>

<h1 align="center">
  📅 BS Calendar
  <br/>
  <sub>Bikram Sambat Date Integration for Frappe/ERPNext</sub>
</h1>

<p align="center">
  <strong>🔥 Seamlessly integrate Nepali Bikram Sambat (BS) calendar into your Frappe/ERPNext ecosystem 🔥</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-supported-doctypes">Doctypes</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## ✨ Features

### 🗓️ Dual Calendar Support
Switch effortlessly between **AD (Anno Domini)** and **BS (Bikram Sambat)** date formats based on user preference.

### 🎨 Beautiful Nepali Date Picker
- Native Nepali date picker integration
- Automatic AD ↔ BS conversion display
- Real-time equivalent date preview
- Elegant styling that matches Frappe's design

### 📊 Extensive Doctype Coverage
BS date support for **50+ ERPNext doctypes** including:
- Accounting (Sales Invoice, Purchase Invoice, Payment Entry, Journal Entry)
- HR (Leave Application, Attendance, Salary Slip, Payroll Entry)
- Stock (Stock Entry, Stock Reconciliation, Delivery Note)
- Buying/Selling (Purchase Order, Sales Order, Quotation)
- Assets (Asset, Asset Movement, Asset Repair)
- And many more...

### 💼 HRMS Integration
- **Monthly BS Leave Allocation**: Automatically allocate leaves at the start of each BS month
- **Leave Policy Override**: Custom leave policy assignment supporting BS cycles
- **BS Month-wise Leave Tracking**: Track and manage leaves based on Nepali calendar months

### 🎯 Smart Features
- **User Preference**: Each user can choose their preferred date format
- **Report Filters**: BS date support in report filters
- **Bulk Operations**: Bulk update Nepali dates for sales invoices
- **Fiscal Year Support**: BS date integration for fiscal year management

---

## 🚀 Installation

### Prerequisites
- Frappe Framework (v15.x)
- ERPNext (optional, for full feature set)
- HRMS (optional, for leave management features)

### Quick Install

```bash
# Navigate to your bench directory
cd $PATH_TO_YOUR_BENCH

# Get the app from repository
bench get-app https://github.com/your-org/bs_calendar.git --branch main

# Install on your site
bench --site your-site.local install-app bs_calendar

# Run migrations
bench --site your-site.local migrate

# Build assets
bench build --app bs_calendar

# Restart bench
bench restart
```

### Post-Installation Setup

The app automatically creates necessary custom fields on installation. To verify:

```bash
bench --site your-site.local console
```

```python
>>> frappe.get_all("Custom Field", filters={"module": "BS Calendar"})
```

---

## 💡 Usage

### Setting User Date Preference

1. Navigate to **User** doctype
2. Find the `use_ad_date` checkbox
3. **Checked** = Use standard AD dates with BS equivalent display
4. **Unchecked** = Use Nepali BS date picker with AD equivalent display

### Date Display Behavior

| User Preference | Date Input | Display |
|-----------------|------------|---------|
| AD Date (default) | Standard calendar | Shows BS equivalent below |
| BS Date | Nepali date picker | Shows AD equivalent below |

### Monthly Leave Allocation (BS)

For HR Managers to allocate leaves based on BS months:

```python
from bs_calendar.custom_code.leave_allocation.monthly_leave_bs import allocate_monthly_leave_bs

# Allocate leaves for Baisakh 2081
allocate_monthly_leave_bs(
    bs_year=2081,
    bs_month=1,
    leave_types=["Casual Leave", "Sick Leave"]
)
```

### Leave Type Configuration

Enable BS monthly allocation in Leave Type:
1. Go to **Leave Type**
2. Enable `Allocate Leave on Start of BS Month`
3. Set `BS Monthly Allocation Amount`
4. Set `Max Leaves Allowed`

---

## 📋 Supported Doctypes

<details>
<summary><strong>💰 Accounting & Finance</strong></summary>

- Sales Invoice
- Purchase Invoice
- Payment Entry
- Journal Entry
- Period Closing Voucher
- Invoice Discounting
- Dunning
- Process Deferred Accounting
- POS Invoice
- POS Opening/Closing Entry

</details>

<details>
<summary><strong>📦 Stock & Inventory</strong></summary>

- Stock Entry
- Stock Reconciliation
- Material Request
- Delivery Note
- Purchase Receipt
- Serial No
- Batch
- Installation Note
- Quality Inspection
- Quick Stock Balance

</details>

<details>
<summary><strong>🛒 Buying & Selling</strong></summary>

- Sales Order
- Purchase Order
- Quotation
- Request for Quotation
- Supplier Quotation
- Blanket Order
- Landed Cost Voucher

</details>

<details>
<summary><strong>👥 Human Resources</strong></summary>

- Leave Application
- Leave Allocation
- Attendance
- Attendance Request
- Expense Claim
- Employee Advance
- Salary Slip
- Payroll Entry
- Leave Period
- Leave Policy Assignment
- Leave Control Panel
- Leave Encashment
- Shift Assignment/Request
- Employee Benefit Claim/Application
- And more...

</details>

<details>
<summary><strong>🏢 Assets</strong></summary>

- Asset
- Asset Repair
- Asset Movement
- Asset Value Adjustment
- Asset Capitalization

</details>

<details>
<summary><strong>🎁 Promotions & Pricing</strong></summary>

- Loyalty Program
- Promotional Scheme
- Pricing Rule
- Coupon Code

</details>

---

## 🏗️ Project Structure

```
bs_calendar/
├── bs_calendar/
│   ├── custom_code/
│   │   └── leave_allocation/
│   │       └── monthly_leave_bs.py    # BS-based leave allocation
│   ├── public/
│   │   ├── css/
│   │   │   ├── calendar.css           # Main calendar styles
│   │   │   ├── calendar_theme.css     # Theme customization
│   │   │   ├── date.css               # Date field styles
│   │   │   └── doctype.css            # Doctype-specific styles
│   │   └── js/
│   │       ├── nepali_date.js         # Core BS date picker
│   │       ├── bs_date.js             # BS date utilities
│   │       ├── bs_module.js           # Module initialization
│   │       ├── formatter.js           # Date formatting
│   │       ├── holiday_list.js        # Holiday list integration
│   │       ├── hrms_bs_date.js        # HRMS specific dates
│   │       ├── payroll_bs_date.js     # Payroll date handling
│   │       ├── salary_slip.js         # Salary slip BS dates
│   │       └── ...                    # Other utilities
│   ├── hooks.py                       # App hooks & configuration
│   ├── custom_field.py                # Custom field definitions
│   └── utils.py                       # Utility functions
├── pyproject.toml
└── README.md
```

---

## 🤝 Contributing

We welcome contributions! This app uses `pre-commit` for code quality.

### Setup Development Environment

```bash
# Clone the repository
cd apps/bs_calendar

# Install pre-commit hooks
pip install pre-commit
pre-commit install
```

### Code Quality Tools

| Tool | Purpose |
|------|---------|
| **Ruff** | Python linting & formatting |
| **ESLint** | JavaScript linting |
| **Prettier** | Code formatting |
| **pyupgrade** | Python syntax upgrades |

### Running Tests

```bash
bench --site your-site.local run-tests --app bs_calendar
```

---

## 📜 Changelog

### v1.0.0
- ✅ Initial release
- ✅ Nepali date picker integration
- ✅ Support for 50+ doctypes
- ✅ HRMS leave allocation with BS months
- ✅ User preference for AD/BS dates

---

## 📄 License

MIT License - see [LICENSE](license.txt) for details.

---

## 🏢 About

<p align="center">
  <strong>Developed with ❤️ by <a href="https://yarsalabs.com">Yarsa Labs Pvt. Ltd.</a></strong>
  <br/>
  <sub>Making ERPNext work for Nepal 🇳🇵</sub>
</p>

<p align="center">
  <a href="mailto:support@yarsalabs.com">📧 support@yarsalabs.com</a>
</p>

---

<p align="center">
  <strong>⭐ If you find this useful, please star this repository! ⭐</strong>
</p>
