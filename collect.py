"""
Collect some markdown files and concatenate them into a single file.
We'll first specify some path, and then we'll need to recursively read all the ".md" files in that path.
"""

import os

LEARN_PROMPTING_DOC = "Learn_Prompting/docs"

dirs_of_interests = [f"{LEARN_PROMPTING_DOC}/basics", f"{LEARN_PROMPTING_DOC}/basic_applications",
                        f"{LEARN_PROMPTING_DOC}/intermediate", f"{LEARN_PROMPTING_DOC}/applied_prompting",
                     f"{LEARN_PROMPTING_DOC}/advanced_applications", f"{LEARN_PROMPTING_DOC}/reliability",
                     ]

# now we'll recursively read all the ".md" files in that path
# we'll use the os.walk function to do this

def get_all_files_in_dir(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                all_files.append(os.path.join(root, file))
    return all_files

all_files = []
for dir in dirs_of_interests:
    all_files.extend(get_all_files_in_dir(dir))

# concatenate all the files into a single string
# but first sort the files content by "sidebar_position: (number)" in the first few lines
# then concatenate them into a single string
all_files_str_list = [] # we'll use it to store tuple (filename, number, file_content)
for file in all_files:
    with open(file, "r") as f:
        file_content = f.readlines()
        # get the number
        for line in file_content:
            if line.startswith("sidebar_position:"):
                number = int(line.split(":")[1].strip())
                break
        # the tuple is (filename, number, file_content)
        all_files_str_list.append((file, number, file_content))
        

# sort the list by number
all_files_str_list.sort(key=lambda x: x[1])
# concatenate them into a single string with join function and start with the filename
all_files_str = ""
for file in all_files_str_list:
    all_files_str += f"<!--- file:{file[0]} --->\n"
    all_files_str += "".join(file[2])


# save in a file call context_prompt.txt
with open("context_prompt.txt", "w") as f:
    f.write(all_files_str)