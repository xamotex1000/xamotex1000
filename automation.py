def change_file_contents(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("File contents changed successfully.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = '''
<html>
<head>
    <meta http-equiv="refresh" url=">
</head>
</html>
'''
change_file_contents(file_path, new_content)