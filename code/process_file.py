'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import packaging
import streamlit as st
import json

st.title("Process One Package 📦")
uploaded_file = st.file_uploader("Upload a file containing package information", type="txt")

if uploaded_file:
    file_content = uploaded_file.getvalue().decode("utf-8")
    json_filename = uploaded_file.name.replace(".txt", ".json")
    parsed_packages = []
    for package_line in file_content.splitlines():
        package_line = package_line.strip()
        parsed_pkg = packaging.parse_packaging(package_line)
        total_items = packaging.calc_total_units(parsed_pkg)
        base_unit = packaging.get_unit(parsed_pkg)
        parsed_packages.append(parsed_pkg)
        st.info(f"{package_line} ➡️ Total 📦 Size: {total_items} {base_unit}")
    with open(f"./data/{json_filename}", "w") as json_file:
        json.dump(parsed_packages, json_file, indent=4)

    st.success(f"{len(parsed_packages)} packages saved to {json_filename}", icon="💾")