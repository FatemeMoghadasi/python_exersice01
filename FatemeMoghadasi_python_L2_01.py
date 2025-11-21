#input information
username = input("Enter your username").strip()
password = input("Enter password")

#they should be full
if username == "" or password == "":
    print("the username and password can not be empty")
else:
    score = 8
    reasons = []

#password length
    if len(password) > 8:
        reasons.append("✅ Password is longer than 8 characters")
    else:
        reasons.append("❌ Password is shorter than 8 characters")
        score -= 1

#atleast one English letter
        has_letter = False
        for ch in password:
            if ch.isalpha():
                has_letter = True
                break
        if has_letter:    
            reasons.append("✅ Password contains at least one English letter")
        else:
            reasons.append("❌ Password does not contain any English letters")
            score -= 1

#atleast on special character
        special_charc = ['!' , '@' , '$']
        has_special = False
        for ch in password:
            if ch in special_charc:
                has_special = True
                break
        if has_special:
            reasons.append("✅ Password contains at least one special character (!, @, $)")
        else:
            reasons.append("❌ Password does not contain any special characters")
            score -= 1

#atleast one capital word
        has_capital = False
        for ch in password:
            if ch.isupper():
                has_capital = True
                break
        if has_capital:
            reasons.append("✅ Password contains at least one uppercase English letter (A-Z)")
        else:
            reasons.append("❌ Password does not contain any uppercase letters")
            score -= 1

#password and username should be diffrent
        if username == password:
            reasons.append("❌ Password is identical to the username")
            score -= 1
        else:
            reasons.append("✅ Password is not identical to the username")

#should not be swapcase
        if username.lower() != password.lower():
            reasons.append("✅ Password is not the swapcase version of the username")
        else:
            reasons.append("❌ Password is the swapcase version of the username")
            score -= 1

#password should not have
        leet_dict = {'@':'a','!':'i','$':'s','0':'o'}
        normalized_password = ""
        for ch in password:
            if ch in leet_dict:
                normalized_password += leet_dict[ch]
            else:
                normalized_password += ch.lower()
        if normalized_password != username.lower():
            reasons.append("✅ Password is not a special-character version of the username")
        else:
            reasons.append("❌ Password is a special-character version of the username")
            score -= 1

#Password should not be a common password
        common_passwords = ["123456", "12345678", "12345", "111111", "123456789",
                        "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"]
        if password in common_passwords:
            reasons.append("❌ Password is one of the most common passwords")
        else:
            reasons.append("✅ Password is not one of the most common passwords")

        print(f"\n1. Username: {username}")
        print(f"2. Password: {password}\n")
        print("✅/❌ reasons:")
        count = 1
        for r in reasons:
            print(str(count) + ". " + r)
            count += 1

        if score <= 2:
            security_level = "Very Weak"
            tip = "Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols."
        elif score <= 4:
            security_level = "Weak"
            tip = "Your password could be stronger. Consider adding uppercase letters, numbers, or symbols."
        elif score <= 6:
            security_level = "Moderate"
            tip = "Your password is okay, but it can be improved with more complexity."
        elif score == 7:
            security_level = "Strong"
            tip = "Your password is strong, but adding more symbols or numbers could make it very strong."
        else:
            security_level = "Very Strong"
            tip = "Excellent password! Keep it secure."

        print(f"\nFinal score: {score} out of 8")
        print(f"Security Level: {security_level}")
        print(f"Tip: {tip}")
