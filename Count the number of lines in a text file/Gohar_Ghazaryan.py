def line_numbers_in_text_file(file_path):
    f = open(file_path)
    rows = f.readlines()
    return len(rows)
path = "C:\\Users\Admin\Desktop\\test.txt"
print(line_numbers_in_text_file(path))
    
