# Example config.conf file:
# username = my_username
# password = my_password
# server = my_server

def read_config_file(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
    return config

def main():
    config_filename = 'config.conf'
    config = read_config_file(config_filename)
    
    # Assign variables based on config values
    username = config.get('username')
    password = config.get('password')
    server = config.get('server')
    
    # Use the variables
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Server: {server}")

if __name__ == "__main__":
    main()







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
change_file_contents(file_path, new_content)
def test_change_file_contents():
    x = 0