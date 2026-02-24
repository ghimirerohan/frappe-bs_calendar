frappe.provide('frappe.listview_settings');

const DatePickerConfig = {
    CALENDAR_FIELDS: ['nepali_date', 'from_nepali_date', 'to_nepali_date', 'nepali_start_date', 'nepali_end_date', 'nepali_year_start_date', 'nepali_year_end_date',
        'from_nepali_date_leave_allocation', 'to_nepali_date_leave_allocation', 'from_nepali_date_leave_application', 'to_nepali_date_leave_application', 'nepali_from_date', 'nepali_to_date',
        'valid_from_bs', 'valid_to_bs', 'warranty_expiry_date_bs', 'amc_expiry_date_bs', 'expiry_date_bs', 'manufacturing_date_bs', 'inst_date_note', 'report_date_bs_quality_inspection',
        'work_from_date_bs', 'work_end_date_bs', 'from_date_bs', 'to_date_bs', 'start_date_bs', 'end_date_bs', 'att_fr_date_bs', 'att_to_date_bs', 'effective_from_bs', 'effective_to_bs','encashment_date_bs',
    ],
    ENGLISH_DATE_FIELD: 'from_date',
    ENGLISH_TO_DATE_FIELD: 'to_date',
    NEPALI_DATE_FIELD: 'from_nepali_date',
    NEPALI_TO_DATE_FIELD: 'to_nepali_date',

    initializePickers: function(listview) {
        this.listview = listview;
        this.initializeAllDatePickers();
        this.setupEventListeners(listview);
        this.setupDateConversions(listview);
    },

    initializeAllDatePickers: function() {
        this.CALENDAR_FIELDS.forEach(fieldName => {
            setTimeout(() => this.initDatePicker(fieldName), 100);
        });
    },

    initDatePicker: function(fieldName) {
        $('input[data-fieldname="' + fieldName + '"]').each((_, element) => {
            const $input = $(element);
            if (!$input.hasClass('nepali-picker-initialized')) {
                this.setupDatePickerInput($input, fieldName);
            }
        });
    },

    setupDatePickerInput: function($input, fieldName) {
        $input.addClass('nepali-picker-initialized');

        const inputEl = $input[0];
        const mode = (typeof get_ndp_mode === 'function') ? get_ndp_mode() : 'light';

        inputEl.NepaliDatePicker({
            dateFormat: 'YYYY-MM-DD',
            miniEnglishDates: true,
            mode: mode,
            animation: 'fade',
            onSelect: (d) => {
                const nepaliDate = d.value;
                $input.val(nepaliDate);

                try {
                    const adDate = NepaliFunctions.BS2AD(nepaliDate, 'YYYY-MM-DD', 'DD-MM-YYYY');
                    if (fieldName === this.NEPALI_DATE_FIELD) {
                        this.updateEnglishDate(adDate);
                    } else if (fieldName === this.NEPALI_TO_DATE_FIELD) {
                        this.updateEnglishToDate(adDate);
                    }
                } catch (err) {
                    console.error('Nepali to English date conversion error:', err);
                }

                $input.trigger('change');
            }
        });
    },

    formatToYYYYMMDD: function(dateStr) {
        if (!dateStr) return '';

        if (dateStr.match(/^\d{4}-\d{2}-\d{2}$/)) {
            return dateStr;
        }
        else if (dateStr.match(/^\d{2}-\d{2}-\d{4}$/)) {
            let parts = dateStr.split('-');
            return `${parts[2]}-${parts[1]}-${parts[0]}`;
        }
        return dateStr;
    },

    setupEventListeners: function(listview) {
        listview.page.wrapper.on('click', '.filter-button', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });

        const observer = new MutationObserver(() => this.initializeAllDatePickers());
        observer.observe(document.body, { childList: true, subtree: true });

        $(document).on('click', '.filter-list, .filter-box, .filter-button', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });

        $(document).on('shown.bs.dropdown', '.filter-box', () => {
            setTimeout(() => this.initializeAllDatePickers(), 100);
        });

        $(document).on('click', `input[data-fieldname="${this.CALENDAR_FIELDS.join('"], input[data-fieldname="')}"]`,
            (e) => {
                const $input = $(e.target);
                if (!$input.hasClass('nepali-picker-initialized')) {
                    this.initializeAllDatePickers();
                }
            });
    },

    setupDateConversions: function(listview) {
        this.setupNepaliDatepicker(listview);
        this.setupEnglishDatepicker(listview);
        this.setupNepaliToDatepicker(listview);
        this.setupEnglishToDatepicker(listview);
    },

    setupNepaliDatepicker: function(listview) {
        const $nepaliInput = $(`input[data-fieldname="${this.NEPALI_DATE_FIELD}"]`);

        if ($nepaliInput.length) {
            $nepaliInput.on('change', (e) => {
                const nepaliDate = this.formatToYYYYMMDD($(e.target).val());
                if (!nepaliDate) return;

                try {
                    const adDate = NepaliFunctions.BS2AD(nepaliDate, 'YYYY-MM-DD', 'DD-MM-YYYY');
                    this.updateEnglishDate(adDate, listview);
                    this.applyDateRangeFilter(listview);
                } catch (err) {
                    console.error('Nepali date conversion error:', err);
                    $(e.target).val('');
                }
            });
        }
    },

    setupEnglishDatepicker: function(listview) {
        const $englishInput = $(`input[data-fieldname="${this.ENGLISH_DATE_FIELD}"]`);

        if ($englishInput.length) {
            $englishInput.on('change', (e) => {
                const englishDate = this.formatToYYYYMMDD($(e.target).val());
                if (!englishDate) return;

                try {
                    const nepaliDate = NepaliFunctions.AD2BS(englishDate, 'YYYY-MM-DD', 'YYYY-MM-DD');
                    this.updateNepaliDate(nepaliDate, listview);
                    this.applyDateRangeFilter(listview);
                } catch (err) {
                    console.error('English date conversion error:', err);
                    $(e.target).val('');
                }
            });
        }
    },

    setupNepaliToDatepicker: function(listview) {
        const $nepaliToInput = $(`input[data-fieldname="${this.NEPALI_TO_DATE_FIELD}"]`);

        if ($nepaliToInput.length) {
            $nepaliToInput.on('change', (e) => {
                const nepaliDate = this.formatToYYYYMMDD($(e.target).val());
                if (!nepaliDate) return;

                try {
                    const adDate = NepaliFunctions.BS2AD(nepaliDate, 'YYYY-MM-DD', 'DD-MM-YYYY');
                    this.updateEnglishToDate(adDate, listview);
                    this.applyDateRangeFilter(listview);
                } catch (err) {
                    console.error('Nepali to-date conversion error:', err);
                    $(e.target).val('');
                }
            });
        }
    },

    setupEnglishToDatepicker: function(listview) {
        const $englishToInput = $(`input[data-fieldname="${this.ENGLISH_TO_DATE_FIELD}"]`);

        if ($englishToInput.length) {
            $englishToInput.on('change', (e) => {
                const englishDate = this.formatToYYYYMMDD($(e.target).val());
                if (!englishDate) return;

                try {
                    const nepaliDate = NepaliFunctions.AD2BS(englishDate, 'YYYY-MM-DD', 'YYYY-MM-DD');
                    this.updateNepaliToDate(nepaliDate, listview);
                    this.applyDateRangeFilter(listview);
                } catch (err) {
                    console.error('English to-date conversion error:', err);
                    $(e.target).val('');
                }
            });
        }
    },

    updateNepaliDate: function(nepaliDate, listview) {
        const $nepaliInput = $(`input[data-fieldname="${this.NEPALI_DATE_FIELD}"]`);
        if ($nepaliInput.length) {
            $nepaliInput.val(nepaliDate);
        }
    },

    updateEnglishDate: function(englishDate, listview) {
        const $englishInput = $(`input[data-fieldname="${this.ENGLISH_DATE_FIELD}"]`);
        if ($englishInput.length) {
            $englishInput.val(englishDate);
        }
    },

    updateNepaliToDate: function(nepaliDate, listview) {
        const $nepaliToInput = $(`input[data-fieldname="${this.NEPALI_TO_DATE_FIELD}"]`);
        if ($nepaliToInput.length) {
            $nepaliToInput.val(nepaliDate);
        }
    },

    updateEnglishToDate: function(englishDate, listview) {
        const $englishToInput = $(`input[data-fieldname="${this.ENGLISH_TO_DATE_FIELD}"]`);
        if ($englishToInput.length) {
            $englishToInput.val(englishDate);
        }
    },

    applyDateRangeFilter: function(listview) {

        const fromEnglishDate = $(`input[data-fieldname="${this.ENGLISH_DATE_FIELD}"]`).val();
        const toEnglishDate = $(`input[data-fieldname="${this.ENGLISH_TO_DATE_FIELD}"]`).val();


        if (!fromEnglishDate || !toEnglishDate) {
            return;
        }

        try {
            const formatDateForFrappe = (dateStr) => {
                const [day, month, year] = dateStr.split('-');
                return `${year}-${month}-${day}`;
            };

            const fromDateFormatted = formatDateForFrappe(fromEnglishDate);
            const toDateFormatted = formatDateForFrappe(toEnglishDate);
            const dateRangeValue = [fromDateFormatted, toDateFormatted];
            const dateRangeFilters = [
                ["doctype", this.ENGLISH_DATE_FIELD, "between", dateRangeValue]
            ];

            if (listview.filter_area) {
                listview.filter_area.clear();
                listview.filter_area.add(dateRangeFilters);
                listview.refresh(dateRangeFilters);
            }

        } catch (error) {
            console.error('Error applying filter:', error);
            console.error('Error details:', error.message);
        }

    }
};

function initializeDatePickersForListView(doctype) {
    frappe.listview_settings[doctype] = {
        onload: function(listview) {
            DatePickerConfig.initializePickers(listview);
        }
    };

    $(document).ready(function() {
        setTimeout(() => {
            if (cur_list && cur_list.doctype === doctype) {
                if (cur_list.filter_area) {
                    cur_list.filter_area.clear();
                }
                DatePickerConfig.initializePickers(cur_list);
            }
        }, 1000);
    });
}

const doctypes = ['Purchase Invoice', 'GL Entry', 'Sales Invoice', 'Journal Entry', 'POS Invoice', 'Employee Attendance Tool'];
doctypes.forEach(doctype => initializeDatePickersForListView(doctype));
