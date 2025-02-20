'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import packaging
import streamlit as st
import json
import os

st.title("Process Multiple Packages 📦")
uploaded_files = st.file_uploader("Upload files containing package information", type="txt", accept_multiple_files=True)
total_files_processed = 0
total_lines_processed = 0
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_content = uploaded_file.getvalue().decode("utf-8")
        json_filename = uploaded_file.name.replace(".txt", ".json")
        parsed_packages = []
        lines_in_file = 0
        for package_line in file_content.splitlines():
            package_line = package_line.strip()
            if package_line:
                parsed_pkg = packaging.parse_packaging(package_line)
                total_items = packaging.calc_total_units(parsed_pkg)
                base_unit = packaging.get_unit(parsed_pkg)
                parsed_packages.append(parsed_pkg)
                lines_in_file += 1
        with open(f"./data/{json_filename}", "w") as json_file:
            json.dump(parsed_packages, json_file, indent=4)
        st.success(f"{len(parsed_packages)} packages saved to {json_filename}", icon="💾")
        total_files_processed += 1
        total_lines_processed += lines_in_file
    st.write(f"Total files processed: {total_files_processed}")
    st.write(f"Total lines processed: {total_lines_processed}")