from flask import Flask, render_template, request, redirect, url_for
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Özetleme fonksiyonu
def summarize_text(text):
    # Cümlelere ayır
    sentences = sent_tokenize(text)
    
    # Stopwords (gereksiz kelimeler) listesini al
    stop_words = set(stopwords.words("english"))
    
    # Kelime frekanslarını hesapla
    word_frequencies = FreqDist(word.lower() for word in nltk.word_tokenize(text) if word.isalnum())
    
    # Cümlelerin puanını hesapla
    sentence_scores = {}
    for sentence in sentences:
        score = 0
        words_in_sentence = nltk.word_tokenize(sentence)
        for word in words_in_sentence:
            if word.lower() not in stop_words and word.isalnum():
                score += word_frequencies[word.lower()]
        sentence_scores[sentence] = score
    
    # En yüksek puanlı cümleleri seç
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:3])  # İlk 3 cümleyi al
    return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_text(text)
        return render_template('index.html', summary=summary)

    return render_template('index.html', summary=None)

# Yeni bir rota: Sıfırlamak için yönlendirme
@app.route('/clear')
def clear():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
