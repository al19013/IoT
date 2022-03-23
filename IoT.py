from flask import Flask,request,render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 19013

@app.route('/',methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/weight',methods=['POST'])
def update_weight():
    time=request.form["time"]
    weight = request.form["weight"]
    try:
        f=open(file_path,'w')
        f.write(time+","+weight)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/weight',methods=['GET'])
def get_weight():
    try:
        f=open(file_path,'r')
        for row in f:
            weight = row
    except Exception as e:
        print(e)
    finally:
        f.close()
        return weight

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port_num)