import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Power Calculator", layout="centered")

st.title("🔢 Advanced Power Calculator")
st.write("Enter one or more integers to compute their powers (square, cube, fifth power).")

# Input method
mode = st.radio("Select input mode:", ["Single Number", "Multiple Numbers"])

if mode == "Single Number":
    nums = [st.number_input("Enter an integer", value=1, step=1)]
else:
    input_str = st.text_input("Enter comma-separated integers (e.g. 2, 4, 5)", value="2, 3")
    try:
        nums = [int(x.strip()) for x in input_str.split(",")]
    except ValueError:
        st.error("Please enter only integers separated by commas.")
        st.stop()

# Operation selection
st.markdown("### Choose operations to perform:")
compute_square = st.checkbox("Square", value=True)
compute_cube = st.checkbox("Cube", value=True)
compute_fifth = st.checkbox("Fifth Power", value=True)

# Compute results
results = []
for n in nums:
    result = {"Number": n}
    if compute_square:
        result["Square"] = n ** 2
    if compute_cube:
        result["Cube"] = n ** 3
    if compute_fifth:
        result["Fifth Power"] = n ** 5
    results.append(result)

# Display results
df = pd.DataFrame(results)
st.dataframe(df)

# Plot if multiple values
if len(nums) > 1:
    st.markdown("### 📊 Comparison Chart")
    chart_type = st.selectbox("Select chart type:", ["Bar Chart", "Line Chart"])
    
    if chart_type == "Bar Chart":
        st.bar_chart(df.set_index("Number"))
    else:
        st.line_chart(df.set_index("Number"))

# Download option
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download results as CSV",
    data=csv,
    file_name="power_results.csv",
    mime="text/csv",
)
