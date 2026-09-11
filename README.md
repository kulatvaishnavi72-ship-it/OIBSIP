# TempSwift — Temperature Converter Website

**Track:** Web Development & Designing — Level 1, Task 3
**Program:** Oasis Infobyte SIP

## Objective
An interactive web tool that converts a temperature value between Celsius, Fahrenheit, and Kelvin in real time, with input validation and correct handling of physically impossible (below absolute zero) values.

## Tech Stack
- HTML5
- CSS3
- JavaScript (Vanilla — no frameworks or libraries)

## Features
- Numeric input field with strict validation — non-numeric input is rejected with an inline error message
- Dropdown to select the **source unit** (Celsius / Fahrenheit / Kelvin)
- All three converted values are displayed **simultaneously** on every conversion
- "Convert" button triggers the calculation (Enter key also works)
- Absolute-zero guard: values below −273.15 °C / −459.67 °F / 0 K are rejected with a clear explanatory message instead of producing a nonsensical result
- Clean, centred, responsive UI with clear labels and visual feedback (the source unit is outlined, converted units are highlighted)

## Files
```
index.html   — page structure
style.css    — styling (gradient card UI, responsive layout)
script.js    — conversion logic, validation, DOM updates
```

## How to Run
Open `index.html` directly in any modern browser — no build step, server, or dependencies required.

## How It Works
1. Enter a numeric value in the input field.
2. Choose which unit that value is in (From unit).
3. Click **Convert** (or press Enter).
4. All three units update at once; the unit you entered is outlined, the two converted units are highlighted.

## Testing Performed
The conversion logic was verified programmatically against known reference points before submission:

| Input | Expected Output | Result |
|---|---|---|
| 0 °C | 32 °F, 273.15 K | ✅ |
| 100 °C | 212 °F, 373.15 K | ✅ |
| 98.6 °F | 37.00 °C, 310.15 K | ✅ |
| −40 °C | −40 °F, 233.15 K | ✅ |
| 0 K | −273.15 °C, −459.67 °F | ✅ |
| "abc" (non-numeric) | Rejected with error | ✅ |
| −300 °C (below absolute zero) | Rejected with error | ✅ |
| Empty input | Rejected with error | ✅ |

## Author
_Add your name here before submitting._
