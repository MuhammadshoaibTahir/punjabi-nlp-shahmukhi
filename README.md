# Punjabi NLP Toolkit 🇵🇰

A Python library for **Punjabi (Shahmukhi + Roman) Natural Language Processing**.

This toolkit is designed to handle **real-world Punjabi text**, including:

* Mixed script input (Roman + Shahmukhi)
* Noisy social media text
* Linguistic normalization

---

## 🚀 Features

* ✅ Unicode & character normalization
* 🔄 Roman Punjabi → Shahmukhi conversion
* ✂️ Sentence & word tokenization
* 🚫 Stopword removal
* 📊 Frequency analysis
* 🔗 N-gram extraction (bigrams, trigrams)
* 🔍 Script detection (Shahmukhi / Gurmukhi / Roman)

---

## 📦 Installation

```bash
pip install punjabi-nlp
```

---

## ⚡ Quick Start

```python
from punjabi_nlp import PunjabiPipeline

pipeline = PunjabiPipeline()

text = "mnu lagda ae tussi theek o"

output = pipeline.process(text)

print(output)
```

---

## 🧪 Example Output

```python
{
  'script': 'shahmukhi',
  'normalized_text': 'مینوں لگدا اے تسی ٹھیک او',
  'sentences': ['مینوں لگدا اے تسی ٹھیک او'],
  'tokens': ['مینوں', 'لگدا', 'اے', 'تسی', 'ٹھیک', 'او'],
  'token_count': 6,
  'frequency': {
    'مینوں': 1,
    'لگدا': 1,
    'اے': 1,
    'تسی': 1,
    'ٹھیک': 1,
    'او': 1
  }
}
```

---

## 🔥 Mixed Script Example (Real-World Input)

```python
text = "کِتّھے ایں؟ mnu lagda ae tussi theek o"
```

### Output:

```text
کتھے ایں? مینوں لگدا اے تسی ٹھیک او
```

👉 This demonstrates:

* Shahmukhi normalization
* Roman conversion
* Clean tokenization

---

## 🧠 Why This Library?

Punjabi is a **low-resource language in NLP**, especially in Shahmukhi script.

This toolkit aims to:

* Provide a **standard preprocessing pipeline**
* Support **linguistic research**
* Enable **corpus-based studies**
* Handle **code-mixed Punjabi text**

---

## 📊 Corpus Analysis

The library supports:

* Word frequency
* Bigrams & trigrams
* Lexical pattern extraction

---

## 🏗️ Project Structure

```text
punjabi_nlp/
├── normalization.py
├── tokenization.py
├── roman.py
├── stopwords.py
├── utils.py
├── corpus.py
└── pipeline.py
```

---

## 🧩 Example Use Cases

* 📚 Corpus linguistics research
* 🧠 NLP model preprocessing
* 💬 Social media text cleaning
* 🗣️ Punjabi language tools
* 🎓 Teaching computational linguistics

---

## ⚠️ Limitations

* Rule-based Roman conversion (not fully phonetic yet)
* Limited stopword list
* No POS tagging (planned)

---

## 🚀 Future Work

* 🔁 Shahmukhi ↔ Gurmukhi transliteration
* 🧠 Smart phonetic Roman conversion
* 🏷️ POS tagging
* 📈 Named Entity Recognition (NER)
* 🖥️ GUI tool for live processing

---

## 🤝 Contributing

Contributions are welcome!

You can help by:

* Improving normalization rules
* Expanding Roman mappings
* Adding datasets
* Reporting issues

---

## 📜 License

MIT License

---

## 👤 Author

**Shoaib Tahir**
Computational Linguistics | Punjabi NLP

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 📢 Share with others
* 🧠 Use in research

---
