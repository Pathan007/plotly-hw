import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"

db = SQLAlchemy(app)

Base = automap_base()

Base.prepare(db.engine, reflect=True)


Samples_Metadata = Base.classes.sample_metadata

Samples = Base.classes.samples

SamplesMetadata = Base.classes.samples_metadata

session = Session(engine)

@app.route("/")

def default():

    sample_list_v = names()

    print(sample_list_v)

         stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.columns)[2:])

    @app.route("/metadata/<sample>")
def sample_metadata(sample):

 samples_cols_list = Base.classes.samples.__table__.columns.keys()

    sample_list = samples_cols_list[1:]

    return jsonify(samples_cols_list[1:])

 @app.route("/otu", methods=['POST','GET'])

def otu():



    otu_desc = session.query(OTU.lowest_taxonomic_unit_found).all()

    otu_descriptions = [i[0] for i in otu_desc]

    return jsonify(otu_descriptions   

    @app.route("/metadata/<sample>")
def sample_metadata(sample):
   
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.ETHNICITY,
        Samples_Metadata.GENDER,
        Samples_Metadata.AGE,
        Samples_Metadata.LOCATION,
        Samples_Metadata.BBTYPE,
        Samples_Metadata.WFREQ,
    ]

    
    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()


    @app.route("/metadata/<sample>")

def sample_metadata(sample):



    sel = [

        Samples_Metadata.sample,

        Samples_Metadata.ETHNICITY,

        Samples_Metadata.GENDER,

        Samples_Metadata.AGE,

        Samples_Metadata.LOCATION,

        Samples_Metadata.BBTYPE,

        Samples_Metadata.WFREQ,

    ]


    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

sample_metadata = {}

    for result in results:

        sample_metadata["sample"] = result[0]

        sample_metadata["ETHNICITY"] = result[1]

        sample_metadata["GENDER"] = result[2]

        sample_metadata["AGE"] = result[3]

        sample_metadata["LOCATION"] = result[4]

        sample_metadata["BBTYPE"] = result[5]

        sample_metadata["WFREQ"] = result[6]



    print(sample_metadata)

    return jsonify(sample_metadata)







@app.route("/samples/<sample>")

def samples(sample):



    stmt = db.session.query(Samples).statement

    df = pd.read_sql_query(stmt, db.session.bind)



    # Filter the data based on the sample number and

    

    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

    # Format the data to send as json

    data = {

        "otu_ids": sample_data.otu_id.values.tolist(),

        "sample_values": sample_data[sample].values.tolist(),

        "otu_labels": sample_data.otu_label.tolist(),

    }

    return jsonify(data)





if __name__ == "__main__":

    app.run()