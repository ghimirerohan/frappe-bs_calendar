import frappe
from frappe import _

def create_custom_fields():
    custom_fields = {
        "User": [
            {"fieldname": "use_ad_date", "label": "Use Ad Date", "fieldtype": "Check", "insert_after": "username",
            "description": "<b>Disclaimer:</b> Checking this means you prefer using the default date picker (AD format) as your preferred format."},
        ],
        "Expense Claim": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", 'allow_on_submit': 1},
        ],
        "Salary Slip": [
            {"fieldname": "nepali_start_date", "label": "Nepali Start Date", "fieldtype": "Data", "insert_after": "start_date", "allow_on_submit": 1},
            {"fieldname": "nepali_end_date", "label": "Nepali End Date", "fieldtype": "Data", "insert_after": "end_date", "allow_on_submit": 1},
        ],
        "Attendance": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "attendance_date", "allow_on_submit": 1},
        ],
        "Fiscal Year": [
            {"fieldname": "nepali_year_start_date", "label": "Nepali Year Start Date", "fieldtype": "Data", "insert_after": "year_start_date", "allow_on_submit": 1},
            {"fieldname": "nepali_year_end_date", "label": "Nepali Year end Date", "fieldtype": "Data", "insert_after": "year_end_date", "allow_on_submit": 1}
        ],
        "Holiday List":[
            {"fieldname": "nepali_from_date", "label": "Nepali From Date", "fieldtype": "Data", "insert_after": "total_holidays", "allow_on_submit": 1},
            {"fieldname": "nepali_to_date", "label": "Nepali To Date", "fieldtype": "Data", "insert_after": "nepali_from_date", "allow_on_submit": 1}
        ],
        "Holiday": [
            {"fieldname":"nepali_date_holiday", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "holiday_date", "allow_on_submit": 1}
        ],
        "Leave Allocation":[
            {"fieldname": "from_nepali_date_leave_allocation", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_nepali_date_leave_allocation", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1}
        ],
        "Leave Application": [
            {"fieldname": "from_nepali_date_leave_application", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_nepali_date_leave_application", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1},
        ],
        "Purchase Order":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Purchase Receipt":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],  
        "Purchase Invoice":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1},
        ],
        "Sales Order":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Sales Invoice": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1},
            {"fieldname": "customs_declaration_date_bs", "label": "Customs Export Declaration Date BS", "fieldtype": "Data", "insert_after": "customs_declaration_date", "allow_on_submit": 1}
        ],
        "Delivery Note":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Material Request":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Payment Request":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Payment Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1},
        ],
        "GL Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Stock Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1} 
        ],
        "Journal Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "naming_series", "allow_on_submit": 1} 
        ],
        "Request for Quotation":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1} 
        ],
        "Supplier Quotation":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "supplier", "allow_on_submit": 1} 
        ],
        "Quotation":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1} 
        ],
        "Blanket Order":[
            {"fieldname": "from_nepali_date", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_nepali_date", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1}
        ],
        "Landed Cost Voucher": [
            {"fieldname": "nepali_date", "label": "NepalI Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Asset": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1},
        ],
        "Asset Repair": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1} 
        ],
        "Asset Movement":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Asset Value Adjustment":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "date", "allow_on_submit": 1},
        ],
        "Asset Capitalization":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "POS Opening Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1} 
        ],
        "POS Closing Entry":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "period_end_date", "allow_on_submit": 1} 
        ],
        "Loyalty Program":[
            {"fieldname": "from_nepali_date", "label": "From Date BS", "fieldtype": "Data", "insert_after": "customer_territory", "allow_on_submit": 1},
            {"fieldname": "to_nepali_date", "label": "To Date BS", "fieldtype": "Data", "insert_after": "from_nepali_date", "allow_on_submit": 1}
        ],
        "Promotional Scheme":[
            {"fieldname": "valid_from_bs", "label": "Valid From BS", "fieldtype": "Data", "insert_after": "valid_from", "allow_on_submit": 1},
            {"fieldname": "valid_to_bs", "label": "Valid To BS", "fieldtype": "Data", "insert_after": "valid_upto", "allow_on_submit": 1}
        ],
        "Pricing Rule":[
            {"fieldname": "valid_from_bs", "label": "Valid From BS", "fieldtype": "Data", "insert_after": "valid_from", "allow_on_submit": 1},
            {"fieldname": "valid_to_bs", "label": "Valid To BS", "fieldtype": "Data", "insert_after": "valid_upto", "allow_on_submit": 1}
        ],
        "Coupon Code":[
            {"fieldname": "valid_from_bs", "label": "Valid From BS", "fieldtype": "Data", "insert_after": "valid_from", "allow_on_submit": 1},
            {"fieldname": "valid_to_bs", "label": "Valid To BS", "fieldtype": "Data", "insert_after": "valid_upto", "allow_on_submit": 1}
        ],
        "Serial No":[
            {"fieldname": "warranty_expiry_date_bs", "label": "Warranty Expiry Date BS", "fieldtype": "Data", "insert_after": "warranty_expiry_date", "allow_on_submit": 1},
            {"fieldname": "amc_expiry_date_bs", "label": "AMC Expiry Date BS", "fieldtype": "Data", "insert_after": "amc_expiry_date", "allow_on_submit": 1}
        ],
        "Batch":[
            {"fieldname": "expiry_date_bs", "label": "Expiry Date BS", "fieldtype": "Data", "insert_after": "expiry_date", "allow_on_submit": 1},
            {"fieldname": "manufacturing_date_bs", "label": "Manufacturing Date BS", "fieldtype": "Data", "insert_after": "manufacturing_date", "allow_on_submit": 1}
        ],
        "Installation Note":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "inst_date", "allow_on_submit": 1} 
        ],
        "Stock Reconciliation":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Quality Inspection":[
            {"fieldname": "report_date_bs_quality_inspection", "label": "Report Date BS", "fieldtype": "Data", "insert_after": "report_date", "allow_on_submit": 1}
        ],
        "Quick Stock Balance":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "date", "allow_on_submit": 1}
        ],
        "Payroll Entry": [
            {"fieldname": "nepali_start_date", "label": "Start Date BS", "fieldtype": "Data", "insert_after": "start_date", "allow_on_submit": 1},
            {"fieldname": "nepali_end_date", "label": "End Date BS", "fieldtype": "Data", "insert_after": "end_date", "allow_on_submit": 1}
        ],
        "Income Tax Slab":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "effective_from", "allow_on_submit": 1},
        ],
        "Payroll Period": [
            {"fieldname": "nepali_start_date", "label": "Start Date BS", "fieldtype": "Data", "insert_after": "start_date", "allow_on_submit": 1},
            {"fieldname": "nepali_end_date", "label": "End Date BS", "fieldtype": "Data", "insert_after": "end_date", "allow_on_submit": 1}
        ],
        "Salary Structure Assignment": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
        ],
        "Bulk Salary Structure Assignment": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_payable_account", "allow_on_submit": 1}           
        ],
        "Salary Withholding":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Additional Salary":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_date", "allow_on_submit": 1}
        ],
        "Employee Incentive":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_date", "allow_on_submit": 1}
        ],
        "Retention Bonus":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "bonus_payment_date", "allow_on_submit": 1}
        ],
        "Employee Tax Exemption Declaration":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_period", "allow_on_submit": 1}
        ],
        "Employee Tax Exemption Proof Submission":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_period", "allow_on_submit": 1}
        ],
        "Employee Benefit Application":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_period", "allow_on_submit": 1}
        ],
        "Employee Benefit Claim":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "payroll_period", "allow_on_submit": 1},
        ],
        "Compensatory Leave Request": [
            {"fieldname": "work_from_date_bs", "label": "Work From Date BS", "fieldtype": "Data", "insert_after": "work_from_date", "allow_on_submit": 1},
            {"fieldname": "work_end_date_bs", "label": "Work End Date BS", "fieldtype": "Data", "insert_after": "work_end_date", "allow_on_submit": 1}
        ],
        "Attendance Request": [
            {"fieldname": "from_date_bs", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_date_bs", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1}
        ],
        "Employee Advance": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Job Offer": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "offer_date", "allow_on_submit": 1}
        ],
        "Employee Referral": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "date", "allow_on_submit": 1}
        ],
        "Shift Assignment": [
            {"fieldname": "start_date_bs", "label": "Start Date BS", "fieldtype": "Data", "insert_after": "start_date", "allow_on_submit": 1},
            {"fieldname": "end_date_bs", "label": "End Date BS", "fieldtype": "Data", "insert_after": "end_date", "allow_on_submit": 1}
        ],
        "Shift Request": [
            {"fieldname": "from_date_bs", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_date_bs", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1}
        ],
        "Shift Assignment Tool": [
            {"fieldname": "start_date_bs", "label": "Start Date BS", "fieldtype": "Data", "insert_after": "start_date", "allow_on_submit": 1},
            {"fieldname": "end_date_bs", "label": "End Date BS", "fieldtype": "Data", "insert_after": "end_date", "allow_on_submit": 1}
        ],
        "Employee Attendance Tool":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "date", "allow_on_submit": 1},
        ],
        "Upload Attendance":[
            {"fieldname": "att_fr_date_bs", "label": "Attendance From Date BS", "fieldtype": "Data", "insert_after": "att_fr_date", "allow_on_submit": 1},
            {"fieldname": "column_break", "label": "", "fieldtype": "Column Break", "insert_after": "att_fr_date_bs"},
            {"fieldname": "att_to_date_bs", "label": "Attendance To Date BS", "fieldtype": "Data", "insert_after": "att_to_date", "allow_on_submit": 1},
        ],
        "Leave Period": [
            {"fieldname": "from_date_bs", "label": "From Date BS", "fieldtype": "Data", "insert_after": "from_date", "allow_on_submit": 1},
            {"fieldname": "to_date_bs", "label": "To Date BS", "fieldtype": "Data", "insert_after": "to_date", "allow_on_submit": 1}
        ],
        "Leave Policy Assignment":[
            {"fieldname": "effective_from_bs", "label": "Effective From BS", "fieldtype": "Data", "insert_after": "effective_from", "allow_on_submit": 1},
            {"fieldname": "effective_to_bs", "label": "Effective To BS", "fieldtype": "Data", "insert_after": "effective_to", "allow_on_submit": 1}
        ],
        "Leave Control Panel":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "leave_policy", "allow_on_submit": 1}
        ],
        "Leave Encashment":[
            {"fieldname": "encashment_date_bs", "label": "Encashment Date BS", "fieldtype": "Data", "insert_after": "encashment_date", "allow_on_submit": 1},
        ],
        "Period Closing Voucher": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "transaction_date", "allow_on_submit": 1}
        ],
        "Invoice Discounting":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Dunning":[
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "Process Deferred Accounting": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1}
        ],
        "POS Invoice": [
            {"fieldname": "nepali_date", "label": "Nepali Date", "fieldtype": "Data", "insert_after": "posting_date", "allow_on_submit": 1},
        ]
    }

    created_fields = [] 

    for doctype_name, fields in custom_fields.items():
        for field in fields:
            if not frappe.db.exists("Custom Field", {"dt": doctype_name, "fieldname": field["fieldname"]}):
                custom_field = frappe.get_doc({
                    "doctype": "Custom Field",
                    "dt": doctype_name,
                    "module": "BS Calendar",
                    **field
                })
                custom_field.save()
                frappe.msgprint(_(f"Custom field '{field['label']}' added successfully to {doctype_name}!"))
                created_fields.append({"dt": doctype_name, "fieldname": field["fieldname"]})
            else:
                frappe.msgprint(_(f"Field '{field['label']}' already exists in {doctype_name}."))

    return created_fields
