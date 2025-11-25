import frappe

def load_nepali_date(doc, method):
    if not hasattr(doc, "nepali_date") or not hasattr(doc, "posting_date"):
        return

    posting_date_str = str(doc.posting_date).strip()
    nepali_date_str = str(doc.nepali_date).strip() if doc.nepali_date else ""

    if nepali_date_str and posting_date_str != nepali_date_str:
        doc.nepali_date = None
