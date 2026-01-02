#Amazon logo
driver.find_element(By.CLASS_NAME, "a-icon a-icon-logo")
#Email field
driver.find_element(By.ID, "ap_email_login")
#Continue button
driver.find_element(By.ID, "continue")
#Conditions of use link
driver.find_element(By.XPATH,"//a[contains(@href,'signin_notification_condition_of_use')]")
#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")
#Need help link
driver.find_element(By.ID, "ap-other-signin-issues-link")
#Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
#Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")
#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

#