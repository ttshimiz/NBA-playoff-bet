#!/Users/ttshimiz/anaconda/bin/python

from nba_py import player, team, league
import pandas as pd

# These variables change every year:
# Drafted Players
taro = {'players':['Draymond Green',
                   'Stephen Curry',
                   'Klay Thompson',
                   'Kyrie Irving',
                   'Al Horford'],
        'draft_pick': [5, 2, 11, 8, 14]}

vicki = {'players':['LeBron James',
                    'Russell Westbrook',
                    'Isaiah Thomas',
                    'LaMarcus Aldridge',
                    'Kyle Lowry'],
         'draft_pick': [1, 6, 7, 13, 12]}

johnny = {'players':['Kawhi Leonard',
                     'Kevin Durant',
                     'DeMar DeRozan',
                     'Kevin Love',
                     'James Harden'],
          'draft_pick': [4, 3, 10, 15, 9]}

# Teams in the playoffs
#playoff_teams = ['GSW', 'SAS', 'HOU', 'LAC', 'UTA', 'OKC', 'MEM', 'POR',
#                 'BOS', 'CLE', 'TOR', 'WAS', 'ATL', 'MIL', 'IND', 'CHI']

# Get all of the stats for all players in the playoffs
player_stats = league.PlayerStats(season_type='Playoffs', per_mode='Totals').overall()

# Add a column for each player's total points in our scoring system
player_stats['JVT_TOTAL'] = player_stats['PTS'] + 2*(player_stats['AST'] + player_stats['REB'] +
                                                     player_stats['STL'] + player_stats['BLK'])
def get_playoff_stats(name):

#    name_split = name.split()
#    first = name_split[0]
#    last = name_split[1]
#
#    pid = player.get_player(first, last)
    stats = player_stats[player_stats['PLAYER_NAME'] == name]

    return stats


def calc_team_totals(team):

    totals = pd.DataFrame(columns=['ngames', 'points', 'assists', 'rebounds', 'steals', 'blocks', 'total'],
                          index=team)
    for p in team:

        stats = get_playoff_stats(p)
        totals.loc[p, 'ngames'] = stats['GP'].values[0]
        totals.loc[p, 'points'] = stats['PTS'].values[0]
        totals.loc[p, 'assists'] = stats['AST'].values[0]
        totals.loc[p, 'rebounds'] = stats['REB'].values[0]
        totals.loc[p, 'steals'] = stats['STL'].values[0]
        totals.loc[p, 'blocks'] = stats['BLK'].values[0]
        totals.loc[p, 'total'] = stats['JVT_TOTAL'].values[0]

    return totals


if __name__ == '__main__':

    vicki_totals = calc_team_totals(vicki)
    taro_totals = calc_team_totals(taro)
    johnny_totals = calc_team_totals(johnny)

    vicki_total_pts = (vicki_totals['points'].sum() + 2.0*(vicki_totals['assists'].sum() + vicki_totals['rebounds'].sum()) +
                      2.0*(vicki_totals['steals'].sum() + vicki_totals['blocks'].sum()))
    taro_total_pts = (taro_totals['points'].sum() + 2.0*(taro_totals['assists'].sum() + taro_totals['rebounds'].sum()) +
                      2.0*(taro_totals['steals'].sum() + taro_totals['blocks'].sum()))
    johnny_total_pts = (johnny_totals['points'].sum() + 2.0*(johnny_totals['assists'].sum() + johnny_totals['rebounds'].sum()) +
                        2.0*(johnny_totals['steals'].sum() + johnny_totals['blocks'].sum()))

    print 'TEAM\tPTS\tAST\tREB\tSTL\tBLK\tTOTAL'
    print 'VICKI\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(vicki_totals['points'].sum(),vicki_totals['assists'].sum(),vicki_totals['rebounds'].sum(),
           vicki_totals['steals'].sum(),vicki_totals['blocks'].sum(),
           vicki_total_pts)
    print 'TARO\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(taro_totals['points'].sum(),taro_totals['assists'].sum(),taro_totals['rebounds'].sum(),
           taro_totals['steals'].sum(),taro_totals['blocks'].sum(),
           taro_total_pts)
    print 'JOHNNY\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(johnny_totals['points'].sum(),johnny_totals['assists'].sum(),johnny_totals['rebounds'].sum(),
           johnny_totals['steals'].sum(),johnny_totals['blocks'].sum(),
           johnny_total_pts)



