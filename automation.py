def read_config_file(filename):
    config = {}
    config_array = []
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
            if line.startswith("V["):
                element = []
                prefix, array = line.split("[")
                element = array.split(", ")
                config_array.append([element[0], element[1], element[2].replace("\n", "")])
    config["list"] = config_array
    return config
config = read_config_file('./config.conf')
class Stats:
    def __init__(self):
        self.username = config.get('username')
        self.theme = config.get('theme')
#default, dark, radical, merko, grubby, tokyonight, onedark, cobalt, synthwave, highcontrast, dracula
        self.show_icons = config.get('show icons')
        self.hide_border = config.get('hide border')
        self.count_private = config.get('count private')

with open('README Template.md', 'r') as file:
    contents = file.read()

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
file_path = "./README.md"
list_string = "|<b>Language</b>|<b>Confidence</b>|\n|-|-|"
for i, item in enumerate(config["list"]):
    list_string+='\n|<img src="https://img.shields.io/badge/'+config["list"][i][0]+'%20-%20%230050b1?style=flat&logo='+config["list"][i][0]+' height=32></img>|'+config["list"][i][1]+'/10, '+config["list"][i][2]+'|'
new_content = contents.replace("VARLIST", list_string).replace("VARSTATS", "https://github-readme-stats.vercel.app/api?username="+config["username"]+"&title_color="+config["title"]+"&text_color="+config["text"]+"&border_color="+config["border"]+"&bg_color="+config["background"])
change_file_contents(file_path, new_content)
