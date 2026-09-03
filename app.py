import streamlit as st

st.set_page_config(page_title="AI Productivity Assistant", page_icon="📅", layout="wide")

st.title("📅 AI Productivity Assistant")
st.write("Your smart daily planner")

# Sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Your Name", "Student")

st.sidebar.markdown("---")
st.sidebar.info("Week 17 Project - AI Productivity")

# Main
st.markdown(f"### Welcome {user_name}! 👋")

task = st.text_input("Add a new task:")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success(f"Added: {task}")

st.markdown("### Your Tasks Today")
if st.session_state.tasks:
    for i, t in enumerate(st.session_state.tasks, 1):
        st.checkbox(f"{i}. {t}", key=f"task_{i}")
else:
    st.info("No tasks yet - add one above!")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tasks", len(st.session_state.tasks))
with col2:
    st.metric("Productivity", "85%")
with col3:
    st.metric("Focus Time", "2h 30m")

st.markdown("### AI Suggestion")
st.write("💡 Tip: Complete your most difficult task first thing in the morning for best productivity!")

if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.rerun()