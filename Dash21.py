import dash
import dash_html_components as html
import random
import dash_core_components as dcc
from dash.exceptions import PreventUpdate

card1 = ""
card2 = ""
card3 = ""
card4 = ""
card5 = ""
dealer_card1 = ""
dealer_card2 = ""
dealer_card3 = ""
dealer_card4 = ""
dealer_card5 = ""
player_stand = False
dealer_new_game = False
player_new_game = False

image_list = ['2C.png', '2D.png', '2H.png', '2S.png', '3C.png', '3D.png', '3H.png', '3S.png',
              '4C.png', '4D.png', '4H.png', '4S.png', '5C.png', '5D.png', '5H.png', '5S.png',
              '6C.png', '6D.png', '6H.png', '6S.png', '7C.png', '7D.png', '7H.png', '7S.png',
              '8C.png', '8D.png', '8H.png', '8S.png', '9C.png', '9D.png', '9H.png', '9S.png',
              '10C.png', '10D.png', '10H.png', '10S.png', 'JC.png', 'JD.png', 'JH.png', 'JS.png',
              'QC.png', 'QD.png', 'QH.png', 'QS.png', 'KC.png', 'KD.png', 'KH.png', 'KS.png',
              'AC.png', 'AD.png', 'AH.png', 'AS.png']

deal_button_style = {'background-color': 'white',
                     'color': 'black',
                     'height': '50px',
                     'width': '100px',
                     'margin-top': '50px',
                     'margin-bottom': '30px',
                     'margin-left': '50px'}

card_values = [
    2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11
]
dealer_card_value = 0
player_card_value = 0

# Dash app and layout
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Interval(
        id='dealer_card_interval',
        disabled=True,
        interval=1000,
        n_intervals=0,
        max_intervals=7
    ),

    html.Button(id='hit_button', children='HIT', n_clicks=0, style=deal_button_style),
    html.Button(id='stand_button', children='STAND', n_clicks=0, style=deal_button_style),
    html.Button(id='new_game_button', children='NEW GAME', n_clicks=0, style=deal_button_style),
    html.H1(id='your_cards', children="Your cards "),
    html.Br(),
    html.Button(id='card1', n_clicks=0),
    html.Button(id='card2', n_clicks=0),
    html.Button(id='card3', n_clicks=0),
    html.Button(id='card4', n_clicks=0),
    html.Button(id='card5', n_clicks=0),
    html.Br(),
    html.H1(id='dealer_cards', children="Dealer cards "),
    html.Button(id='dealer_card1', n_clicks=0),
    html.Button(id='dealer_card2', n_clicks=0),
    html.Button(id='dealer_card3', n_clicks=0),
    html.Button(id='dealer_card4', n_clicks=0),
    html.Button(id='dealer_card5', n_clicks=0)

])

@app.callback(
dash.dependencies.Output('new_game_button', 'n_clicks'),
[dash.dependencies.Input('new_game_button', 'n_clicks')]
)
def start_new_game(new_game_clicks):
    global dealer_new_game, player_new_game
    if new_game_clicks > 0:
        print("NEW GAME")
        dealer_new_game = True
        player_new_game = True
    else:
        dealer_new_game = False
        player_new_game = False
    return 0


@app.callback(
    dash.dependencies.Output('card1', 'style'),
    dash.dependencies.Output('card2', 'style'),
    dash.dependencies.Output('card3', 'style'),
    dash.dependencies.Output('card4', 'style'),
    dash.dependencies.Output('card5', 'style'),
    dash.dependencies.Output('hit_button', 'n_clicks'),
    #dash.dependencies.Output('new_game_button', 'n_clicks'),
    [dash.dependencies.Input('hit_button', 'n_clicks')],
    [dash.dependencies.Input('new_game_button', 'n_clicks')]
)
def update_cards(n_clicks, new_game_clicks):  # , cards_to_replace):
    # card=[]
    global card1, card2, card3, card4, card5, player_card_value, player_stand, player_new_game

    directory = "/assets/cards/"

    print("**** update player cards **** hit_button_clicks: " + str(n_clicks) + " new_game_clicks: " + str(player_new_game))

    if player_new_game:
        player_stand = False
        player_new_game = False
        print("**** PLAYER NEW GAME ****")
        y1 = random.randint(0, len(image_list) - 1)
        card1 = image_list[y1]
        y2 = random.randint(0, len(image_list) - 1)
        card2 = image_list[y2]
        player_card_value = card_values[y1] + card_values[y2]
        print("player card value: " + str(player_card_value))
        return {
                   'height': '270px', 'width': '180px', 'border-radius': '8%',
                   'background-image': 'url(' + directory + card1 + ')',
                   'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card2 + ')',
                'background-size': 'cover'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, 0

    if (player_stand):
        print("***************PreventUpdate**********")
        raise PreventUpdate

    print("AFTER***************PreventUpdate**********")

    if n_clicks == 0:
        print("**** ZERO CLICKS")
        y1 = random.randint(0, len(image_list) - 1)
        card1 = image_list[y1]
        y2 = random.randint(0, len(image_list) - 1)
        card2 = image_list[y2]
        player_card_value = card_values[y1] + card_values[y2]
        print("player card value: " + str(player_card_value))
        return {
                   'height': '270px', 'width': '180px', 'border-radius': '8%',
                   'background-image': 'url(' + directory + card1 + ')',
                   'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card2 + ')',
                'background-size': 'cover'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, n_clicks
    elif n_clicks == 1:
        print(">>>> FIRST CLICKS")
        y = random.randint(0, len(image_list) - 1)
        card3 = image_list[y]
        player_card_value += card_values[y]
        print("player card value: " + str(player_card_value))
        #replace_dealer_card(1)
        return {
                   'height': '270px', 'width': '180px', 'border-radius': '8%',
                   'background-image': 'url(' + directory + card1 + ')',
                   'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card2 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card3 + ')',
                'background-size': 'cover'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, n_clicks
    elif n_clicks == 2:
        y = random.randint(0, len(image_list) - 1)
        card4 = image_list[y]
        player_card_value += card_values[y]
        print("player card value: " + str(player_card_value))
        return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card1 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card2 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card3 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card4 + ')',
                'background-size': 'cover'}, \
               {'background-color': 'Transparent',
                   'border-color': 'Transparent'}, n_clicks
    elif n_clicks == 3:
        y = random.randint(0, len(image_list) - 1)
        card5 = image_list[y]
        player_card_value += card_values[y]
        print("player card value: " + str(player_card_value))
        return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card1 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card2 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card3 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card4 + ')',
                'background-size': 'cover'}, \
               {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + card5 + ')',
                'background-size': 'cover'}, n_clicks


