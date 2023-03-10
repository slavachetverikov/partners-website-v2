from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem",
    }
  })



def load_partners_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM partner"))
    column_names = result.keys()
    partners = []
    for row in result.all():
      partners.append(dict(zip(column_names, row)))
    return partners

    
def load_organizations_from_db():
  with engine.connect() as connection:
    result_2 = connection.execute(text("SELECT * FROM organization"))
    column_names_2 = result_2.keys()
    organizations = []
    for row in result_2.all():
      organizations.append(dict(zip(column_names_2, row)))
    return organizations



    
def load_partner_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM partner WHERE partner_id ={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]



    
def load_organization_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM organization WHERE org_id ={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]



      
# def add_application_to_db(data):
#   with engine.connect() as conn:
#     query = text("INSERT INTO partner (full_name, phone, email, country) VALUES (:full_name, :phone, :email, :country)")
  
#     conn.execute(query, 
#                  full_name=data.get('full_name'), 
#                  phone=data.get('phone'),
#                  email=data.get('email'), 
#                  country=data.get('country'))

