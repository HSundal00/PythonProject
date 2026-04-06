contents = ["All carrets are to be slided.", 
            "The carrots are meant to be orange.", 
            "This is just another long line."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)