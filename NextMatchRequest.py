import requests
from datetime import datetime
from zoneinfo import ZoneInfo  # Para detectar y manejar zonas horarias automáticamente

API_KEY = "6da21cf913144f4d8276712ebf975d2e"  # Reemplaza con tu API key de football-data
HEADERS = {
    "X-Auth-Token": API_KEY
}

def find_team_id(team_name):
    """Busca el ID del equipo por nombre en ligas populares."""
    leagues = ["PD", "PL", "SA", "BL1", "FL1"]  # PD=LaLiga, PL=Premier, SA=Serie A, etc.
    for league in leagues:
        url = f"https://api.football-data.org/v4/competitions/{league}/teams"
        response = requests.get(url, headers=HEADERS).json()
        for team in response.get("teams", []):
            if team_name.lower() in team["name"].lower():
                return team["id"]
    return None

def get_next_match(team_name):
    team_id = find_team_id(team_name)
    if not team_id:
        return f"No se encontró ningún equipo llamado '{team_name}'."

    url = f"https://api.football-data.org/v4/teams/{team_id}/matches"
    params = {"status": "SCHEDULED", "limit": 1}
    response = requests.get(url, headers=HEADERS, params=params).json()
    
    if not response.get("matches"):
        return f"No hay próximos partidos programados para '{team_name}'."

    match = response["matches"][0]
    home_team = match["homeTeam"]["name"]
    away_team = match["awayTeam"]["name"]

    # Convertir fecha UTC a hora local automáticamente
    utc_match_time = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
    utc_match_time = utc_match_time.replace(tzinfo=ZoneInfo("UTC"))
    local_match_time = utc_match_time.astimezone()  # Ajusta automáticamente a la hora local del dispositivo

    return f"Próximo partido: {home_team} vs {away_team} el {local_match_time.strftime('%d/%m/%Y %H:%M:%S %Z')}"

if __name__ == "__main__":
    team_name = input("Introduce el nombre del equipo: ").strip()
    print(get_next_match(team_name))

#API Key: 6da21cf913144f4d8276712ebf975d2e
