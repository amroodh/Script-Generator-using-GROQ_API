# Script Generator

This is a Streamlit application that generates scripts based on user-provided topics using the Groq API and few-shot prompting. The application also evaluates the generated scripts using various metrics such as F1 score, precision, recall, true positives, and false positives.

## Setup

### Prerequisites

- Python 3.7 or higher
- Groq API key

### Installation

1. Clone the repository or download the script.
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set your Groq API key as an environment variable:

    ```bash
    export GROQ_API_KEY="your_actual_api_key_here"
    ```

### Running the Application

1. Save your dataset as `dataset.csv` in the same directory as the script.
2. Run the Streamlit application:

    ```bash
    streamlit run script_generator.py
    ```

3. Open the provided URL in your browser to access the application.

### Using the Application

1. Enter a topic in the input field.
2. Click the "Generate Script" button.
3. View the generated script and evaluation metrics.

### Requirements

- `streamlit`
- `pandas`
- `scikit-learn`
- `groq`
- `fpdf`

### Example

To generate a script for the topic "content creation":

1. Enter "content creation" in the input field.
2. Click "Generate Script".
3. View the generated script and evaluation metrics.

## License

This project is licensed under the MIT License.
