from flask import Flask,request,jsonify
from model import recommend
from flask_cors import CORS


app=Flask(__name__)
CORS(app)

@app.route("/recommend",methods=['POST'])
def recommend_anime():
    data=request.get_json()
    anime_name=data.get("anime",'')
    recommended,found=recommend(anime_name)
    if not found:
        return jsonify({'error':"not found",'recommend':[]}), 404
    return jsonify({"recommend":recommended})
if __name__=='__main__':
    app.run(debug=True)        