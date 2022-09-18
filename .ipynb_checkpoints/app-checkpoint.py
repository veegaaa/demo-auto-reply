from flask import Flask, url_for, request
from flask import render_template
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from params import params
from params import days_of_week_dict
from params import goals
from params import time_amount_dict

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'randomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutors.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Tutor(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    about = db.Column(db.String(255*4), nullable=False)
    rating = db.Column(db.Float)
    picture = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    free = db.Column(db.JSON)
    goals = db.Column(db.JSON)

    booking = db.relationship("Booking", back_populates="tutor")


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    day_of_week = db.Column(db.String(10))
    time = db.Column(db.String(10))

    tutor = db.relationship("Tutor", back_populates="booking")
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    time_amount = db.Column(db.String(20)),
    goal = db.Column(db.String(20)),


######################################

def get_tutor_dict(tutor):
    return {
        'id': tutor.id,
        'name': tutor.name,
        'about': tutor.about,
        'rating': tutor.rating,
        'price': tutor.price,
        'picture': tutor.picture,
        'goals': tutor.goals,
        'free': tutor.free,
    }
######################################

class BookLessonForm(FlaskForm):
    name = StringField('Your name', [InputRequired()])
    phone = StringField('Your phone', [InputRequired()])
    submit = SubmitField()


class ApplySelectionForm(FlaskForm):
    comment_txt = StringField('Type request here:', [InputRequired()])
    submit = SubmitField('Request tutor search')

######################################

@app.route("/", methods=['GET','POST'])
def template_request():
    application_form = ApplySelectionForm()
    if request.method == 'GET':
        return render_template("request.html", application_form=application_form,
                           **params)
    else:
        last_comment_req=application_form.comment_txt.data
        class_name = 'class_name'
        proba = 'proba'
        return render_template("request.html", 
                               application_form=application_form,
                               last_comment_req=str(application_form.comment_txt.data),
                               class_name=class_name,
                               proba=proba,
                           **params)
        # appl = Application(
        #     student_name=application_form.name.data,
        #     phone_number=application_form.phone.data,
        #     time_amount=application_form.time_amount.data,
        #     goal=application_form.goal.data,
        # )
        # db.session.add(appl)
        # db.session.commit()
        # return render_template("request_done.html",
        #                        name=application_form.name.data,
        #                        phone=application_form.phone.data,
        #                        time_amount=time_amount_dict[application_form.time_amount.data],
        #                        goal=goals[application_form.goal.data],
        #                        **params)

# if __name__ == '__main__':
#     app.run()

# with app.test_request_context():
#     print(url_for('template_departure', depart=123123))
#     # print(url_for('login'))
#     # print(url_for('login', next='/')
#     # print(url_for('profile', username='John Doe'))
#     print("safasfasfasfasfasfsafsa")

# app.run('0.0.0.0', 8000, debug=True)