from nba_py import player
import pandas as pd

# Drafted Players
taro = ['Draymond Green',
        'Kevin Love',
        'Hassan Whiteside',
        'Russell Westbrook',
        'Luol Deng']
        
vicki = ['Stephen Curry',
         'Klay Thompson',
         'Chris Paul',
         'Kawhi Leonard',
         'Kevin Durant']
         
johnny = ['Lebron James',
          'Kyrie Irving',
          'Dwyane Wade',
          'LaMarcus Aldridge',
          'Kyle Lowry']
          
def get_playoff_stats(name):

    name_split = name.split()
    first = name_split[0]
    last = name_split[1]
    
    pid = player.get_player(first, last)
    stats = player.PlayerGameLogs(pid, season_type='Playoffs')
    
    return stats.info()
    

def calc_team_totals(team):
    
    totals = pd.DataFrame(columns=['points', 'assists', 'rebounds', 'steals', 'blocks'],
                          index=team)
    for p in team:
    
        stats = get_playoff_stats(p)
        totals.loc[p, 'points'] = stats['PTS'].sum()
        totals.loc[p, 'assists'] = stats['AST'].sum()
        totals.loc[p, 'rebounds'] = stats['REB'].sum()
        totals.loc[p, 'steals'] = stats['STL'].sum()
        totals.loc[p, 'blocks'] = stats['BLK'].sum()
        
    return totals
    
    
if __name__ == '__main__':

    vicki_totals = calc_team_totals(vicki)
    taro_totals = calc_team_totals(taro)
    johnny_totals = calc_team_totals(johnny)
    
    vicki_total_pts = (vicki_totals['points'].sum() + 1.5*(vicki_totals['assists'].sum() + vicki_totals['rebounds'].sum()) +
                      2.0*(vicki_totals['steals'].sum() + vicki_totals['blocks'].sum()))
    taro_total_pts = (taro_totals['points'].sum() + 1.5*(taro_totals['assists'].sum() + taro_totals['rebounds'].sum()) +
                      2.0*(taro_totals['steals'].sum() + taro_totals['blocks'].sum()))
    johnny_total_pts = (johnny_totals['points'].sum() + 1.5*(johnny_totals['assists'].sum() + johnny_totals['rebounds'].sum()) +
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
    
    
    
        