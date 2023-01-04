# current league api key = RGAPI-02d2d5c0-a266-4197-8be0-d19b9a9be2d4
import time
import requests

class summonerWR:
    wins_total = 0
    loses_total = 0
    total_games = 0
    main_summoner = "THS Haru"
    duo_summoner = "La3ii"
    season = "Preseason 13"
    patches = 0

    if season == "Preseason 13":
        patches = [12.1, 12.2, 12.3, 12.4, 12., 12.6, 12.7, 12.8, 12.9, 12.10, 12.11, 12.12, 12.13, 12.14, 12.15, 12.6, 12.17, 12.18, 12.19, 12.20, 12.21]

    main_summoner = input("What's your summoner name: ")
    duo_summoner = input("What's your duo summoner name: ")

    response = requests.get(
        url=f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{main_summoner}?api_key=RGAPI-02d2d5c0-a266-4197-8be0-d19b9a9be2d4")
    summoner_details = response.json()
    summoner_puuid = summoner_details["puuid"]


    matches = []
    seconds = 1
    seconds2 = 78 * 0.5

    match_page = 0

    counter = 0
    def GetWR(self):
        self.matches.clear()
        response = requests.get(
            url=f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.summoner_puuid}/ids?start={self.match_page}&count=100&api_key=RGAPI-02d2d5c0-a266-4197-8be0-d19b9a9be2d4")
        self.matches = response.json()
        print(f"page = {self.match_page}")
        if not self.matches:
            return
        else:
            for match in self.matches:
                print("time elapsed: " + self.seconds.__str__() + " seconds")
                self.seconds = self.seconds + 1
                print(match)
                response = requests.get(
                    url=f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key=RGAPI-02d2d5c0-a266-4197-8be0-d19b9a9be2d4")
                if not self.matches:
                    return
                elif response.status_code == 200:
                    self.GetMatchData(response)
                else:
                    print("sleeping for 121 seconds")
                    for i in range(121):
                        print((121 - i).__str__() + " seconds remaining")
                        time.sleep(1)
                    # self.GetMatchData(response)


    def GetMatchData(self, response):
        match_data = response.json()
        time.sleep(1)
        game_version = match_data["info"]["gameVersion"]
        print(game_version)
        test = game_version.split('.')[0] + "."+game_version.split('.')[1]
        print(test)
        self.counter = self.counter + 1
        print("counter: " + self.counter.__str__())
        if not (test.__str__() == "12.22" or test.__str__() == "12.23"):
            print("e")
            if match_data["info"]["queueId"] == 420:
                for summoner in match_data["info"]["participants"]:
                    # print(summoner["summonerName"])
                    # print(summoner["win"])
                    if summoner["summonerName"] == self.duo_summoner:
                        if summoner["win"]:
                            self.wins_total = self.wins_total + 1
                            # print("won")
                        else:
                            self.loses_total = self.loses_total + 1
                            # print("lost")
        if test.__str__() == "11.24":
            print("finished with preseason games")
            self.matches = []
            return
        if self.counter == 100:
            self.counter = 0
            self.match_page = self.match_page + 100
            print(f"changing page to {self.match_page}")
            # response = requests.get(
            #     url=f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.summoner_puuid}/ids?start={self.match_page}&count=100&api_key=RGAPI-02d2d5c0-a266-4197-8be0-d19b9a9be2d4")
            # self.matches = response.json()
            self.GetWR()


    def PrintResult(self):
        self.total_games = self.wins_total + self.loses_total
        print(f"you have played a total of {self.total_games} with {self.duo_summoner}")
        print(f"you won {self.wins_total} and lost {self.loses_total}")
        if self.total_games > 0:
            print(f"your win ratio with summoner {self.duo_summoner} is: " + (
                    (self.wins_total / (self.wins_total + self.loses_total)) * 100).__str__())

# print(match_data["info"]["participants"])

obj = summonerWR()
obj.GetWR()
obj.PrintResult()
