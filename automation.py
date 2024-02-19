class Stats:
    def __init__(self):
        self.username = "xamotex1000"
        self.theme = "cobalt" 
#default, dark, radical, merko, grubbox, tokyonight, onedark, cobalt, synthwave, highcontrast, dracula
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

stats = Stats()
file_path = "./GHRMStats.html"
new_content = f'''
<html>
<head>
    <meta http-equiv="refresh" content="0; url=https://github-readme-stats.vercel.app/api?username={stats.username}&theme={stats.theme}&show_icons={stats.show_icons}&hide_border={stats.hide_border}&count_private={stats.count_private}">
</head>
</html>
'''
def test_change_file_contents():
    change_file_contents(file_path, new_content)