import dash
import dash_html_components as html

#import glob
#import os

import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

deal_button_style = {'background-color': 'white',
                     'color': 'black',
                     'height': '50px',
                     'width': '100px',
                     'margin-top': '50px',
                     'margin-bottom': '30px',
                     'margin-left': '50px'}

hold_button_style = {'background-color': 'white',
                     'color': 'black',
                     'height': '40px',
                     'width': '150px',
                     'margin-top': '30x',
                     'margin-left': '15px',
                     'margin-right': '15px'}

discard_button_style = {'background-color': 'red',
                        'color': 'black',
                        'height': '40px',
                        'width': '150px',
                        'margin-top': '30x',
                        'margin-left': '15px',
                        'margin-right': '15px'}

image_list = ['10C.png', '10D.png', '10H.png', '10S.png', '2C.png', '2D.png', '2H.png', '2S.png', '3C.png',
                  '3D.png', '3H.png', '3S.png', '4C.png', '4D.png', '4H.png', '4S.png', '5C.png', '5D.png', '5H.png',
                  '5S.png', '6C.png', '6D.png', '6H.png', '6S.png', '7C.png', '7D.png', '7H.png', '7S.png', '8C.png',
                  '8D.png', '8H.png', '8S.png', '9C.png', '9D.png', '9H.png', '9S.png', 'AC.png', 'AD.png', 'AH.png',
                  'AS.png', 'JC.png', 'JD.png', 'JH.png', 'JS.png', 'KC.png', 'KD.png', 'KH.png', 'KS.png', 'QC.png',
                  'QD.png', 'QH.png', 'QS.png']

# initial hand of 5 cards
value = [0, 1, 2, 3, 4]
card = []
index = []

deal = True

children = 'Deal'

total = 100
bet = 5

for num in value:
    ans = random.randint(0, len(image_list) - 1)
    while ans in index:
        ans = random.randint(0, len(image_list) - 1)
    index.append(ans)
    card.append(image_list[ans])
    print(card[num])

print(card)
print("READY")
# reset win counters
num_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # number cards, colored cards and suits


def calculate_win(cards=[], deal=False):
    global total, bet
    if deal:
        score = -1 * bet  # default is you pay the bet to play
    # cards = ['QS.png', '6.png', '6C.png', 'QC.png', '6D.png']
    for item in cards:
        print("cool", item)
        # hearts 14, spades 15, diamonds 16, clubs 17
        if 'H' in item:
            num_count[14] = num_count[14] + 1
            print("hearts ", item)
        elif 'S' in item:
            num_count[15] = num_count[15] + 1
            print("spades ", item)
        elif 'D' in item:
            num_count[16] = num_count[16] + 1
            print("diamonds ", item)
        elif 'C' in item:
            num_count[17] = num_count[17] + 1
            print("clubs ", item)
        if 'J' in item:
            num_count[11] = num_count[11] + 1
        elif 'Q' in item:
            num_count[12] = num_count[12] + 1
        elif 'K' in item:
            num_count[13] = num_count[13] + 1
        elif 'A' in item:
            num_count[1] = num_count[1] + 1
        for num in range(2, 11):
            if str(num) in item:
                num_count[num] = num_count[num] + 1
                # print("loop ",num, " occurances: ", num_count[num])
    win_string = ""
    temp_win_string = ""
    num_pairs = 0
    three_of_a_kind = False
    min_val = 14
    max_val = 0
    for num in range(1, 14):
        # print(num, " occurances: ", num_count[num])
        if num_count[num] > 0 and num < min_val:
            min_val = num
        elif num_count[num] > 0 and num > max_val:
            max_val = num
        print("-------> MIN: ", min_val, "MAX", max_val)
        if num_count[num] == 2:
            if not three_of_a_kind:

                if num > 1 and num < 11:
                    win_string = "        pair of " + str(num) + "s !"
                elif num == 1:
                    win_string = "        pair of Aces !"
                elif num == 11:
                    win_string = "        pair of Jacks !"
                elif num == 12:
                    win_string = "        pair of Queens !"
                elif num == 13:
                    win_string = "        pair of Kings !"

                num_pairs = num_pairs + 1
                print("a pair : ", win_string, " num of pairs: ", num_pairs)
                if deal:
                    score = bet
            else:
                win_string = "        FULL HOUSE!"
                if deal:
                    score = bet * 5
        elif num_count[num] == 3:
            three_of_a_kind = True
            if num_pairs == 0:
                win_string = "        3 of a kind"
                if deal:
                    score = bet * 3
            else:
                win_string = "        full house!"
                if deal:
                    score = bet * 5
        elif num_count[num] == 4:
            win_string = "        4 of a kind"
            if deal:
                score = bet * 10

    print("Outside Loop -------> MIN: ", min_val, "MAX", max_val)
    print("win string is: ", win_string)

    if win_string == "" and max_val - min_val == 4:
        temp_win_string = "        straight"
    elif win_string == "" and num_count[1] == 1 and num_count[10] == 1 and num_count[11] == 1 and num_count[12] == 1 and \
            num_count[13] == 1:  # straight to the Ace
        temp_win_string = "        straight!"

    for num in range(14, 18):
        if num_count[num] == 5:
            win_string = "        flush!"
            if deal:
                score = bet * 5

    if temp_win_string == "        straight":
        if win_string == "        flush!":
            win_string = "        straight flush!"
            if deal:
                score = bet * 10
        else:  # just a straight
            win_string = temp_win_string
            if deal:
                score = bet * 3
    if temp_win_string == "        straight!":
        if win_string == "        flush!":
            win_string = "        ROYAL FLUSH!"
            if deal:
                score = bet * 50
        else:  # just a straight (to the Ace)
            win_string = temp_win_string
            if deal:
                score = bet * 3

    if num_pairs == 2:
        win_string = "two pairs"
        if deal:
            score = bet * 2

    if deal:
        total += score

    print(num_count)
    print("win_string is", win_string)

    return num_count, win_string


