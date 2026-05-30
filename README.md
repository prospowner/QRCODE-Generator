# Python QR Code Generator

A lightweight, terminal-driven matrix generation utility written in Python that allows users to encode raw text strings or web URLs into scannable, high-quality `.png` QR code assets.

## Features
* **Granular Matrix Customization:** Exposes configurations for the QR matrix grid, including versioning sizes, padding borders, pixel box dimensions, and medium-tier error correction thresholds (`ERROR_CORRECT_M`).
* **Automated Filename Sanitization:** Includes smart conditional guardrails to auto-assign default names if left blank and checks for string extensions, appending `.png` dynamically if omitted.
* **Error-Resilient Operations:** Wraps core compilation data streams and rendering pipelines within safe `try/except` execution blocks to intercept runtime compilation errors gracefully.

## Dependencies
This utility requires the open-source `qrcode` library and `Pillow` to compile image matrix data. 
You can install them together using pip:
```bash
pip install qrcode pillow
