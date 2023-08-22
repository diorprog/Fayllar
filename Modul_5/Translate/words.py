uzbek_english_dict = {
    'arrive': 'Yetib kelmoq',
    'article': 'Maqola',
    'cancel': 'Bekor qilmoq',
    'competition': 'Musobaqa',
    'explain': 'Tushuntirmoq',
    'happen': "Ro'y bermoq, yuz bermoq",
    'how often': 'Qanchalik tez-tez',
    'invite': '(Mehmonga) taklif qilmoq',
    'last': 'Davom etmoq',
    'mean': "Ma'no bildirmoq, nazarda tutmoq",
    'meeting': '1. Majlis.  2. Uchrashuv',
    'mobile phone': 'Uyali telefon',
    'sell': 'Sotmoq',
    'silver': 'Kumush',
    'spare': "Bo'sh",
    'spend on': "(pul) sarflamoq, (vaqt) o'tkazmoq",
    'steal': "O'g'irlamoq",
    'take part': "Ishtirok etmoq",
    'train': "Poyezd",
    'translate': "Tarjima qilmoq",
    'uncle': "Tog'a, amaki",
    'word': "So'z",
    'yet': "Allaqachon (so'roq gapda), haliyam yo'q (inkor gapda)",
    'actor': "Aktyor",
    'angry': "Ranjimoq, jahli chiqmoq",
    'apply for': "(Ish so'rab, o'qishga qabul qilishni so'rab) ariza bermoq",
    'appoint': "(lavozimga) tayinlamoq"
}

# Enter the word to translate
word_to_translate = input("Enter a word to translate: ")

if word_to_translate in uzbek_english_dict:
    translated_word = uzbek_english_dict[word_to_translate]
    print(f"English: {word_to_translate}\nUzbek: {translated_word}")
else:
    print("Word not found in the dictionary.")
