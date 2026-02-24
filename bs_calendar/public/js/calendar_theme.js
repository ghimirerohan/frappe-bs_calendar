/*
 * Provides get_ndp_mode() for NepaliDatePicker v5's built-in dark/light mode.
 * The v5 library applies .ndp-light / .ndp-dark classes internally based on
 * the `mode` option passed during initialization.
 */
function get_ndp_mode() {
    const theme = frappe.boot?.user?.theme?.toLowerCase() || "light";
    return theme === "dark" ? "dark" : "light";
}
