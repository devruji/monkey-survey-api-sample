from collections import defaultdict
import os

ENV = 'dev'

class Config:
    def __init__(self):
        ###############
        # Monkey API
        ###############
        self.cli_id = '22_Wo-xSS0qou6mVivnqJA'
        self.secret ='48983254926320982001350257165045547463'
        self.access_token = 'wvZoQR8UXo.EP3C.yOVBTbiQXibJ0ZoycwNEqF8XiBrdggybvdO085x9xkEZie.F5.a9eiTC8xg1sq8.l7xFQIw.PmhSdIxKQbTZnzqHn7Rd962vhxbmHUoLjQPZ.EAI'
        self.uri = 'https://www.surveymonkey.com/r/N3TCWXY'
        self.oauth_monkey = 'https://www.surveymonkey.com'
        self.wdc_survey_id = '299446673'
        self.page1_mapping_id = {}
        self.page1_mapping_answer = {}
        self.page1_result_parser = defaultdict(list)

class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        pass

class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        pass

configBy = {
    'dev': DevelopmentConfig(),
    'prod': ProductionConfig()
}


if __name__ == '__main__':
    appConfig = configBy[ENV]

    print(appConfig)