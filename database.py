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
    result = connection.execute(text("select * from partner"))
    column_names = result.keys()
    partners = []
    for row in result.all():
      partners.append(dict(zip(column_names, row)))
    return partners
    
def load_organizations_from_db():
  with engine.connect() as connection:
    result_2 = connection.execute(text("select * from organization"))
    column_names_2 = result_2.keys()
    organizations = []
    for row in result_2.all():
      organizations.append(dict(zip(column_names_2, row)))
    return organizations

