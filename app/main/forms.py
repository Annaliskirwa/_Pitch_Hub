from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.fields.core import Label
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
  title = StringField('Title', validators = [Required()])
  description = TextAreaField("Write here your pitch",validators = [Required()])
  category = RadioField('Label', choices = [('promotionpitch', 'Promotion Pitch'), ('interviewpitch', 'Interview Pitch'), ('pickuplines', 'Pick-Up Lines'), ('productpitch', 'Product Pitch')], validators = [Required()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  description = TextAreaField('Comment here', validators = [Required()])
  submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
  submit = SubmitField()

class Downvote(FlaskForm):
  submit = SubmitField()

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell the world who you are...', validators = [Required()])
  submit = SubmitField('Submit')