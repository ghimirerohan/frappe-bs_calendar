app_name = "bs_calendar"
app_title = "BS Calendar"
app_publisher = "Yarsa Labs Pvt. Ltd."
app_description = "Nepali BS Calendar Integration for Frappe Framework"
app_email = "support@yarsalabs.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["/assets/bs_calendar/css/nepali_datepicker_v5.css",
                   "/assets/bs_calendar/css/date.css",
                   "/assets/bs_calendar/css/calendar_theme.css",
                   "/assets/bs_calendar/css/doctype.css"]

app_include_js = [
                 "/assets/bs_calendar/js/nepali_datepicker_v5.js",
                 "/assets/bs_calendar/js/calendar_theme.js",
                 "/assets/bs_calendar/js/nepali_date.js",
                 "/assets/bs_calendar/js/formatter.js",
                 "/assets/bs_calendar/js/report_filter.js",
                 "/assets/bs_calendar/js/employee_benefit_claim.js"
                 ]

doctype_js = {
    "User": "public/js/nepali_date.js",
    "Expense Claim": "public/js/bs_date.js",
    "Leave Application": "public/js/bs_date.js",
    "Holiday List": ["public/js/bs_date.js","public/js/holiday_list.js"],
    "Holiday": "public/js/holiday_list.js",
    "Leave Allocation": "public/js/bs_date.js",
    "Attendance": "public/js/bs_date.js",
    "Fiscal Year": "public/js/bs_date.js",
    "Stock Entry": "public/js/hrms_bs_date.js",
    "Material Request": "public/js/hrms_bs_date.js",
    "Purchase Invoice": ["public/js/bs_date.js", "public/js/utils.js"],
    "Purchase Order": "public/js/bs_date.js","Purchase Receipt": "public/js/bs_date.js",
    "Sales Order": "public/js/bs_date.js","Delivery Note": "public/js/bs_date.js",
    "Sales Invoice": ["public/js/bs_date.js", "public/js/utils.js"],
    "Payment Entry": "public/js/bs_date.js",
    "Journal Entry": ["public/js/bs_date.js", "public/js/utils.js"],
    "Request for Quotation": "public/js/bs_date.js","Supplier Quotation": "public/js/bs_date.js", "Quotation": "public/js/bs_date.js",
    "Blanket Order": "public/js/bs_date.js",
    "Landed Cost Voucher": "public/js/bs_date.js",
    "Asset": "public/js/bs_date.js", "Asset Repair": "public/js/bs_date.js", "Asset Movement": "public/js/bs_date.js", "Asset Value Adjustment": "public/js/bs_date.js", "Asset Capitalization": "public/js/bs_date.js",
    "POS Opening Entry": "public/js/bs_date.js", "POS Closing Entry": "public/js/bs_date.js",
    "Loyalty Program": "public/js/bs_date.js", "Promotional Scheme": "public/js/bs_date.js", "Pricing Rule": "public/js/bs_date.js", "Coupon Code": "public/js/bs_date.js",
    "Serial No": "public/js/bs_date.js", "Batch": "public/js/bs_date.js",
    "Installation Note": "public/js/bs_date.js", "Stock Reconciliation": "public/js/bs_date.js", "Quality Inspection": "public/js/bs_date.js", "Quick Stock Balance": "public/js/bs_date.js",
    "Payroll Entry": "public/js/payroll_bs_date.js", "Income Tax Slab": "public/js/payroll_bs_date.js", "Payroll Period": "public/js/payroll_bs_date.js", "Salary Structure Assignment": ["public/js/payroll_bs_date.js"], "Salary Withholding": "public/js/payroll_bs_date.js", "Additional Salary": "public/js/payroll_bs_date.js", "Employee Incentive": "public/js/payroll_bs_date.js", "Retention Bonus": "public/js/payroll_bs_date.js",
    "Employee Tax Exemption Proof Submission": "public/js/payroll_bs_date.js", "Employee Benefit Application": "public/js/payroll_bs_date.js", "Employee Benefit Claim": "public/js/hrms_bs_date.js",
    "Attendance Request": "public/js/hrms_bs_date.js", "Compensatory Leave Request": "public/js/hrms_bs_date.js", "Employee Advance": "public/js/hrms_bs_date.js", "Shift Assignment": "public/js/hrms_bs_date.js", "Shift Request": "public/js/hrms_bs_date.js", "Job Offer": "public/js/hrms_bs_date.js", "Employee Referral": "public/js/hrms_bs_date.js", "Shift Assignment Tool": "public/js/hrms_bs_date.js",
    "Upload Attendance": "public/js/hrms_bs_date.js", "Leave Period": "public/js/hrms_bs_date.js", "Leave Policy Assignment": "public/js/hrms_bs_date.js", "Leave Control Panel": "public/js/hrms_bs_date.js", "Leave Encashment": "public/js/hrms_bs_date.js",
    "Bulk Salary Structure Assignment": "public/js/bs_date.js", "Employee Attendance Tool": 'public/js/bs_date.js',
    "Period Closing Voucher": "public/js/bs_date.js", "Invoice Discounting": "public/js/bs_date.js", "Dunning": "public/js/bs_date.js", "Process Deferred Accounting": "public/js/bs_date.js", "POS Invoice": "public/js/bs_date.js",
    "Salary Slip": "public/js/salary_slip.js"
}

doctype_list_js = {
    "Leave Allocation": "public/js/utils.js",
    "Sales Invoice" : "public/js/bulk_update_nepali_date.js"
}

after_install = "bs_calendar.custom_field.create_custom_fields"

doc_events = {
    "Sales Invoice" : {
        "before_insert": "bs_calendar.utils.load_nepali_date",
    }
}

override_doctype_class = {
    "Leave Policy Assignment": "bs_calendar.custom_code.leave_allocation.monthly_leave_bs.LeavePolicyAssignment"
}
