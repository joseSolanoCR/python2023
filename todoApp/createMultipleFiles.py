contents = ["hola", "mundo", "dinamico"]
filenames = ["doc1.txt", "doc2.txt", "doc3.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"files/{filename}", "w" )
    file.write(content)