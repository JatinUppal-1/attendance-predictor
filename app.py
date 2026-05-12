import streamlit as st
from utils.attendance import calculate_attendance 

st.set_page_config(page_title="CEC Attendance Predictor", page_icon="🎓")
st.title("🎓 Attendance Predictor")
st.markdown("Calculate your status for **CGC Landran** classes.")

col1, col2 = st.columns(2)

with col1:
    conducted = st.number_input("Classes Conducted", min_value=1, value=200)
    attended = st.number_input("Classes Attended", min_value=0, value=200)

with col2:
    planned_miss = st.number_input("Planned Misses", min_value=0, value=0)

if st.button("Check My Status", use_container_width=True):
    percentage = calculate_attendance(conducted, attended, planned_miss)
    percentage=int(percentage)
    
    st.divider()
    st.subheader(f"Predicted Attendance: {percentage}%")

    if percentage < 75:
        st.error(f"⚠️ **DETAINED**: You are {75 - percentage}% below the limit!")
    elif 75 <= percentage < 80:
        st.warning("⚡ **WARNING**: You are in the danger zone. Don't skip!")
    else:
        st.success("✅ **SAFE**: You are maintaining a good record.")