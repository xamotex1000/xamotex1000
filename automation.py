def read_config_file(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
            config_array = []
            if line.startswith("V["):
                element = []
                prefix, array = line.split("[")
                element = array.split(", ")
                config_array.append(element)
                print(config_array)
                
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
    print(contents)

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
new_content = contents.replace("", "")
change_file_contents(file_path, new_content)