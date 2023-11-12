import os

def generate_sidebar():
    sidebar_content = ""
    for root, dirs, files in os.walk("."):
        # 忽略带下划线的目录
        if os.path.basename(root).startswith("_") or root == ".":
            continue
        md_files = [file for file in files if file.endswith(".md") and not file.startswith("_")]
        if md_files:
            relative_path = os.path.relpath(root, ".")
            indent_level = relative_path.count(os.sep)
            sidebar_content += "  " * indent_level + "- "
            sidebar_content += "**" + os.path.basename(root) + "**\n"
            for file in md_files:
                file_path = os.path.join(root, file)
                relative_file_path = os.path.relpath(file_path, ".")
                file_name = os.path.splitext(file)[0]
                sidebar_content += "  " * (indent_level + 1) + "- "
                sidebar_content += "[" + file_name + "]"
                sidebar_content += "(" + relative_file_path.replace("\\", "/") + ")\n"

    with open("_sidebar.md", "w", encoding="utf-8") as sidebar_file:
        sidebar_file.write(sidebar_content)

generate_sidebar()