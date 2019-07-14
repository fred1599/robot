import requests

from flask import Flask, render_template, request

from .utils import parse, parse_text_wiki

app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = ''


@app.route('/', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('robot_template.html')
    else:
        query = ' '.join(parse(request.form['question']))
        search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        search_url_wiki = "https://fr.wikipedia.org/w/api.php?"

        params = {
            'input': query,
            'inputtype': 'textquery',
            'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
            'key': app.config['GOOGLEMAPS_KEY'],
            'language': 'fr-FR',
        }

        req = requests.get(url=search_url, params=params)
        result = req.json()

        if result:
            try:
                infos_dict = result['candidates'][0]
                exact_address = infos_dict['formatted_address'].split(',')
                location = infos_dict['geometry']['location']
            except IndexError:
                exact_address = ''
                location = {}

            source = "https://maps.googleapis.com/maps/api/js?key="
            source += app.config['GOOGLEMAPS_KEY']
            source += r"&callback=initMap"

            city = ''

            try:
                city = exact_address[-2].split()[1]
            except IndexError:
                if len(exact_address) == 1:
                    city = exact_address[0]

            params_wiki = {
                'action': 'query',
                'prop': 'extracts',
                'exintro': '',
                'explaintext': '',
                'titles': city,
                'format': 'json',
            }

            req_wiki = requests.get(url=search_url_wiki, params=params_wiki)
            result_wiki = req_wiki.json()

            parse_wiki = ''
            if 'query' in result_wiki:
                q = result_wiki['query']
                if 'pages' in q:
                    p = q['pages']
                    parse_wiki = parse_text_wiki(p)

            return render_template('robot_template.html',
                                   location=location,
                                   wiki=parse_wiki,
                                   query=query,
                                   address=exact_address,
            )

        else:
            return 'bad request'
