'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import packaging
import streamlit as st
st.title("Process One Package 📦")
package_input = st.text_input("Enter package information:")

if package_input:
    package = packaging.parse_packaging(package_input)
    unit_name = None
    for item in package:
        for key, value in item.items():
            if unit_name is None:
                unit_name = key.capitalize()
            st.write(f"{key.capitalize()} ➡️ {value}")
    total_units = packaging.calc_total_units(package)
    st.write(f"Total Size: {total_units} {unit_name} 📦")