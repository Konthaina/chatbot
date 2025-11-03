# AngkorScience ឆាតបូត

<p align="center">
  <img src="assets/icon.svg" alt="AngkorScience Chatbot" width="120" />
</p>

ឆាតប៊ូតសាមញ្ញមួយ ដែលប្រើចំណុចចាប់ផ្តើម Gradio និង Google's Generative AI (Gemini) ដើម្បីឆ្លើយសំណួរអំពី AngkorScience។

សារសំខាន់ៈ ការបកប្រែខ្មែរនេះបង្កើតដោយម៉ាស៊ីន — សូមពិនិត្យ និងកែតម្រូវឲ្យបានត្រឹមត្រូវមុនប្រើប្រាស់សាធារណៈ។

## លក្ខណៈពិសេស

- UI វេទិកា Gradio ងាយស្រួលប្រើ (ស្តាយឆាត)
- ប្រើម៉ូឌែល `google-generativeai` / Gemini សម្រាប់ការឆ្លើយ
- ដាក់លេខសម្ងាត់ និងការកំណត់ពី `.env`

## ចាប់ផ្ដើមយល់ដឹង (Quickstart)

1. គម្លាតរបៀប (clone) ឬចម្លងឯកសារ និងបើកថតគម្រោង
2. បង្កើត virtual environment និងតំឡើងអាសយដ្ធាន:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. បង្កើត `.env` នៅក្នុងថតគម្រោង និងបំពេញកូនសោ API:

```env
GEMINI_API=your_gemini_api_key_here
GEMINI_MODEL=your_model_name_here
```

4. រត់កម្មវិធី៖

```bash
python index.py
```

Gradio នឹងបង្ហាញ URL ក្នុង terminal — បើក URL នោះក្នុងកម្មវិធីរុករករបស់អ្នក ដើម្បីចាប់ផ្ដើមសន្ទនា។

## កំណត់បរិមាណ

- `GEMINI_API` — កូនសោ API របស់ Gemini (មិនគួរបង្ហោះសាធារណៈ)
- `GEMINI_MODEL` — ឈ្មោះម៉ូឌែលដែលប្រើ (ឧ. `gemini-pro`)

## កំណត់សម្រាប់អភិវឌ្ឍន៍

- មុខងារ chat គឺ `chat(message, history)` នៅក្នុង `index.py`។ វាផ្តល់សារ ទាញផ្ទុកទៅក្នុង `conversation_history` ហើយហៅម៉ូឌែល Gemini ដើម្បីបង្កើតចម្លើយ។
- បច្ចុប្បន្នប្រើ `conversation_history` ក្នុងផ្លូវចងចាំក្នុង RAM។ សម្រាប់ផលិតកម្ម សូមគិតពីការផ្ទុក Persistent, rate-limiting និង authentication។
- យុទ្ធសាស្រ្តដែលអាចធ្វើបាន:
  - បន្ថែមការសម្រាប់តម្លឹងសារ ដើម្បីជៀសវាង injection
  - រក្សាស្ថានភាព per-session ជាជាងបញ្ជីមួយគត់
  - បន្ថែម unit tests និង CI

## ដោះស្រាយបញ្ហា

- បើមានកំហុស authentication, សូមពិនិត្យ `GEMINI_API` ថាត្រឹមត្រូវ
- ប្រសិនបើ Gradio មិនបើកអេក្រង់, ពិនិត្យ URL ដែលបានបង្ហាញ និង firewall
- ប្រសិនបើមានបញ្ហា dependencies, សាកល្បងបង្កើត virtualenv ម្តងទៀត និង `pip install -r requirements.txt`

## សុវត្ថិភាព

- សូមកុំ commit `.env` ឬសោ API ទៅក្នុងប្រភពកូដសាធារណៈ
- គ្រប់គ្រង និងប្ដូរកូនសោប្រសិនមានការបង្ហោះ

## អាជ្ញាប័ណ្ណ

គម្រោងនេះផ្តល់ជូនក្នុងស្ថានភាព "as-is"។ បន្ថែមឯកសារ `LICENSE` (ឧ. MIT) ប្រសិនបើចង់ចែករំលែកទូទៅ។

## ទាក់ទង

ប្រសិនបើអ្នកចង់បានជំនួយក្នុងការពង្រឹងគម្រោង (tests, deployment, session handling), សូមប្រាប់ខ្ញុំ និងខ្ញុំអាចអនុវត្តបន្ថែម។

