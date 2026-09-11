// TempSwift — Temperature Converter
// Handles: input validation, unit selection, conversion to all units
// simultaneously, and absolute-zero edge case handling.

const ABS_ZERO = { C: -273.15, F: -459.67, K: 0 };

const inputEl = document.getElementById('temp-input');
const unitEl = document.getElementById('unit-select');
const errorEl = document.getElementById('input-error');
const convertBtn = document.getElementById('convert-btn');

const outEls = {
  C: document.getElementById('out-C'),
  F: document.getElementById('out-F'),
  K: document.getElementById('out-K'),
};
const rowEls = {
  C: document.getElementById('row-C'),
  F: document.getElementById('row-F'),
  K: document.getElementById('row-K'),
};

function toCelsius(value, unit) {
  if (unit === 'C') return value;
  if (unit === 'F') return (value - 32) * (5 / 9);
  if (unit === 'K') return value - 273.15;
  return NaN;
}

function fromCelsius(celsius, unit) {
  if (unit === 'C') return celsius;
  if (unit === 'F') return celsius * (9 / 5) + 32;
  if (unit === 'K') return celsius + 273.15;
  return NaN;
}

function clearError() {
  errorEl.textContent = '';
  inputEl.classList.remove('is-invalid');
}

function showError(message) {
  errorEl.textContent = message;
  inputEl.classList.add('is-invalid');
  Object.values(outEls).forEach((el) => {
    el.textContent = '—';
    el.classList.remove('is-error');
  });
  Object.values(rowEls).forEach((row) => {
    row.classList.remove('is-active', 'is-source');
  });
}

function isBelowAbsoluteZero(value, unit) {
  return value < ABS_ZERO[unit] - 1e-9;
}

function formatValue(value) {
  // Round to 2 decimal places, trim trailing zeros where possible
  const rounded = Math.round(value * 100) / 100;
  return rounded.toFixed(2);
}

function handleConvert() {
  clearError();
  const raw = inputEl.value.trim();
  const sourceUnit = unitEl.value;

  if (raw === '') {
    showError('Please enter a temperature value.');
    return;
  }

  // Reject non-numeric input (allow leading minus and decimal point)
  const numericPattern = /^-?\d+(\.\d+)?$/;
  if (!numericPattern.test(raw)) {
    showError('Please enter a valid number (digits only, e.g. -40 or 36.6).');
    return;
  }

  const value = parseFloat(raw);

  if (isBelowAbsoluteZero(value, sourceUnit)) {
    showError(
      `That's below absolute zero for ${sourceUnit === 'C' ? 'Celsius' : sourceUnit === 'F' ? 'Fahrenheit' : 'Kelvin'} ` +
      `(minimum possible: ${formatValue(ABS_ZERO[sourceUnit])} ${sourceUnit === 'K' ? 'K' : '°' + sourceUnit}). ` +
      `Nothing can be colder than absolute zero.`
    );
    return;
  }

  const celsius = toCelsius(value, sourceUnit);

  ['C', 'F', 'K'].forEach((unit) => {
    const converted = fromCelsius(celsius, unit);
    const unitLabel = unit === 'K' ? 'K' : `°${unit}`;
    outEls[unit].textContent = `${formatValue(converted)} ${unitLabel}`;
    outEls[unit].classList.remove('is-error');

    rowEls[unit].classList.remove('is-active', 'is-source');
    if (unit === sourceUnit) {
      rowEls[unit].classList.add('is-source');
    } else {
      rowEls[unit].classList.add('is-active');
    }
  });
}

convertBtn.addEventListener('click', handleConvert);

inputEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    handleConvert();
  }
});

inputEl.addEventListener('input', () => {
  if (errorEl.textContent) clearError();
});

unitEl.addEventListener('change', () => {
  if (inputEl.value.trim() !== '') {
    handleConvert();
  }
});
