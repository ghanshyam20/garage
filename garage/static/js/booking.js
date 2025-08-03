// JavaScript for dynamic price calculation on the booking page
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('booking-form');
    if (!form) return;
    const laborRate = parseFloat(form.getAttribute('data-labor-rate')) || 0;
    const hoursInput = document.getElementById('id_hours');
    const totalPriceEl = document.getElementById('total-price');
    function calculateTotal() {
        const hours = parseFloat(hoursInput.value) || 0;
        let serviceTotal = 0;
        document.querySelectorAll('input[name="services"]:checked').forEach(function (checkbox) {
            const price = parseFloat(checkbox.getAttribute('data-price')) || 0;
            serviceTotal += price;
        });
        const total = serviceTotal + hours * laborRate;
        totalPriceEl.textContent = total.toFixed(2);
    }
    hoursInput.addEventListener('input', calculateTotal);
    document.querySelectorAll('input[name="services"]').forEach(function (checkbox) {
        checkbox.addEventListener('change', calculateTotal);
    });
    calculateTotal();
});