# Dash app and layout
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([

    html.H1(id='score', children="Total: " + str(total)),

    html.Button(id='card_button_1', n_clicks=0),
    html.Button(id='card_button_2', n_clicks=0),
    html.Button(id='card_button_3', n_clicks=0),
    html.Button(id='card_button_4', n_clicks=0),
    html.Button(id='card_button_5', n_clicks=0),

    html.Button(id='deal_button', n_clicks=0, style=deal_button_style),

    html.Br(),

    html.Button(id='card_hold_1', n_clicks=0),
    html.Button(id='card_hold_2', n_clicks=0),
    html.Button(id='card_hold_3', n_clicks=0),
    html.Button(id='card_hold_4', n_clicks=0),
    html.Button(id='card_hold_5', n_clicks=0),

    html.Br(),
    html.H1(id='win_string')

])


# html.Img(children=[i for i in image_list]),

@app.callback(
    dash.dependencies.Output('card_hold_1', 'children'),
    dash.dependencies.Output('card_hold_1', 'style'),
    [dash.dependencies.Input('card_button_1', 'n_clicks')]
)
def update_hold_text(n_clicks):
    global deal
    global hold_button_style
    global discard_button_style
    print("*******card 1 clicks", n_clicks)
    if deal == True:
        print("*******DEAL so do NOTHING and return!")
        hold_string_1 = "DISCARD"
        card_1_style = discard_button_style
        return hold_string_1, card_1_style
    else:
        print("*******Still in the DRAW!")
    hold_string_1 = "HOLD"

    card_1_style = hold_button_style
    if n_clicks % 2 == 1:
        hold_string_1 = "DISCARD"
        card_1_style = discard_button_style
    return hold_string_1, card_1_style


@app.callback(
    dash.dependencies.Output('card_hold_2', 'children'),
    dash.dependencies.Output('card_hold_2', 'style'),
    [dash.dependencies.Input('card_button_2', 'n_clicks')]
)
def update_hold_text(n_clicks):  #
    # print("card 2 clicks", n_clicks)
    global deal
    global hold_button_style
    global discard_button_style
    # print("*******card 2 clicks", n_clicks)
    if deal == True:
        # print("*******DEAL so do NOTHING and return!")
        hold_string_2 = "DISCARD"
        card_2_style = discard_button_style
        return hold_string_2, card_2_style
    hold_string_2 = "HOLD"
    card_2_style = hold_button_style
    if n_clicks % 2 == 1:
        hold_string_2 = "DISCARD"
        card_2_style = discard_button_style
    return hold_string_2, card_2_style


@app.callback(
    dash.dependencies.Output('card_hold_3', 'children'),
    dash.dependencies.Output('card_hold_3', 'style'),
    [dash.dependencies.Input('card_button_3', 'n_clicks')]
)
def update_hold_text(n_clicks):
    # print("card 3 clicks", n_clicks)
    global deal
    global hold_button_style
    global discard_button_style
    # print("*******card 3 clicks", n_clicks)
    if deal == True:
        # print("*******DEAL so do NOTHING and return!")
        hold_string_3 = "DISCARD"
        card_3_style = discard_button_style
        return hold_string_3, card_3_style
    hold_string_3 = "HOLD"
    card_3_style = hold_button_style
    if n_clicks % 2 == 1:
        hold_string_3 = "DISCARD"
        card_3_style = discard_button_style
    return hold_string_3, card_3_style


@app.callback(
    dash.dependencies.Output('card_hold_4', 'children'),
    dash.dependencies.Output('card_hold_4', 'style'),
    [dash.dependencies.Input('card_button_4', 'n_clicks')]
)
def update_hold_text(n_clicks):
    # print("card 4 clicks", n_clicks)
    global deal
    global hold_button_style
    global discard_button_style
    # print("*******card 4 clicks", n_clicks)
    if deal == True:
        # print("*******DEAL so do NOTHING and return!")
        hold_string_4 = "DISCARD"
        card_4_style = discard_button_style
        return hold_string_4, card_4_style
    hold_string_4 = "HOLD"
    card_4_style = hold_button_style
    if n_clicks % 2 == 1:
        hold_string_4 = "DISCARD"
        card_4_style = discard_button_style
    return hold_string_4, card_4_style


