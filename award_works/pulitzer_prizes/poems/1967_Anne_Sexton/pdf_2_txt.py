import fitz

doc = fitz.open('anne_sexton_poems.pdf')

for page in doc:
    open('anne_sexton_poems.txt', 'a', encoding='utf-8').write(page.get_text() + '\n' + '*' * 50 + '\n')
