
from flask import Flask, render_template, request, redirect
from twilio.rest import Client

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']
    
    if username == 'verify' and password == '12345':
        account_sid = 'AC2e74009639a12cee4555cca57cbfd94e'
        auth_token = '9b7e8033633a80c3a8c1e54d6373f8a2'
        client = Client(account_sid, auth_token)
        
        service_sid = 'VA53e1ffee466d856539c56ed99a92fd95'
        verification = client.verify.services(service_sid).verifications.create(to=mobile_number, channel='sms')
        
        print(verification.status)
        
        return render_template('otp_verify.html')
    
    else:
        return render_template('user_error.html')

@app.route('/otp', methods=['POST'])
def get_otp():
    print("Processing")
    received_otp = request.form['received_otp']
    mobile_number = request.form['number']
    
    account_sid = 'AC2e74009639a12cee4555cca57cbfd94e'
    auth_token = '9b7e8033633a80c3a8c1e54d6373f8a2'
    client = Client(account_sid, auth_token)
    
    service_sid = 'VA53e1ffee466d856539c56ed99a92fd95'
    verification_check = client.verify.services(service_sid).verification_checks.create(to=mobile_number, code=received_otp)
    
    print(verification_check.status)
    
    if verification_check.status == "pending":
        return render_template('otp_error.html')
    else:
        return redirect("https://c-266.onrender.com/")  