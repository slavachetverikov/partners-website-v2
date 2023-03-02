from flask import Flask, render_template, jsonify

app = Flask(__name__)


PARTNERS = [
  {
    'partner_id':1,
    'full_name': 'Butler John Arthur',
    'phone': '+7(981)123-45-67',
    'email': 'john.butler@gmail.com',
    'country': 'Moscow'
  },
    {
    'partner_id':2,
    'full_name': 'Miklasheva Olga Viktorovna',
    'phone': '+7(960)143-45-67',
    'email': 'ol.miklasheva@mail.ru',
    'country': 'Saint Petersburg'
  },
    {
    'partner_id':3,
    'full_name': 'Svetova Yana Michailovna ',
    'phone': '+7(960)343-41-57',
    'email': 'yana.svetova@gmail.com',
    'country': 'Saint Petersburg'
  },
    {
    'partner_id':4,
    'full_name': 'Svenskaya Irina Gennadievna',
    'phone': '+7(960)103-35-80',
    'email': 'irina-svenskaya1978@mail.ru',
    'country': 'Saint Petersburg'
  },
    {
    'partner_id':5,
    'full_name': 'Kolesov Ivan Leonidovch',
    'phone': '+7(960)178-49-60',
    'email': 'ivan.kolesov@gmail.com',
    'country': 'Moscow'
  },
    {
    'partner_id':6,
    'full_name': 'Ivanov Vladimir Alexeevich',
    'phone': '+7(960)373-59-30',
    'email': 'ivanov.vlad@gmail.com',
    'country': 'Saint Petersburg'
  },
    {
    'partner_id':7,
    'full_name': 'Karpovich Alina Alexeevna',
    'phone': '+7(964)123-49-56',
    'email': 'k.alina1974@gmail.com',
    'country': 'Novgorod'
  }
]

ORGANIZATIONS = [
  {
    'org_id':1,
    'org_name': 'Grid Dynamics',
    'trade_code': 1215,
    'country': 'Saint Petersburg',
    'image': "https://partners-website.slavchetverikov.repl.co/static/grid.png",
    'description': "A leading provider of engineering and consulting services,  cloud computing, big data, and machine learning applications."
    
  },  
  {
    'org_id':2,
    'org_name': 'Worldwide Clinical Trials',
    'trade_code': 1212,
    'country': 'Moscow',
    'image': "https://partners-website.slavchetverikov.repl.co/static/wct.jpeg",
    'description': "A leading therapeutically focused Contract Research Organization (CRO) that applies deep therapeutic expertise to help customers achieve their drug development goals."
  },
  {
    'org_id':3,
    'org_name': 'Intermedia',
    'trade_code': 1213,
    'country': 'Saint Petersburg',
    'image': "https://partners-website.slavchetverikov.repl.co/static/intermedia.png",
    'description': "A cloud communications company that helps over 130,000 businesses connect better – through voice, video conferencing, chat, and more."
  } 
]


@app.route("/api/partners")
def list_partners():
  return jsonify(PARTNERS)

  

@app.route("/")
def hello_partner():
    return render_template('home.html', partners=PARTNERS, organizations=ORGANIZATIONS, company_name = '"M-Partner"')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
