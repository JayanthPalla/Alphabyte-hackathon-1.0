import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)


def clean_text(resume_text):
    clean_text = remove_stopwords(resume_text)
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text


def extract_text_from_pdf(pdf_file_path):
    text = ""
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    text = clean_text(text)
    return text


def extract_text_from_text_file(text_file_path, encoding='utf-8'):
    with open(text_file_path, 'r', encoding=encoding) as file:
        text = file.read()
    text = clean_text(text)
    return text

