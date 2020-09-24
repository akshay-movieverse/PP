from flask import Flask,jsonify, request 
from flask_restful import Api, Resource
from youtubesearchpython import SearchVideos
from flask_cors import CORS, cross_origin
import json
import pafy


url = "https://www.youtube.com/watch?v=pr-4GbR4DpQ"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api3": {"origins": "*"}})

api = Api(app)

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


link_data={'link_360': 0 , 'link_480':0 ,   'link_720': 0, 'link_1080': 0 ,'link_m4a': 0}

@app.route('/api3', methods=['POST'])
@cross_origin(origin='*')#,headers=['Content- Type','Authorization'])
def foo():
    try:
        data = request.get_json('data')
        link=data['link']
        #print(link)
        v = pafy.new(link)
        for s in v.allstreams:
            if ('x360' in s.resolution):
                    #print(s)
                link_data['link_360']=s.url
            elif ('x480' in s.resolution):
                link_data['link_480']=s.url
            elif ('x720' in s.resolution):
                link_data['link_720']=s.url
            elif ('x1080' in s.resolution):
                link_data['link_1080']=s.url
            elif ('m4a' in s.extension):
                link_data['link_m4a']=s.url
            else:
                pass

            #data = request.json('data')
            #data = request.args.get('data')     # status code 
            #print(data)

        return jsonify(link_data)    
    #return "HELL"
    except:
        return "FAIL"



class One(Resource):

    def get(self,name):
        try:
            search = SearchVideos(name, offset = 1, mode = "json", max_results = 20)
            return json.loads(search.result())
        except:
            return "Fail"
class Mid(Resource):

    def post(self):      
        data = request.get_json('data')
        link=data['link']
        #print(link)
        v = pafy.new(link)
        for s in v.allstreams:
            if ('x360' in s.resolution):
                #print(s)
                link_data['link_360']=s.url
            elif ('x480' in s.resolution):
                link_data['link_480']=s.url
            elif ('x720' in s.resolution):
                link_data['link_720']=s.url
            elif ('x1080' in s.resolution):
                link_data['link_1080']=s.url
            elif ('m4a' in s.extension):
                link_data['link_m4a']=s.url
            else:
                pass

        #data = request.json('data')
        #data = request.args.get('data')     # status code 
        #print(data)

        return jsonify(link_data)    #json.loads({'data':"HELLAA"}) , 201 #jsonify({'data': 'HELLL'}), 201
 


class Two(Resource):

    def get(self):
        try:
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url
            return {'id': str(playurl)}
        except:
            return "Fail"
class Three(Resource):

    def get(self):
        try:
            video = pafy.new(url)
            test=video.streams
            playurl=test[1].url
            return {'id': str(playurl)}
        except:
            return "Fail"

class Four(Resource):
    
    @cross_origin(origin='*')
    def get(self,name):
        try:
            #data = name
            #link=data['link']
            #print(link)

            link="https://www.youtube.com/watch?v="+name
            v = pafy.new(link)
            for s in v.allstreams:
                if ('x360' in s.resolution):
                        #print(s)
                    link_data['link_360']=s.url
                elif ('x480' in s.resolution):
                    link_data['link_480']=s.url
                elif ('x720' in s.resolution):
                    link_data['link_720']=s.url
                elif ('x1080' in s.resolution):
                    link_data['link_1080']=s.url
                elif ('m4a' in s.extension):
                    link_data['link_m4a']=s.url
                else:
                    pass

                #data = request.json('data')
                #data = request.args.get('data')     # status code 
                #print(data)

            return jsonify(link_data)    
        #return "HELL"
        except:
            return "FAIL"



api.add_resource(One, "/api/<string:name>")
api.add_resource(Mid, "/api2/")
api.add_resource(Four,'/api4/<string:name>')
api.add_resource(Two, "/test/")
api.add_resource(Three, "/test/360/")
if __name__ == "__main__":
    app.run(debug=True)