#!/Users/ttshimiz/anaconda/bin/python

import playoff_bet
import pandas as pd
import datetime

def create_main(totals):

    with open('../templates/index_temp.txt', 'r') as f:
        index_text = f.read()

    totals.sort_values(by='total', inplace=True, ascending=False)

    top15 = create_player_rankings()

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
        f.write(index_text.format(top_title, top, mid_title, mid, bot_title, bot, today.isoformat(), top15))

    return

def create_player_rankings():

    all_stats = playoff_bet.player_stats.sort_values(by='JVT_TOTAL', ascending=False)

    for i,p in enumerate(playoff_bet.vicki['players']):
        all_stats.loc[all_stats['PLAYER_NAME'] == p,'PLAYER_NAME'] = p + ' (' + str(playoff_bet.vicki['draft_pick'][i]) + ')'

    for i,p in enumerate(playoff_bet.taro['players']):
        all_stats.loc[all_stats['PLAYER_NAME'] == p,'PLAYER_NAME'] = p + ' (' + str(playoff_bet.taro['draft_pick'][i]) + ')'

    for i,p in enumerate(playoff_bet.johnny['players']):
        all_stats.loc[all_stats['PLAYER_NAME'] == p,'PLAYER_NAME'] = p + ' (' + str(playoff_bet.johnny['draft_pick'][i]) + ')'


    top15 = all_stats.iloc[0:15]

    return top15


def create_team(team, name):

    with open('../templates/team_temp.txt', 'r') as f:
        team_text = f.read()
    team.sort_values(by='total', inplace=True, ascending=False)
    p1 = team.iloc[0]
    p1_name = team.index.values[0] + ' (' + str(team.iloc[0]['draft_order']) + ')'
    p2 = team.iloc[1]
    p2_name = team.index.values[1] + ' (' + str(team.iloc[1]['draft_order']) + ')'
    p3 = team.iloc[2]
    p3_name = team.index.values[2] + ' (' + str(team.iloc[2]['draft_order']) + ')'
    p4 = team.iloc[3]
    p4_name = team.index.values[3] + ' (' + str(team.iloc[3]['draft_order']) + ')'
    p5 = team.iloc[4]
    p5_name = team.index.values[4] + ' (' + str(team.iloc[4]['draft_order']) + ')'

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
                          columns=['ngames', 'points', 'assists', 'rebounds', 'steals', 'blocks', 'total'])

    totals.loc['vicki'] = pd.Series({'ngames': vicki_totals['ngames'].sum(),
                                     'points': vicki_totals['points'].sum(),
                                     'assists': vicki_totals['assists'].sum(),
                                     'rebounds': vicki_totals['rebounds'].sum(),
                                     'steals': vicki_totals['steals'].sum(),
                                     'blocks': vicki_totals['blocks'].sum(),
                                     'total':  vicki_totals['total'].sum()})

    totals.loc['taro'] = pd.Series({'ngames': taro_totals['ngames'].sum(),
                                     'points': taro_totals['points'].sum(),
                                     'assists': taro_totals['assists'].sum(),
                                     'rebounds': taro_totals['rebounds'].sum(),
                                     'steals': taro_totals['steals'].sum(),
                                     'blocks': taro_totals['blocks'].sum(),
                                     'total':  taro_totals['total'].sum()})

    totals.loc['johnny'] = pd.Series({'ngames': johnny_totals['ngames'].sum(),
                                     'points': johnny_totals['points'].sum(),
                                     'assists': johnny_totals['assists'].sum(),
                                     'rebounds': johnny_totals['rebounds'].sum(),
                                     'steals': johnny_totals['steals'].sum(),
                                     'blocks': johnny_totals['blocks'].sum(),
                                     'total':  johnny_totals['total'].sum()})

    create_main(totals)
