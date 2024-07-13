
from abc import ABC, abstractmethod

class RulesParser(ABC):
    """
    Abstract base class for parsing rules. This class provides a common interface for all rule parsers.
    """
    cols = None
    def __init__(self, dict_data) -> None:
        """
        Initialize the RulesParser with dictionary data.

        :param dict_data: The dictionary data to be parsed
        """
        self.dict_data = dict_data

    @classmethod
    def get_course(cls):
        """
        Get the columns associated with the rule parser class.

        :return: The columns associated with the class
        """
        return cls.cols
    
    @abstractmethod
    def parse_data(self):
        """
        Abstract method to parse data. Must be implemented by subclasses.
        Define the unique logic of different parsing rules here.
        """
        pass

class RuleEPLSeasonPerformance(RulesParser):
    """
    Concrete class for parsing English Premier League (EPL) season performance data.
    """
    cols = ['league', 'season','gameid','utcDate','home_team','away_team','winner',
            'full_time_home_score','full_time_away_score','half_time_home_score','half_time_away_score' ]
    def __init__(self,dict_data):
        """
        Initialize the RuleEPLSeasonPerformance with dictionary data.

        :param dict_data: The dictionary data to be parsed
        """
        super().__init__(dict_data=dict_data)
        self.league = self.dict_data.get('competition').get('name')
        self.season = self.dict_data.get('filters').get('season')

    def parse_data(self):
        """
        Parse the match data and extract relevant information.

        :return: A list of dictionaries containing parsed match data
        """
        tmp  = []
        for data in self.dict_data['matches']:
            if data.get("score").get("winner").upper() == "AWAY_TEAM":
                winner = data.get("awayTeam").get("name")
            elif data.get("score").get("winner").upper() == "HOME_TEAM":
                winner = data.get("homeTeam").get("name")
            elif data.get("score").get("winner").upper() == "DRAW":
                winner = "DRAW"
            else:
                winner = "ERROR"
            tmp.append(
                {
                    "league"    : self.league,
                    "season"    : self.season,
                    "gameid"    : data.get("id"),
                    "utcDate"   : data.get("utcDate"),
                    "home_team" : data.get("homeTeam").get("name"),
                    "away_team" : data.get("awayTeam").get("name"),
                    "winner"    : winner ,
                    "full_time_home_score"    : data.get("score").get("fullTime").get("home"),
                    "full_time_away_score"    : data.get("score").get("fullTime").get("away"),
                    "half_time_home_score"    : data.get("score").get("halfTime").get("home"),
                    "half_time_away_score"    : data.get("score").get("halfTime").get("away"),       
                }
            )
        return tmp
    

def get_target_parser(rule):
    """
    Get the appropriate parser class based on the rule provided.

    :param rule: The rule specifying which parser to use
    :return: The corresponding parser class
    """
    match rule:
        case "EPL_Season" : 
            return RuleEPLSeasonPerformance
        case _:
            pass

