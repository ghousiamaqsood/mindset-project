import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")

st.title("🌱 Growth Mindset Challenge Web App with Streamlit")
st.header("Welcome to the Growth Journey!")

st.write("💡 'Failure is an opportunity to grow.' - Carol Dweck")
st.write("💡 'Challenges make you stronger.'")

st.write("Continuous Learning")
st.write("Hard Work and Effort")
st.write("Accepting Challenges")

# Quote section
st.header("Today's Growth Mindset Quote")
st.write("💡 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe your challenge")

# Condition
if user_input:
    st.success(f"💪 You're facing: {user_input} Keep pushing forward towards your goal! ✈️")
else:
    st.write("You are doing great! Keep it up! 🚀")

# Reflecting
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success("🚀 Great! Keep reflecting and learning!")
else:
    st.warning("📝 Don't forget to reflect on your learning. Please share any hurdles!")

# Achievements
st.header("Share Your Achievements!")
achievements = st.text_input("What did you achieve today?")  # ✅ یہاں اسپیس کا مسئلہ حل ہوگیا!

if achievements:
    st.success(f"🌟 Amazing! You achieved: {achievements} Keep it up!")
else:
    st.warning("🚀 Don't forget to celebrate your valuable achievements!")

# Footer
st.write("---")
st.write("Always remember to keep a growth mindset!")
st.write("🌟 This web app is created by [Ghousia Maqsood] with ❤️ using Streamlit")
