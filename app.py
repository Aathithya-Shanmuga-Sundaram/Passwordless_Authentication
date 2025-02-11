from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dictionary to store registered users (In a real application, use a database)
users = {}

# This function helps to get the IP address of the client
def get_ip():
    return request.remote_addr

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the username and email from the form
        username = request.form['username']
        email = request.form['email']

        # Fetch user agent, IP, timezone, and resolution from background
        user_agent = request.headers.get('User-Agent')  # Get user agent
        ip_address = get_ip()  # Get IP address
        timezone = request.form['timezone']  # This will be set via JS
        screen_resolution = request.form['screen_resolution']  # Set via JS

        # Print out the fetched details for debugging purposes
        print("User Agent:", user_agent)
        print("IP Address:", ip_address)
        print("Timezone:", timezone)
        print("Screen Resolution:", screen_resolution)
        
        # Store user data (You can store it in a database in a real application)
        users[username] = {
            "email": email,
            "user_agent": user_agent,
            "ip_address": ip_address,
            "timezone": timezone,
            "screen_resolution": screen_resolution
        }
        
        return redirect(url_for('home'))  # Redirect to login page after registration
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    
    # Fetch user agent, IP, timezone, and resolution from the login request
    user_agent = request.headers.get('User-Agent')
    ip_address = get_ip()
    timezone = request.form['timezone']  # This will be set via JS
    screen_resolution = request.form['screen_resolution']  # Set via JS

    # Print out the fetched details for debugging purposes
    print("User Agent:", user_agent)
    print("IP Address:", ip_address)
    print("Timezone:", timezone)
    print("Screen Resolution:", screen_resolution)

    # Check if the username exists in the predefined users list
    if username in users:
        # Retrieve the stored user details for comparison
        stored_user = users[username]
        
        # Compare user details
        if (stored_user['user_agent'] == user_agent and 
            stored_user['ip_address'] == ip_address and 
            stored_user['timezone'] == timezone and 
            stored_user['screen_resolution'] == screen_resolution):
            return f"Login successful for {username}"
        else:
            return "Authentication failed. Details do not match."
    else:
        return "User not found"

if __name__ == "__main__":
    app.run(debug=True)
