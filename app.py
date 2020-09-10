from flask import Flask
from flask_restful import Api, Resource
from youtubesearchpython import SearchVideos
import json
import pafy

url = "https://www.youtube.com/watch?v=SOjh073441g"

app = Flask(__name__)
api = Api(app)


class One(Resource):

    def get(self,name):
        try:
            search = SearchVideos(name, offset = 1, mode = "json", max_results = 20)
            return json.loads(search.result())
        except:
            return "Fail"

class Two(Resource):

    def get(self):
        
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        return {'id': str(playurl)}
        #except:
        #    return "Fail"

api.add_resource(One, "/api/<string:name>")
api.add_resource(Two, "/test/")
if __name__ == "__main__":
    app.run(debug=True)