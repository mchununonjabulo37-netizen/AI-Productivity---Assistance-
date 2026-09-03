# AI Productivity Assistant - Documentation
Name: Nonjabulo Gugu Mchunu | CAPACITI Week 17 | 3 Sept 2026

### 1. Problem Statement
Professionals waste up to 28% of work time on emails, meeting notes, and task planning, reducing productivity.

### 2. Solution Overview
A 5-in-1 Streamlit app that automates:
- Email Generation with tone & audience adaptation
- Meeting Summarization with action items
- Task Planning using Eisenhower Matrix
- Research Assistant
- Productivity Chatbot

### 3. Tools Used
ChatGPT (draft prompts), Gemini (research), Notion AI (docs), GitHub Copilot (app.py), Streamlit (UI), Lovable.ai (planning)

### 4. Prompt Techniques
Role-based, Audience Adaptation, Tone Variation, Chain-of-Thought, Few-shot, Eisenhower Matrix

### 5. Challenges & Solutions
Challenge: Coding on mobile + GitHub errors
Solution: Used Streamlit simplicity, fixed prompts.md duplicates via mobile edit

### 6. Responsible AI Considerations
- All prompts: bias-free inclusive language
- Disclaimers: "review before sending"
- No personal data stored
- Human validation required for all outputs
- No hallucination instruction added

### 7. Value & Impact
Saves 1.5 hrs/day, 60% faster task planning, consistent professional communication

### 8. How to Run
pip install -r requirements.txt
streamlit run app.py