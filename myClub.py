from fastapi import FastAPI
from typing import Optional

app=FastAPI()

Clubs = {
   'team_1'  :  {'name':'Manchester City','Points':53},
   'team_2'  :  {'name':'Chelsea','Points':43},
   'team_3'  :  {'name':'Liverpool','Points':42},
   'team_4'  :  {'name':'West Ham','Points':41},
   'team_5'  :  {'name':'Arsnel','Points':40}
}
#===============================================
@app.get("/")

async def first_app():
    return Clubs

#=================================================
# @app.get('/table{club_id}')
# async def show_table(club_id:int):
#     return {"club ID":club_id}

#=======================================================
# Path Parameter :additional variables to an API call.
# @app.get('/{team_id}')

# async def get_club_by_id(club_id:str):
#     return Clubs[club_id]

#============================================================
#Query Parameter
# @app.get('/')
# async def show_top_table(skip_club:str):
#     new_table=Clubs.copy()
#     del new_table[skip_club]
#     return new_table

 #==================================================================
 #post metheod 
@app.post("/")
async def create_team(name:str, points:int):
    current_team_id = 0

    if len(Clubs) > 0:
        for team in Clubs:
            x = int(team.split('_')[-1])
            if x > current_team_id:
                current_team_id = x

    Clubs[f'team_{current_team_id + 1}'] = {'name': name, 'Points': points}
    return Clubs[f'team_{current_team_id + 1}']
#======================================================================
#Put requests :Update records
@app.put("/{team}")
async def update_team(team: str, name: str, points):
    team_information = {'name': name, 'Points': points}
    Clubs[team] = team_information
    return team_information

#========================================================================
#Delete request: Delete records
@app.delete("/{team}")
async def delete_team(team):
    del Clubs[team]
    return f'Club {team} deleted.'