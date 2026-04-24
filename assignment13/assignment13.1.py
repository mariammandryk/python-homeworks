import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<.*?>', '', html)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(clean_text)


delete_html_tags('draft.html')
print("OK")