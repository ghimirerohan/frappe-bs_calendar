frappe.ui.form.on('Bulk Salary Structure Assignment', {
    refresh(frm) {
        NepaliFormDatePicker.init(frm, 'nepali_date', 'from_date');
    }
});
frappe.ui.form.on('Employee Attendance Tool', {
    refresh(frm) {
        NepaliFormDatePicker.init(frm, 'nepali_date', 'date');
    }
});
const NepaliFormDatePicker = {
    init(frm, bsField, adField) {
        const $input = $(frm.fields_dict[bsField].input);

        if ($input.hasClass('nepali-picker-initialized')) return;

        $input.addClass('nepali-picker-initialized');

        const inputEl = $input[0];
        const mode = (typeof get_ndp_mode === 'function') ? get_ndp_mode() : 'light';

        inputEl.NepaliDatePicker({
            dateFormat: 'YYYY-MM-DD',
            miniEnglishDates: true,
            mode: mode,
            animation: 'fade',
            onSelect: (d) => {
                const bsDate = d.value;
                $input.val(bsDate);
                frappe.model.set_value(frm.doctype, frm.docname, bsField, bsDate);

                try {
                    const adDate = NepaliFunctions.BS2AD(bsDate, 'YYYY-MM-DD', 'YYYY-MM-DD');
                    frappe.model.set_value(frm.doctype, frm.docname, adField, adDate + ' 00:00:00');
                } catch (err) {
                    console.error('BS to AD conversion error:', err);
                }
            }
        });
        $input.on('change', function () {
            const entered = $(this).val().trim();
            if (/^\d{4}-\d{2}-\d{2}$/.test(entered)) {
                try {
                    const adDate = NepaliFunctions.BS2AD(entered, 'YYYY-MM-DD', 'YYYY-MM-DD');
                    frappe.model.set_value(frm.doctype, frm.docname, adField, adDate + ' 00:00:00');
                } catch (err) {
                    console.error('Invalid manual BS date:', err);
                    $(this).val('');
                }
            } else {
                $(this).val('');
            }
        });
    }
};
