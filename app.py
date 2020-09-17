from flask import Flask,jsonify, request 
from flask_restful import Api, Resource
from youtubesearchpython import SearchVideos
import json
import pafy

url = "https://www.youtube.com/watch?v=SOjh073441g"

app = Flask(__name__)
api = Api(app)

link_data={'link_360': 0 , 'link_480':0 ,   'link_720': 0, 'link_1080': 0 ,'link_m4a': 0}

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
        v = pafy.new(url)
        for s in v.allstreams:
            if ('x360' in s.resolution):
                print(s)
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

api.add_resource(One, "/api/<string:name>")
api.add_resource(Mid, "/api2/")
api.add_resource(Two, "/test/")
api.add_resource(Three, "/test/360/")
if __name__ == "__main__":
    app.run(debug=True)