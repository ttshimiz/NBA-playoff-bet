#!/Users/ttshimiz/anaconda/bin/python

import playoff_bet
import pandas as pd
import datetime

def create_main(totals):

    with open('../templates/index_temp.txt', 'r') as f:
        index_text = f.read()

    totals.sort_values(by='total', inplace=True, ascending=False)

    vstr = '<a href="teams/vicki.html">Vicki</a>'
    tstr = '<a href="teams/taro.html">Taro</a>'
    jstr = '<a href="teams/johnny.html">Johnny</a>'
    titles = {'vicki':vstr, 'taro':tstr, 'johnny':jstr}

    top = totals.iloc[0]
    top_title = titles[totals.index.values[0]]
    mid = totals.iloc[1]
    mid_title = titles[totals.index.values[1]]
    bot = totals.iloc[2]
    bot_title = titles[totals.index.values[2]]

    today = datetime.date.today()

    with open('../index.html', 'w') as f:
        f.write(index_text.format(top_title, top, mid_title, mid, bot_title, bot, today.isoformat()))

    return


def create_team(team, name):

    with open('../templates/team_temp.txt', 'r') as f:
        team_text = f.read()
    team.sort_values(by='total', inplace=True, ascending=False)
    p1 = team.iloc[0]
    p1_name = team.index.values[0]
    p2 = team.iloc[1]
    p2_name = team.index.values[1]
    p3 = team.iloc[2]
    p3_name = team.index.values[2]
    p4 = team.iloc[3]
    p4_name = team.index.values[3]
    p5 = team.iloc[4]
    p5_name = team.index.values[4]

    with open('../teams/'+name+'.html', 'w') as f:
        f.write(team_text.format(name.capitalize(), p1_name, p1, p2_name, p2, p3_name, p3,
                                  p4_name, p4, p5_name, p5))

    return

if __name__ == '__main__':

    vicki_totals = playoff_bet.calc_team_totals(playoff_bet.vicki)
    taro_totals = playoff_bet.calc_team_totals(playoff_bet.taro)
    johnny_totals = playoff_bet.calc_team_totals(playoff_bet.johnny)

    create_team(vicki_totals, 'vicki')
    create_team(taro_totals, 'taro')
    create_team(johnny_totals, 'johnny')

    totals = pd.DataFrame(index=['vicki', 'taro', 'johnny'],
                          columns=['points', 'assists', 'rebounds', 'steals', 'blocks', 'total'])

    totals.loc['vicki'] = pd.Series({'points': vicki_totals['points'].sum(),
                                     'assists': vicki_totals['assists'].sum(),
                                     'rebounds': vicki_totals['rebounds'].sum(),
                                     'steals': vicki_totals['steals'].sum(),
                                     'blocks': vicki_totals['blocks'].sum(),
                                     'total':  vicki_totals['total'].sum()})

    totals.loc['taro'] = pd.Series({'points': taro_totals['points'].sum(),
                                     'assists': taro_totals['assists'].sum(),
                                     'rebounds': taro_totals['rebounds'].sum(),
                                     'steals': taro_totals['steals'].sum(),
                                     'blocks': taro_totals['blocks'].sum(),
                                     'total':  taro_totals['total'].sum()})

    totals.loc['johnny'] = pd.Series({'points': johnny_totals['points'].sum(),
                                     'assists': johnny_totals['assists'].sum(),
                                     'rebounds': johnny_totals['rebounds'].sum(),
                                     'steals': johnny_totals['steals'].sum(),
                                     'blocks': johnny_totals['blocks'].sum(),
                                     'total':  johnny_totals['total'].sum()})

    create_main(totals)
