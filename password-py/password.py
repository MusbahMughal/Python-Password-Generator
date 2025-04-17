import streamlit as st
import re

# st.set_page_config(page_title="password Stragth Checker", page_icone="🔒")
# st.set_page_config(page_title="password Stragth Checker", page_icone="🔒")
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")


st.title("🔒 PAssword Stragth Checker")
st.markdown("""

## Welcome to the ultimate password stragth Checker!🙌
use this thiis simple tool to the check the password streagth and suggestion on how to make it stronger
            We will giive you helpful tiips to create a ** Stronger PAssword🔒**
""")

password = st.text_input("Enter Your Password", type="password")

feedback =[]

score = 0

if password:
    if len(password) >= 8:
        score += 1

    else: 
        feedback.append("password should at least  characters long")

if re.search(r'[A-Z]', password) and re.search(r'a-z', password):
   score += 1

else:
    feedback.append("❌password shpuld aontain both upper and lower case character")

    if re.search(r'\d', password):
        score += 1 

    else:
        feedback.append("password should conatain at least one digit" )

        if re.search(r'[@#$%&]', password ):
            score += 1

            else: 
feedback.append("❌ password should conatain at least one speciacl character (@#$%&) " )
if  score == 4:

                 feedback.append("✅ your password d stronger! 🎉" )
                 score == 3

                 feedback.append(" your password is medium stragth. t could be stronger! 💡" )
else:
 feedback.append(" your password is wea stragth. please mae t stronger! " )

            