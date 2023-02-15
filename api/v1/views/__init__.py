#!/usr/bin/python3
""" Define Blueprint """
from flask import Blueprint

# create a Blueprint
app_views = Blueprint('app_views', __name__)

# import all routes (for this Blueprint)
from api.v1.views.states import *
from api.v1.views.index import *
