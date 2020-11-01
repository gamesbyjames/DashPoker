import dash
import dash_html_components as html
import random

image_list = ['10C.png', '10D.png', '10H.png', '10S.png', '2C.png', '2D.png', '2H.png', '2S.png', '3C.png',
                  '3D.png', '3H.png', '3S.png', '4C.png', '4D.png', '4H.png', '4S.png', '5C.png', '5D.png', '5H.png',
                  '5S.png', '6C.png', '6D.png', '6H.png', '6S.png', '7C.png', '7D.png', '7H.png', '7S.png', '8C.png',
                  '8D.png', '8H.png', '8S.png', '9C.png', '9D.png', '9H.png', '9S.png', 'AC.png', 'AD.png', 'AH.png',
                  'AS.png', 'JC.png', 'JD.png', 'JH.png', 'JS.png', 'KC.png', 'KD.png', 'KH.png', 'KS.png', 'QC.png',
                  'QD.png', 'QH.png', 'QS.png']

# Dash app and layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button(id='card', n_clicks=0)
])

@app.callback(
    dash.dependencies.Output('card', 'style'),
    [dash.dependencies.Input('card', 'n_clicks')]
)
def replace_card(n_clicks):
    y = random.randint(0, len(image_list) - 1)
    new_card = image_list[y]
    directory = "/assets/cards/"
    card_image = directory + new_card

    return {'height': '270px',
            'width': '180px',
            'border-radius': '8%',
            'background-image': 'url(' + card_image + ')',
            'background-size': 'cover'}


if __name__ == '__main__':
    app.run_server(debug=True)
