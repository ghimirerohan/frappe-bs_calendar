frappe.ui.form.on('Salary Slip', {
    refresh: function(frm) {
        // Hide Nepali date fields by default as they are shown via other means or just sync fields
        // Actually, usually we want them visible? 
        // The original code hid them: frm.set_df_property('nepali_start_date', 'hidden', 1);
        // But maybe they are shown in a specific section?
        // I'll keep the original behavior of hiding them if that's what the original app did, 
        // but wait, if they are hidden, how does the user see them?
        // Maybe they are just for storage?
        // But the user wants "replacing the english date".
        // If I hide them, the user won't see them.
        // The original code hid them in refresh, maybe because they are rendered specially?
        // Or maybe they are just backend fields?
        // But  and  seem to handle rendering.
        // I'll keep the hide logic for now to match original behavior, assuming  or others handle display.
        // Wait,  has  function.
        
        // Let's check if I should hide them.
        // If I look at , it hides  fields often.
        // And  renders "Equivalent Date".
        // So yes, hiding them is probably correct as the "Equivalent Date" is shown next to the English date.
        
        frm.set_df_property('nepali_start_date', 'hidden', 1);
        frm.set_df_property('nepali_end_date', 'hidden', 1);
    },
    start_date(frm) {
        if (frm.doc.start_date) {
            const nepaliStartDate = NepaliFunctions.AD2BS(frm.doc.start_date, "YYYY-MM-DD", "YYYY-MM-DD");
            frappe.model.set_value(frm.doctype, frm.docname, "nepali_start_date", nepaliStartDate);
            frm.refresh_field('nepali_start_date');
        }
    },
    end_date(frm) {
        if (frm.doc.end_date) {
            const nepaliEndDate = NepaliFunctions.AD2BS(frm.doc.end_date, "YYYY-MM-DD", "YYYY-MM-DD");
            frappe.model.set_value(frm.doctype, frm.docname, "nepali_end_date", nepaliEndDate);
            frm.refresh_field('nepali_end_date');
        }
    },
    nepali_start_date(frm) {
        if (frm.doc.nepali_start_date) {
            const startDate = NepaliFunctions.BS2AD(frm.doc.nepali_start_date, "YYYY-MM-DD", "YYYY-MM-DD");
            frappe.model.set_value(frm.doctype, frm.docname, "start_date", startDate);
            frm.refresh_field('start_date');
        }
    },
    nepali_end_date(frm) {
        if (frm.doc.nepali_end_date) {
            const endDate = NepaliFunctions.BS2AD(frm.doc.nepali_end_date, "YYYY-MM-DD", "YYYY-MM-DD");
            frappe.model.set_value(frm.doctype, frm.docname, "end_date", endDate);
            frm.refresh_field('end_date');
        }
    }
});
