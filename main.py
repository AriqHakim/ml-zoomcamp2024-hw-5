import pickle
from flask import Flask, request, jsonify

model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in: 
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in: 
    dv = pickle.load(f_in)

q1 = {"job": "management", "duration": 400, "poutcome": "success"}

# X = dv.transform([q1])
# y_pred = model.predict_proba(X)[:, 1]
# print(y_pred)
# # 0.759

def pred_cust(data):
    X = dv.transform([data])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

app = Flask('job')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    result = {
        "pred": pred_cust(customer)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6969)