from flask import Flask
from flask_restful import Api, Resource
from main import projected_points_for_week, projected_winners_for_week, projected_points_for_all, week

app = Flask(__name__)
api = Api(app)

class weekly_projections(Resource):
    def get(self):
        return projected_winners_for_week()

class score_projections(Resource):
    def get(self, week, team_id):
        points = projected_points_for_week(team_id, week)
        return {"points": points}

class get_week(Resource):
    def get(self):
        return {"week": week}

class weekly_point_projections(Resource):
    def get(self):
        return projected_points_for_all()

api.add_resource(weekly_projections, "/weeklyprojections")
api.add_resource(score_projections, "/scoreprojections/<int:week>/<int:team_id>")
api.add_resource(get_week, "/getweek")
api.add_resource(weekly_point_projections, "/getpoints")

if __name__ == "__main__":
    
    app.run(debug=True)

