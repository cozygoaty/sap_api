from flask import Flask
import sap


app = Flask(__name__)

@app.route('/sap/', methods=['GET'])
def sap_page():
    return sap.get_random_sap_team()


@app.route('/sap/alliteration', methods=['GET'])
def sap_alliteration_page():
    return sap.get_random_sap_team_alliteration()