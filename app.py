from flask import Flask
import sap


app = Flask(__name__)


@app.route('/random/name', methods=['GET'])
def random_name_page():
    return sap.get_random_sap_team()


@app.route('/random/name/alliteration', methods=['GET'])
def random_name_alliteration_page():
    return sap.get_random_sap_team_alliteration()


