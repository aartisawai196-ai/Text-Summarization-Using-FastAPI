# Text Summarization Using FastAPI

A text summarization project that uses a Transformer-based Hugging Face model to generate concise summaries from longer text. The trained/saved model is integrated with a FastAPI backend to provide a simple API for text summarization.

## 🚀 Features

* Text summarization using a Transformer model
* Hugging Face Transformers integration
* FastAPI REST API
* Interactive API documentation using Swagger UI
* Locally saved model support
* Easy to run and test

## 🛠️ Technologies Used

* Python
* FastAPI
* Hugging Face Transformers
* PyTorch
* Uvicorn
* HTML/JSON API
* Transformer-based NLP model

## 📁 Project Structure

```text
Text-Summarization-Using-FastAPI/
│
├── app.py
├── requirements.txt
├── README.md
│
└── saved_summary_model/
    └── saved_summary_model/
        ├── config.json
        ├── tokenizer files
        └── model files
```

> Note: The large `model.safetensors` file is not included in this GitHub repository because GitHub has a 100 MB file-size limit.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aartisawai196-ai/Text-Summarization-Using-FastAPI.git
```

### 2. Open the project folder

```bash
cd Text-Summarization-Using-FastAPI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to enter text and test the summarization API.

## 🔄 How It Works

```text
User Input
    ↓
FastAPI API
    ↓
Tokenizer
    ↓
Transformer Model
    ↓
Generated Summary
    ↓
API Response
```

The input text is tokenized and passed to the Transformer model. The model generates a shorter summary, which is returned through the FastAPI endpoint.

## 🎯 Use Cases

This project can be useful for:

* Summarizing articles
* Summarizing long documents
* NLP applications
* News summarization
* Building AI-powered text processing APIs

## 🔮 Future Improvements

* Deploy the API online
* Host the model on Hugging Face
* Add a simple frontend interface
* Improve summarization quality
* Add support for larger texts
* Add input validation and error handling

## 👩‍💻 Author

**Aarti Sawai**

GitHub:
https://github.com/aartisawai196-ai