@app.callback(
    dash.dependencies.Output('card_hold_5', 'children'),
    dash.dependencies.Output('card_hold_5', 'style'),
    [dash.dependencies.Input('card_button_5', 'n_clicks')]
)
def update_hold_text(n_clicks):
    # print("card 5 clicks", n_clicks)
    global deal
    global hold_button_style
    global discard_button_style
    # print("*******card 5 clicks", n_clicks)
    if deal == True:
        # print("*******DEAL so do NOTHING and return!")
        hold_string_5 = "DISCARD"
        card_5_style = discard_button_style
        return hold_string_5, card_5_style
    hold_string_5 = "HOLD"
    card_5_style = hold_button_style
    if n_clicks % 2 == 1:
        hold_string_5 = "DISCARD"
        card_5_style = discard_button_style
    return hold_string_5, card_5_style


@app.callback(

    dash.dependencies.Output('score', 'children'),
    dash.dependencies.Output('card_button_1', 'n_clicks'),
    dash.dependencies.Output('card_button_2', 'n_clicks'),
    dash.dependencies.Output('card_button_3', 'n_clicks'),
    dash.dependencies.Output('card_button_4', 'n_clicks'),
    dash.dependencies.Output('card_button_5', 'n_clicks'),
    dash.dependencies.Output('card_button_1', 'style'),
    dash.dependencies.Output('card_button_2', 'style'),
    dash.dependencies.Output('card_button_3', 'style'),
    dash.dependencies.Output('card_button_4', 'style'),
    dash.dependencies.Output('card_button_5', 'style'),
    dash.dependencies.Output('deal_button', 'children'),
    dash.dependencies.Output('win_string', 'children'),
    [dash.dependencies.Input('deal_button', 'n_clicks')],
    [dash.dependencies.State('card_button_1', 'n_clicks')],
    [dash.dependencies.State('card_button_2', 'n_clicks')],
    [dash.dependencies.State('card_button_3', 'n_clicks')],
    [dash.dependencies.State('card_button_4', 'n_clicks')],
    [dash.dependencies.State('card_button_5', 'n_clicks')])
def update_cards(n_clicks, n1, n2, n3, n4, n5):  # , cards_to_replace):

    # print("XXX", n1, n2, n3, n4, n5)
    global total
    global deal

    cards_to_replace = []
    if not deal:
        if n1 % 2 == 1:
            cards_to_replace.append(0)
        if n2 % 2 == 1:
            cards_to_replace.append(1)
        if n3 % 2 == 1:
            cards_to_replace.append(2)
        if n4 % 2 == 1:
            cards_to_replace.append(3)
        if n5 % 2 == 1:
            cards_to_replace.append(4)
    else:
        cards_to_replace = [0, 1, 2, 3, 4]

    # print ("YYY", cards_to_replace)

    for x in cards_to_replace:
        y = random.randint(0, len(image_list) - 1)

        while y in index:
            y = random.randint(0, len(image_list) - 1)

        index[x] = y
        card[x] = image_list[y]

    directory = "/assets/cards/"

    # global deal
    n_click_list = [0, 0, 0, 0, 0]

    if n_clicks % 2 == 0:
        button_text = "DRAW"
        deal = False
        n_click_list = [0, 0, 0, 0, 0]
    else:
        button_text = "DEAL"
        deal = True
        n_click_list = [1, 1, 1, 1, 1]

    # print(button_text)
    # print("AAA ", n_click_list[0], n_click_list[1], n_click_list[2], n_click_list[3], n_click_list[4])
    print(card)

    global num_count
    num_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # reset counters
    win_string = ""
    num_count, win_string = calculate_win(card, deal)
    # for num in range(1, 14):
    #    print("win for ", num, " occurances: ", num_count[num])

    score_string = "SCORE: " + str(total)

    print("---------------")
    return score_string, n_click_list[0], n_click_list[1], n_click_list[2], n_click_list[3], n_click_list[4], {
        'height': '270px', 'width': '180px',
        'background-image': 'url(' + directory + card[0] + ')',
        'background-size': 'cover'}, {'height': '270px',
        'width': '180px',
        'background-image': 'url(' + directory + card[1] + ')',
        'background-size': 'cover'}, {'height': '270px',
        'width': '180px',
        'background-image': 'url(' + directory + card[2] + ')',
        'background-size': 'cover'}, {'height': '270px',
        'width': '180px',
        'background-image': 'url(' + directory + card[3] + ')',
        'background-size': 'cover'}, {'height': '270px',
        'width': '180px',
        'background-image': 'url(' + directory + card[4] + ')',
        'background-size': 'cover'}, button_text, win_string


if __name__ == '__main__':
    app.run_server(debug=True)
