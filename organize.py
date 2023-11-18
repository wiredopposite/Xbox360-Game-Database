import os
import sys
import shutil
import json

json_file_path = 'xbox360_games.json'

def organize_directory(directory_path):
    with open(json_file_path, 'r') as json_file:
        games = json.load(json_file)

    title_id_to_folder_title = {game["Title ID"]: game["Folder Title"] for game in games}

    # depth of initial directory
    initial_depth = directory_path.rstrip(os.path.sep).count(os.path.sep)

    for root, folders, files in os.walk(directory_path):
        current_depth = root.rstrip(os.path.sep).count(os.path.sep)

        # Limit the depth
        if current_depth - initial_depth < 1:
            for folder in folders:
                for title_id, folder_title in title_id_to_folder_title.items():
                    if title_id in folder:
                        game_title_folder = os.path.join(root, folder_title)
                        game_folder = os.path.join(root, folder)
                        if os.path.exists(game_title_folder):
                            print(f"'{os.path.basename(game_title_folder)}' folder already exits, skipping folder '{os.path.basename(game_folder)}'")
                            break

                        os.makedirs(game_title_folder, exist_ok=True)

                        try:
                            shutil.move(game_folder, game_title_folder)
                        except:
                            print(f"Couldn't move '{game_folder}', skipping.")

                        break

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    organize_directory(directory_path)

if __name__ == "__main__":
    main()