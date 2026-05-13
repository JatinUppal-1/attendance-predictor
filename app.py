import streamlit as st
import math
from utils.attendance import calculate_attendance, classes_needed_to_reach_target

st.set_page_config(page_title="CEC Attendance Predictor", page_icon="🎓")
st.title("🎓 Attendance Predictor")
st.markdown("Calculate your status for **CGC Landran** classes.")

col1, col2 = st.columns(2)

with col1:
    conducted = st.number_input("Classes Conducted", min_value=1, value=40)
    attended = st.number_input("Classes Attended", min_value=0, value=30)

with col2:
    planned_miss = st.number_input("Planned Misses", min_value=0, value=0)

percentage = int(calculate_attendance(conducted, attended, planned_miss))

st.divider()
st.subheader(f"Current Attendance: {percentage}%")


if 75 <= percentage < 80:
    st.warning("⚡ **WARNING**: You are in the danger zone. Don't skip!")
else:
    st.success("✅ **SAFE**: You are maintaining a good record.")

if True:
    target = st.slider("What is your goal percentage?", percentage, 100, percentage)
    
    needed = classes_needed_to_reach_target(target, conducted, attended, planned_miss)
    
    st.info(f"👉 To reach **{target}%**, you must attend the next **{needed}** classes without missing any.")