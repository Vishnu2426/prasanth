from flask import Flask,render_template,jsonify
import mysql.connector

app =Flask(__name__)

# db_config={
#     'host':'localhost',
#     'user':'root',
#     'password':'root@123',
#     'database':'prasanth'
# }

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/home') 
def  home():
    return render_template('home.html')


# def get_db_connection():
#     return mysql.connector.connect(**db_config)

# @app.route('/db')
# def db():
#     # Get database connection
#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     # Sample query (adjust to your needs)
#     cursor.execute('SELECT * FROM prasanth')
#     results = cursor.fetchall()
    
#     # Close the connection
#     cursor.close()
#     conn.close()
    
#     # Return the results as JSON
#     return jsonify(results)

if __name__=="__main__":
    app.run(debug=True)
