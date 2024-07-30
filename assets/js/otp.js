document.querySelectorAll('.otp-input').forEach((input, index, inputs) => {
    input.addEventListener('input', () => {
        if (input.value.length === 1) {
            // Move to the next input if there's a value and it's not the last input
            if (index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        }
    });

    input.addEventListener('keydown', (event) => {
        if (event.key === 'Backspace') {
            // Move to the previous input if backspace is pressed and the current input is empty
            if (input.value.length === 0 && index > 0) {
                inputs[index - 1].focus();
            }
        }
    });
});
