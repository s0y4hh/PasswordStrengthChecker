import streamlit as st
import re  # For regular expressions

def check_password_strength(password):
    """
    Checks the strength of a password based on length, complexity, and character variety.

    Args:
        password (str): The password to check.

    Returns:
        None: Displays the strength and feedback using Streamlit.
    """
    score = 0
    feedback = ""

    if len(password) >= 16:
        score += 1
        feedback += "✅ Length is sufficient (16+ characters).  💪"
    else:
        feedback += "❌ Length is insufficient (minimum 16 characters).  📏"

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
        feedback += "✅ Contains both lowercase and uppercase letters.  🔤"
    else:
        feedback += "❌ Missing lowercase or uppercase letters.  🔡"

    if re.search(r"\d", password):
        score += 1
        feedback += "✅ Contains numbers.  🔢"
    else:
        feedback += "❌ Missing numbers.  🔢"

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback += "✅ Contains symbols.   symbols"
    else:
        feedback += "❌ Missing symbols.  ~!@#"

    if score == 4:
        st.success("Strong Password")
        st.write(feedback)
    elif score >= 2:
        st.warning("Medium Password")
        st.write(feedback)
    else:
        st.error("Weak Password")
        st.write(feedback)

    st.markdown("### Uniqueness")
    st.write("Use a unique password for each account. A password manager can help with this. 🔑")

def main():
    """
    Main function to run the Streamlit application.
    """
    # Custom styling (optional, but makes it look better)
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f4f8; /* Light background */
            color: #262730;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }
        .st-header {
            background-color: #4a148c; /* Dark purple header */
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        .st-title {
            color: #4a148c; /* Dark purple title */
        }
        .st-text {
            color: #262730;
        }
        .st-warning {
            color: #ed8936; /* Orange warning text */
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;

        }
        .st-error {
          color: #e53e3e;
          background-color: #f5f5f5;
          padding: 10px;
          border-radius: 5px;
        }
        .st-success{
            color: #38a169;
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='color:#4a148c;'>Password Strength Checker</h1>", unsafe_allow_html=True) #purple
    st.markdown("""
        ## Check Your Password Strength

        Enter your password below to see how strong it is.  A strong password is:

        -   At least 16 characters long 📏
        -   Contains a mix of uppercase and lowercase letters 🔤
        -   Includes numbers 🔢 and symbols~!@#
        -    Unique (not used for any other account) 🔑
        """)
    password = st.text_input("Enter your password:", type="password")
    if password:
        check_password_strength(password)

if __name__ == "__main__":
    main()
