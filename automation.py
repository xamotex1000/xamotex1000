class Stats
    def __init__(self):
        self.username = "xamotex1000"
        self.theme = "cobalt"
        self.show_icons = "true"
        self.hide_border = "false"
        self.count_private = "true"

def change_file_contents(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("File contents changed successfully.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "./GHRMStats.html"
new_content = f'''
<html>
<head>
    <meta http-equiv="refresh" url="https://github-readme-stats.vercel.app/api?username={Stats.username}&theme={Stats.theme}&show_icons={Stats.show_icons}&hide_border={Stats.hide_border}&count_private={Stats.count_private}">
</head>
</html>
'''
change_file_contents(file_path, new_content)