import numpy as np
from flask import Flask, request, jsonify, render_template,render_template_string
import pickle
import smtplib
#import email.message
from email.message import Message
from datetime import date
import pandas as pd

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))
class Datastore():
    num_grav= None
    glicose= None
    pressao= None
    dobra= None
    insulina= None
    imc= None
    hitorico= None
    idade= None
    result_classification= None
class sistema():
    email='Colocar_seu_email_aqui@gmail.com'    
    key='Colocar_sua_senha_aqui'
data=Datastore()
sistema_operacional=sistema()
#################################################
### Código para enviar resultado por e-mail######
#################################################
def enviar_email(data,paciente,medico,contato,sistema_operacional,data_resp):
  hoje=date.today()  
  server = smtplib.SMTP('smtp.gmail.com:587')  
  email_content = f'''
  <p>Prezado(a){paciente},</p>

  </p>Segue o resultado da analise do seu exame realizado pela nossa inteligencia artificial no dia: {hoje}</p>

  {data_resp.to_html()}

  </p> De acordo com a inteligencia utilizada, seu diagnostico foi {data} para diabetes.</p>

  </p>A nossa equipe sugere que o(a) paciente, procure o(a) Dr.(a) {medico}.</p>

  <p>Grato,Equipe Vinicius Mattoso</p>'''
  
  msg =Message()
  msg['Subject'] = f'Resultado do exame avaliado no dia: {hoje}'
  
  
  msg['From'] = sistema_operacional.email
  msg['To'] = contato
  password = sistema_operacional.key
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(email_content)
  
  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) 
#######################################################################
######Inicio das paginas da aplicação##################################
#######################################################################  
@app.route('/')
def home():
    return render_template('index.html')
    #return render_template('email.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [float(x) for x in request.form.values()]
    data.num_grav=int_features[0]
    data.glicose=int_features[1]
    data.pressao=int_features[2]
    data.insulina=int_features[3]
    data.dobra=int_features[4]
    data.imc=int_features[5]
    data.historico=int_features[6]
    data.idade=int_features[7]
    #print(data.historico)
    #print(data.idade)
    #print(int_features)
    final_features = [np.array(int_features)]
    var_resp=final_features
    data.result_classification=var_resp
    prediction = model.predict(final_features)
    #print(prediction)
    

    if prediction == 0:
        #resp=Markup("<h1>Paciente sem Diabetes/<h1>")
        resp = 'Paciente sem Diabetes '
        print(resp)
        #return resp #render_template('index.html', prediction_text=resp)
        #render_template_string('{{resp}}')
        #return render_template('index.html')
        #return resp
    else:
        resp='Paciente com Diabetes '
        #resp = Markup("<h1>Paciente com Diabetes/<h1>")

        print(resp)
        #render_template_string('{{resp}}')
        #return render_template('index.html') #render_template('index.html', prediction_text=resp)
        #return  resp
    #output = round(prediction[0], 2)
    #print(output)

    #return redirect(url_for('sendemail'))
    return render_template('Resposta.html', prediction_text='{}'.format(resp))

@app.route('/email')
def email():
    return render_template('email.html')    

@app.route('/sendemail',methods=['GET', 'POST'])
def sendemail():
    '''
    For rendering results on HTML GUI
    '''
    if data.result_classification==1:
        
        classificacoa='NEGATIVO' 
    else:
        classificacoa='POSITIVO' 

    nome=request.form['paciente']
    medico=request.form['medico']
    email_destino=request.form['email_destino']
    columns=['Num. Gravid','Conc. Glicose','Pressao Diast.','Dobra Cut.','Insulina','IMC','Historico','Idade']
    valores=[data.num_grav,data.glicose,data.pressao,data.dobra,data.insulina,data.imc,data.historico,data.idade]
    data_resp=pd.DataFrame(
    {'Parametros': columns,
     'Entradas': valores,
    })
    #data_resp=data_resp.set_index('Parametros')
    print(data_resp.head())
    #resultado= request.form.values()
    print('Envinhando o E-mail')
    enviar_email(classificacoa,nome,medico,email_destino,sistema_operacional,data_resp)
    print('E-mail enviado')
    #print(nome)
    #print(medico)
    #print(email_destino)
    #print(data.a)

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)