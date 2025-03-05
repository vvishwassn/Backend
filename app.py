from flask import Flask, request, jsonify
import supabase

app = Flask(__name__)

# Supabase connection
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')

    # Insert into Supabase table "responses"
    supabase_client.table("responses").insert({"name": name}).execute()

    return jsonify({"message": "Name submitted successfully!"})

@app.route('/admin', methods=['GET'])
def admin():
    # Fetch all names from the database
    response = supabase_client.table("responses").select("*").execute()
    return jsonify(response.data)

if __name__ == '__main__':
    app.run(debug=True)
