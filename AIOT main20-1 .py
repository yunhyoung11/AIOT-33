from flask import Flask, request, render_template  #플라스크 웹 서버를 만들기 위한 라이브러리를 가져옴 
from gpiozero import LED   #라즈베리파이 GPIO 핀을 제어하기 위한 라이브러리를 가져옴  

app = Flask(__name__)  #플라스크 웹 어플리케이션 생성  
red_led = LED(21)   #GPIO 21번 핀에 연결된 LED를 설정 

@app.route('/')     #웹 페이지의 기본주소로 접속 시 실행되게 설정   
def home():
   return render_template("index.html")   #index.html 파일을 보여줌  

@app.route('/data', methods = ['POST'])   #/data 주소로 POST 요청이 오면 실행  
def data():
    data = request.form['led']    #데이터 중 led라는 데이터를 가져옴  
    
    if(data == 'on'):  #반은 데이터가 on이면  
        red_led.on()   #LED를 켬  
        return home()  #다시 메인페이지로 돌아감  

    elif(data == 'off'):  #받은 데이터가 off면  
        red_led.off()     #LED를 끔  
        return home()     #다시 메인페이지로 돌아감  

if __name__ == '__main__':    #이 파일을 직접 실행했을 때   
   app.run(host = '0.0.0.0', port = '80')   #모든 IP에서 80번 포트로 접속 가능   
