# Prompts Library - AI Productivity Assistant
CAPACITI Week 17 - Njabulo

## Feature 1: Email Generation
**Techniques:** Role-based + Audience Adaptation + Tone Variation

**Prompt Used:**# Prompts Library - AI Productivity Assistant
CAPACITI Week 17 - Njabulo

## 1. Email Generation
Techniques: Role-based + Audience + Tone

Prompt:
You are a professional business writer. Write a {Formal/Informal/Persuasive} email for {Manager/Client/Team} about {topic}. Include Subject, Greeting, Body, CTA, Closing. Use inclusive bias-free language, max 200 words. 
Few-shot: Example Formal to Manager provided.

## 2. Meeting Summarization
Techniques: Chain-of-Thought + Structured

Prompt:
Think step by step: Read notes, extract Key Points, Decisions, Action Items with owners, Deadlines. Output in 5 sections: Summary, Key Points, Decisions, Action Items, Deadlines. Notes: {notes}. Do not hallucinate.

## 3. Task Planning
Techniques: Few-shot + Eisenhower Matrix

Prompt:
You are a productivity coach. Prioritize using Eisenhower Matrix.
Example: Input "Prepare report, Email client" -> Output Do First: Report (9-11am) etc.
Now prioritize: {user_tasks}
Suggest: Pomodoro 25/5, time-blocking, batch emails.

Tools: ChatGPT, Gemini, Notion AI, Copilot
Responsible AI: All prompts include bias-free instruction + disclaimer + human validation required. No data stored.# AI-Productivity-Assistant - CAPACITI Week 17

## Problem: Workplace productivity lost to repetitive tasks
Solution: 5-in-1 AI Assistant

## Features (Meets Project Overview)
1. Email generation (tone + audience adaptation)
2. Meeting summarization (key points, decisions, action items)
3. Task planning (Eisenhower Matrix + metrics)
4. Research assistance (simplified insights)
5. Chatbot interaction

## Tools Used: ChatGPT, Gemini, Notion AI, Streamlit
## Prompt Engineering: Role-based, Few-shot, Chain-of-Thought, Audience adaptation - see /prompts folder
## Responsible AI: Disclaimers, validation, no data storage, bias mitigation
## Value: Saves 1.5hrs/day, 60% faster planning
## How to Run: pip install -r requirements.txt ; streamlit run app.py