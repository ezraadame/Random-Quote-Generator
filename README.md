# Random-Quote-Generator
This is a basic random quote generator created using Flask and HTML. An API is retrieved from Zenquotes.io and is used to generate the random quotes.
---

Before running the application, ensure that you have the following installed:

- **Python** (version 3.6 or later)
- **pip** (Python package installer)

## How to Get Started

1. **Download the Project Files**:
   - Go to the [GitHub repository](https://github.com/your-username/random-quote-generator).
   - Click the "Code" button, then click "Download ZIP" to download the project files to your computer.
   - Extract the ZIP file to a folder on your machine.

2. **Navigate to the Project Folder**:
   - Open a terminal or command prompt and navigate to the folder where you extracted the project files.
     ```bash
     cd path/to/random-quote-generator
     ```

3. **Set up a Virtual Environment** (optional, but recommended):
   - You can create a virtual environment to isolate your dependencies:
     ```bash
     python -m venv venv
     ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Dependencies**:
   - Install the necessary packages by running:
     ```bash
     pip install Flask requests
     ```

## Running the Application

1. **Start the Flask app**:
   - In the project directory, run the following command to start the web server:
     ```bash
     python app.py
     ```

2. **Access the app**:
   - Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the application.

3. **Generate Quotes**:
   - Click the "Generate New Quote" button to fetch a new quote from the ZenQuotes API. You can keep clicking the button to get as many new quotes as you like.

## Troubleshooting

- **ModuleNotFoundError**: If you see a `ModuleNotFoundError`, it means that you need to install the required dependencies. Run `pip install Flask requests` or ensure you've activated the virtual environment.
- **API issues**: If the ZenQuotes API is down, the application may not be able to fetch quotes. In this case, try again later.



