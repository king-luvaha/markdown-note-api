# 📝 FastAPI Markdown Note-Taking App with Grammar Correction

A developer-friendly REST API that accepts `.md` file uploads, corrects grammar using LanguageTool, and returns both the cleaned Markdown and its HTML version. Built with FastAPI, this app is ideal for developers who want to explore grammar correction, file parsing, and API integration using Python.

---

## 🌟 Key Features

- ✅ Upload and parse Markdown files via API
- ✍️ Grammar correction powered by LanguageTool
- 🔄 Returns corrected Markdown and rendered HTML
- ⚡ Built with FastAPI – high-performance, async-ready
- 🧪 Tested using Postman
- 🧱 Modular and extendable codebase

---

## 📂 Project Structure

```
markdown-note-api/
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
├── uploads/                 # for uploaded markdown files
├── requirements.txt
└── README.md
````

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/markdown-note-api.git
cd markdown-note-api
````

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> ✅ **Note:** If you don’t have a `requirements.txt` yet, create one:

```txt
fastapi
uvicorn
sqlalchemy
pydantic
markdown
language-tool-python
aiofiles
python-multipart
```

4. **Run the server**

```bash
uvicorn main:app --reload
```

- App runs at: `http://127.0.0.1:8000`
- Interactive docs: `http://127.0.0.1:8000/docs`

---

## 📬 API Endpoint: Upload Markdown File

### ➕ `POST /upload`

Upload a `.md` file to receive:
- Original Markdown
- Corrected Markdown
- Rendered HTML

### 🔧 Request (Postman Example)

**POST** `http://127.0.0.1:8000/upload`  
**Body** → `form-data`

- Key: `file`
- Type: `File`
- Value: _(Upload your `.md` file)_

### ✅ Sample Response

```json
{
  "id": 1,
  "title": "My First Note",
  "content": "# My Note\nThis is a markdown note.",
  "html_content": "<h1>My Note</h1><p>This is a markdown note.</p>",
  "grammar_issues": "SOME_GRAMMAR_CHECK_OUTPUT"
}
```

> You can import the sample Postman collection provided in the repo under `postman/markdown-note-api.postman_collection.json`.

---

## 🧪 Testing Tips

- Use the `test_files/` folder to quickly try file uploads.
- Postman is ideal for form-data file testing.
- The `language-tool-python` library requires an internet connection (uses LanguageTool's public API).

---

## 🛠 Tech Stack

| Tech                                | Role                                                   |
| ----------------------------------- | ------------------------------------------------------ |
| **FastAPI**                         | A modern, fast (high-performance) Python web framework |
| **Uvicorn**                         | To run the server                                      |
| **SQLAlchemy**                      | For database handling                                  |
| **SQLite**                          | The database                                           |
| **Markdown parsing**                | To convert Markdown to HTML                            |
| **Grammar checking**                | Using LanguageTool for grammar and spell checking      |
| **aiofiles** + **python-multipart** | For file upload support                                |
| **Postman**                         | For API testing                                        |

---

## 📌 Notes

* Make sure you're connected to the internet to use LanguageTool (it uses an external API by default).
* All testing is done using Postman.
* The app currently does not persist notes to a database. You can add this as a future improvement.

---

## 💡 Ideas for Extension

- 🗃️ Save corrected notes to a database (SQLite, PostgreSQL)
- 🔐 Add JWT-based authentication
- 🌐 Create a frontend (React/Vue/Svelte) to upload and display notes
- 📤 Email or download corrected notes
- 🧠 Real-time Markdown editor with inline grammar suggestions
- 🚦Add a custom `.env` for toggling offline/online grammar mode

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---


