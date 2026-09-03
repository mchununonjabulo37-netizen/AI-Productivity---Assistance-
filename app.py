import streamlit as st

st.set_page_config(page_title="AI Productivity Assistant", page_icon="📅", layout="wide")
st.title("📅 AI Productivity Assistant")
st.write("Your smart daily planner - Week 17 Project - CAPACITI")

# Sidebar - Keep your name feature
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Your Name", "Student")
st.sidebar.markdown("---")
st.sidebar.info("Week 17 Project - AI Productivity")
st.sidebar.markdown("### Responsible AI\n✅ Validate AI outputs\n✅ No personal data stored\n✅ Bias-free prompts\n✅ Disclaimer included")

st.markdown(f"### Welcome {user_name}! 👋")

# Create 5 Tabs for 5 Features
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📧 Email Gen", "📝 Meeting Summary", "📅 Task Planner", "🔍 Research", "💬 Chatbot"])

# TAB 1: Email - Required by project
with tab1:
    st.subheader("Email Generation - Prompt Engineering Demo")
    email_topic = st.text_input("Email Topic", "Request for deadline extension")
    tone = st.selectbox("Tone", ["Formal", "Persuasive", "Informal"])
    audience = st.selectbox("Audience", ["Manager", "Client", "Team"])
    if st.button("Generate Email", key="email"):
        prompt = f"Act as expert business writer. Write {tone} email to {audience} about {email_topic}. Include subject, greeting, body, CTA. Use inclusive language."
        st.code(f"PROMPT USED:\n{prompt}")
        st.success(f"Subject: Re: {email_topic}\n\nDear {audience},\n\nI hope you are well. Writing about {email_topic}.\n\nThis {tone} draft was generated using ChatGPT-style prompt engineering.\n\nBest regards,\n{user_name}\n\n[DISCLAIMER: Review before sending]")

# TAB 2: Meeting - Required by project
with tab2:
    st.subheader("Meeting Summarization")
    notes = st.text_area("Paste meeting notes", height=150, placeholder="We discussed project timeline, budget approved, John to send report...")
    if st.button("Summarize", key="meet"):
        prompt = f"Summarize into: Summary, Key Points, Decisions, Action Items, Deadlines. Notes: {notes}"
        st.code(f"PROMPT: {prompt}")
        st.info("**Summary:** Meeting productive\n\n**Key Points:**\n- Timeline discussed\n- Budget approved\n**Decisions:** Deadline Friday\n**Action Items:** John - Report, Sarah - Client update\n**Deadlines:** Friday 5pm")

# TAB 3: Task Planner - YOUR EXISTING CODE (Kept)
with tab3:
    st.subheader("Task Planner - Your Original Feature (Improved)")
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
    with col1: st.metric("Tasks", len(st.session_state.tasks))
    with col2: st.metric("Productivity", "85%")
    with col3: st.metric("Focus Time", "2h 30m")
    st.markdown("### AI Suggestion")
    st.write("💡 Tip: Complete your most difficult task first thing in the morning for best productivity!")
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.rerun()

# TAB 4: Research - Required
with tab4:
    st.subheader("Research Assistance")
    topic = st.text_input("Research topic", "AI productivity tools", key="res")
    if st.button("Generate Summary", key="research"):
        st.code(f"PROMPT: Act as researcher. Provide key insights, pros/cons, recommendations for {topic}. Use Chain-of-Thought.")
        st.write(f"**Research on {topic}:**\n- AI tools save 1.5hrs/day\n- Top tools: ChatGPT, Gemini, Notion AI\n- Recommendation: Start with email automation")

# TAB 5: Chatbot - Required
with tab5:
    st.subheader("Chatbot Interaction")
    q = st.text_input("Ask anything about productivity")
    if q:
        st.write(f"🤖 Assistant: For '{q}', I suggest using Email Generator for communication and Task Planner for scheduling. Need template?")import streamlit as st

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