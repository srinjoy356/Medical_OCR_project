OCR Project


Overview

This project is an Optical Character Recognition (OCR) application built with FastAPI backend and a plain HTML/CSS/JavaScript frontend. It allows users to upload PDF or JPEG files containing medical documents and extracts specific information based on document type (prescription or patient details).

Features

File Upload: Users can upload PDF or JPEG files.
Document Extraction: Automatic extraction of data from uploaded documents using OCR techniques.
Display and Edit Extracted Data: Display extracted data and allow users to edit incorrect details.
Document Visualization: Display the uploaded document for review.
Installation

To run the OCR project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/srinjoy356/OCR_project.git
cd OCR_project
Install dependencies:

Copy code
pip install -r requirements.txt
Start the FastAPI server:

css
Copy code
uvicorn main:app --reload
Access the application:
Open your web browser and go to http://localhost:8000/ to use the application.

Usage

Upload a Document:

Click on the "Choose File" button to select a PDF or JPEG file.
Select the type of document (prescription or patient details) from the dropdown.
Extract Information:

Click on the "Extract" button to initiate the extraction process.
The uploaded document will be displayed for review.
Edit Extracted Data:

Correct any inaccuracies in the extracted data displayed below the document.
Restart:

Use the "Restart" button to return to the main page for reuse.
Technologies Used

Backend: FastAPI, Python
Frontend: HTML, CSS, JavaScript
Libraries: pdf2image, pytesseract, OpenCV
Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/awesome-feature).
Make your changes.
Commit your changes (git commit -am 'Add awesome feature').
Push to the branch (git push origin feature/awesome-feature).
Create a new Pull Request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

Your Name: Srinjoy Roy


Email: srinjoy356@gmail.com


GitHub: srinjoy356
