import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient

# MongoDB connection setup
def get_mongodb_collection():
    # Adjust the URL if using MongoDB Atlas or remote database
    client = MongoClient('mongodb://localhost:27017/')  
    db = client['emailDB']  # Database name
    collection = db['users']  # Collection name
    return collection

# Get user data from MongoDB
def get_user_email_and_signature(user_id):
    collection = get_mongodb_collection()
    print(f"Attempting to fetch user with ID: {user_id}")
    user_data = collection.find_one({"user_id": user_id})
    print(f"User data fetched: {user_data}")
    if user_data:
        return user_data['email'], user_data['signature']
    else:
        return None, None

# Insert sample user data into MongoDB if needed
def insert_sample_user():
    collection = get_mongodb_collection()
    # Check if the user already exists
    if not collection.find_one({"user_id": 1}):
        print("Inserting sample user data into MongoDB...")
        collection.insert_one({
            "user_id": 1,
            "email": "your-email@gmail.com",
            "signature": "Best regards,\ndreammailer"
        })
        print("Sample user inserted.")
    else:
        print("Sample user already exists in the database.")

# Function to create email content
def create_email_content(body_text, signature):
    return f"{body_text}\n\n{signature}"

# Send email function
def send_email(from_email, to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Using Gmail's SMTP server or any other SMTP service
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        from_email = "sausabita4@gmail.com"
        server.login(from_email, "imbw iqvc idmz agwc")  # Replace with your email and password
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function
if __name__ == '__main__':
    user_id = 1  # Example user ID
    to_email = "satyabratatripathy02@gmail.com"
    subject = "Your Subject Here"
    body_text = "Hello, this is the email content."

    # Insert sample data for testing purposes (optional)
    insert_sample_user()

    # Fetch email and signature from MongoDB
    from_email, signature = get_user_email_and_signature(user_id)

    if from_email and signature:
        # Create email content with body and signature
        email_content = create_email_content(body_text, signature)
        # Send the email
        send_email(from_email, to_email, subject, email_content)
    else:
        print(f"User with ID {user_id} not found in MongoDB.")