@app.callback(
    dash.dependencies.Output('dealer_card1', 'style'),
    dash.dependencies.Output('dealer_card2', 'style'),
    dash.dependencies.Output('dealer_card3', 'style'),
    dash.dependencies.Output('dealer_card4', 'style'),
    dash.dependencies.Output('dealer_card5', 'style'),
    dash.dependencies.Output('dealer_card_interval', 'disabled'),
    dash.dependencies.Output('dealer_card_interval', 'n_intervals'),
    dash.dependencies.Output('stand_button', 'n_clicks'),
    #dash.dependencies.Output('new_game_button', 'n_clicks'),
    [dash.dependencies.Input('stand_button', 'n_clicks')],
    [dash.dependencies.Input('new_game_button', 'n_clicks')],
    [dash.dependencies.Input('dealer_card_interval', 'n_intervals')]
)
def replace_dealer_card(n_clicks, new_game_clicks, n_intervals):
    global dealer_card1, dealer_card2, dealer_card3, dealer_card4, dealer_card4, dealer_card_value, player_stand, dealer_new_game
    directory = "/assets/cards/"

    print ("dealer card function:" + str(n_clicks) + " : " + str(n_intervals))

    if dealer_new_game:
        dealer_new_game = False
        print("**** DEALER NEW GAME ****")
        player_stand = False
        y = random.randint(0, len(image_list) - 1)
        dealer_card1 = image_list[y]
        dealer_card_value = card_values[y]
        print("dealer card value: " + str(dealer_card_value))
        return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + dealer_card1 + ')',
                'background-size': 'cover'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, True, 0, 0

    if n_clicks == 0:
        new_game = False
        player_stand = False
        y = random.randint(0, len(image_list) - 1)
        dealer_card1 = image_list[y]
        dealer_card_value = card_values[y]
        print("dealer card value: " + str(dealer_card_value))
        return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                'background-image': 'url(' + directory + dealer_card1 + ')',
                'background-size': 'cover'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, {
                   'background-color': 'Transparent',
                   'border-color': 'Transparent'}, True, 0, n_clicks
    if n_clicks > 0:
        player_stand = True
        print ("------ n_clicks > 0 ------")
        if n_intervals == 0:
            print("------ n_intervals = 0 ------")
            y = random.randint(0, len(image_list) - 1)
            dealer_card2 = image_list[y]
            dealer_card_value += card_values[y]
            print("dealer card value: " + str(dealer_card_value))
            if dealer_card_value > 16:
                new_game = False
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, True, 0, n_clicks
            else:
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, False, n_intervals, n_clicks
        elif n_intervals == 1:
            print("------ n_intervals = 1 ------")
            y = random.randint(0, len(image_list) - 1)
            dealer_card3 = image_list[y]
            dealer_card_value += card_values[y]
            print("dealer card value: " + str(dealer_card_value))
            if dealer_card_value < 17:
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, False, n_intervals, n_clicks
            else:
                new_game = False
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, True, 0, n_clicks
        elif n_intervals == 2:
            print("------ n_intervals = 2 ------")
            y = random.randint(0, len(image_list) - 1)
            dealer_card4 = image_list[y]
            dealer_card_value += card_values[y]
            print("dealer card value: " + str(dealer_card_value))
            if dealer_card_value < 17:
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card4 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, False, n_intervals, n_clicks
            else:
                new_game = False
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card4 + ')',
                        'background-size': 'cover'}, {
                           'background-color': 'Transparent',
                           'border-color': 'Transparent'}, True, 0, n_clicks
        elif n_intervals == 3:
            print("------ n_intervals = 3 ------")
            y = random.randint(0, len(image_list) - 1)
            dealer_card5 = image_list[y]
            dealer_card_value += card_values[y]
            print("dealer card value: " + str(dealer_card_value))
            if dealer_card_value < 17:
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card4 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card5 + ')',
                        'background-size': 'cover'}, False, n_intervals, n_clicks
            else:
                new_game = False
                return {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card1 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card2 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card3 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card4 + ')',
                        'background-size': 'cover'}, {'height': '270px', 'width': '180px', 'border-radius': '8%',
                        'background-image': 'url(' + directory + dealer_card5 + ')',
                        'background-size': 'cover'}, True, 0, n_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
