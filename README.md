# SummarizeTextModel

This project provides a text summarization model with a web API endpoint for summarizing text.

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**

   First, clone the repository from GitHub:
   ```shell 
   git clone https://github.com/mykytayevd/SummarizeTextModel.git
   cd SummarizeTextModel
   ```

2. **Create a Virtual Environment**

    Create a Python virtual environment (venv) for the project:
    ```shell
    python3 -m venv venv
    ```
    Activate the virtual environment:
    
    On Windows:
    ```shell
    venv\Scripts\activate
   ```

    On macOS/Linux:
    ```shell
    source venv/bin/activate
   ```

3. **Install Requirements**

    Install the required Python packages using pip:
    ```shell
   pip install -r requirements.txt
   ```

4. **Run the Application**

    Start the application by running main.py:
    ```shell
   python3 main.py
   ```

## Usage

To use the text summarization API endpoint, send a POST request to http://127.0.0.1:8000/summarize with the text to be summarized in the request body.

Example using curl:
```shell
curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d '{"text": "Your text to be summarized."}'
```