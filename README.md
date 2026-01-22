# 🎓 Lecture-Saver 3000

Lecture-Saver 3000 is a modular Retrieval-Augmented Generation (RAG) system designed to help students chat with their course materials. It uses Google's Gemini-1.5-Flash for both embeddings and text generation.

## 🚀 Features
- **Modular Architecture**: Separate modules for ingestion, embedding, retrieval, and generation.
- **Gemini Integration**: Powered by Google's Gemini-1.5-Flash (Free via Google AI Studio).
- **Evidence-Based Answers**: Provides citations (filename and page number) for every answer.
- **Interactive UI**: Includes a Streamlit application for easy document upload and chatting.
- **Jupyter Notebook**: A step-by-step demonstration of the RAG pipeline.

## 🛠️ Setup

1.  **Clone the repository** (or extract the files).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set your API Key**:
    Obtain a Google AI Studio API key and set it as an environment variable:
    ```bash
    export GOOGLE_API_KEY="your_api_key_here"
    ```

## 📖 Usage

### 1. Ingestion Pipeline
Place your PDF lectures in the `data/` directory and run:
```bash
python populate_database.py
```
To reset the database:
```bash
python populate_database.py --reset
```

### 2. Query via CLI
```bash
python query_data.py "What is Gradient Descent?"
```

### 3. Streamlit App (Bonus)
```bash
streamlit run app.py
```

### 4. Jupyter Notebook
Open `lecture_saver_3000.ipynb` to see the step-by-step implementation.

## 📂 Project Structure
- `get_embedding_function.py`: Returns the Gemini embedding function.
- `populate_database.py`: Processes PDFs and populates ChromaDB.
- `query_data.py`: Handles retrieval and generation.
- `app.py`: Streamlit interface.
- `lecture_saver_3000.ipynb`: Jupyter notebook for demonstration.
- `requirements.txt`: List of required Python libraries.
