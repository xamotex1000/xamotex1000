def read_config_file(filename):
    config = {}
    config_array = []
    multiline = False
    multiline_stop = False
    multiline_type = ""
    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            line.replace("\n", "")
            end_line = index
            if multiline == False and line.endswith("---"):
                multiline = True
                multiline_stop = False
                multiline_type = ""
                found_end = False
                line_index = index
                while found_end == False:
                    if file[line_index].endswith("---") == False:
                        found_end = True
                        end_line = line_index
                    else:
                        line_index+= 1
                if (multiline == False and line.startswith("V[")):
                    multiline_type = "LangList"
            elif line.endswith("---"):
                multiline_stop = True
            if multiline_stop == False and '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
            if (multiline_stop == False and line.startswith("V[")) or multiline_type == "LangList":
                element = []
                array = line.replace("V[", "").replace("---", "")
                print(array)
                for i in range(end_line-index-1):
                    array+=file[index+1+i].replace("---", ", ").replace("\n", "")
                    print(array)
                print(array)
                element = array.split(", ")
                config_array.append(element)
            if multiline and line.endswith("---") == False:
                multiline = False
                multiline_stop = False
                multiline_type = ""
    config["list"] = config_array
    return config
config = read_config_file('./config.conf')
class Stats:
    def __init__(self):
        self.username = config.get('username')
        self.theme = config.get('theme')
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
print(config["list"])
for i, item in enumerate(config["list"]):
    list_string+='\n|<img src="https://img.shields.io/badge/'+config["list"][i][0]+'%20-%20%230050b1?style=flat&logo='+config["list"][i][3]+'&logoColor='+config["list"][i][4]+'" height=32></img>|'+config["list"][i][1]+'/10, '+config["list"][i][2]+'|'
new_content = contents.replace("VARLIST", list_string).replace("VARSTATS", "https://github-readme-stats.vercel.app/api?username="+config["username"]+"&title_color="+config["title"]+"&text_color="+config["text"]+"&border_color="+config["border"]+"&bg_color="+config["background"])
change_file_contents(file_path, new_content)
