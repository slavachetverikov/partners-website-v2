from flask import Flask, render_template, jsonify, request
from database import load_partners_from_db, load_organizations_from_db, load_partner_from_db, load_organization_from_db

app = Flask(__name__)






@app.route("/")
def hello_partner():
    partners = load_partners_from_db()
    organizations = load_organizations_from_db()
    return render_template('home.html', partners=partners, organizations=organizations)





@app.route("/new")
def new_partner():
    return render_template('new_partner_page.html')


@app.route("/new/create", methods=['post'])
def create_partner():
  application = request.form

  # store in the DB
  # add_application_to_db(data)

  return render_template('new_partner_created.html', application=application)





@app.route("/api/organizations")
def list_organizations():
  organizations = load_organizations_from_db()
  return jsonify(organizations)



@app.route("/api/partners")
def list_partners():
  partners = load_partners_from_db()
  return jsonify(partners)





@app.route("/organization/<id>")
def show_organization(id):
  organization = load_organization_from_db(id)[0]
  if not organization:
    return 'Not Found', 404
    
  return render_template('organization_page.html',
                         organization=organization)



@app.route("/partner/<id>")
def show_partner(id):
  partner = load_partner_from_db(id)[0]
  if not partner:
    return 'Not Found', 404
  
  return render_template('partner_page.html',
                         partner=partner)
  


  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
