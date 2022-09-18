from flask import Flask, url_for
from flask import render_template

from data import content_data

app = Flask(__name__)
params = {
   'title': content_data.title,
   'departures': content_data.departures,
   'subtitle': content_data.subtitle,
   'description': content_data.description,
}

@app.route("/")
def template_index():
    return render_template("index.html",
                           tours={tour_id:content_data.tours[tour_id] for tour_id in range(1, 7)},
                           **params)

@app.route("/departures/<depart>")
def template_departure(depart):
    tours_depart = {id:tour for id, tour in content_data.tours.items() if tour['departure'] == depart}
    nights_max = max(tour['nights'] for tour in tours_depart.values())
    nights_min = min(tour['nights'] for tour in tours_depart.values())
    price_min = min(tour['price'] for tour in tours_depart.values())
    price_max = max(tour['price'] for tour in tours_depart.values())
    return render_template("departure.html",
                           depart=depart,
                           tours=tours_depart,
                           nights_max=nights_max,
                           nights_min=nights_min,
                           price_min=price_min,
                           price_max=price_max,
                           **params)

@app.route("/tours/<int:id_tour>")
def template_tours(id_tour):
    return render_template("tour.html",
                           tour=content_data.tours[id_tour],
                           **params
                           )

if __name__ == '__main__':
    app.run()

# with app.test_request_context():
#     print(url_for('template_departure', depart=123123))
#     # print(url_for('login'))
#     # print(url_for('login', next='/'))
#     # print(url_for('profile', username='John Doe'))
#     print("safasfasfasfasfasfsafsa")

# app.run('0.0.0.0', 8000, debug=True)