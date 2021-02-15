import docx
path = "123.docx"
file = docx.Document(path)
for p in file.paragraphs:
    print(p.text)
    list1 = p.text.split(' ')



