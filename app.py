import streamlit as st
from mpin_check import load_common_mpin_list, evaluate_mpin_strength

st.set_page_config(page_title="MPIN Strength Checker", layout="centered")

st.title("MPIN Strength Checker")
st.write("Check whether your MPIN is strong or weak based on common usage and demographics.")

#Load common MPINs dynamically
common_mpins = load_common_mpin_list()

#User Inputs
mpin = st.text_input("Enter your MPIN (4 or 6 digits)", max_chars=6)

col1, col2 = st.columns(2)
with col1:
    dob = st.text_input("Your Date of Birth (DD-MM-YYYY)")
    spouse_dob = st.text_input("Spouse's Date of Birth (DD-MM-YYYY)")
with col2:
    anniversary = st.text_input("Wedding Anniversary (DD-MM-YYYY)")

# Validate and Process
if st.button("Check MPIN Strength"):
    if not mpin.isdigit() or len(mpin) not in [4, 6]:
        st.error("MPIN must be 4 or 6 digits and numeric.")
    else:
        user_data = {}
        if dob: user_data["dob"] = dob
        if spouse_dob: user_data["spouse_dob"] = spouse_dob
        if anniversary: user_data["anniversary"] = anniversary

        result = evaluate_mpin_strength(mpin, user_data, common_mpins)

        if result["strength"] == "STRONG":
            st.success("Your MPIN is STRONG!")
        else:
            st.error("Your MPIN is WEAK.")

        st.markdown("### Reasons:")
        if not result["reasons"]:
            st.markdown("- No weaknesses found. Great choice!")
        else:
            for reason in result["reasons"]:
                st.markdown(f"- {reason}")
