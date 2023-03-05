from flask import Flask, render_template, jsonify
from database import load_partners_from_db, load_organizations_from_db

app = Flask(__name__)






@app.route("/")
def hello_partner():
    partners = load_partners_from_db()
    organizations = load_organizations_from_db()
    return render_template('home.html', partners=partners, organizations=organizations, company_name = '"M-Partner"')




@app.route("/api/organizations")
def list_organizations():
  organizations = load_organizations_from_db()
  return jsonify(organizations)



@app.route("/api/partners")
def list_partners():
  partners = load_partners_from_db()
  return jsonify(partners)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
