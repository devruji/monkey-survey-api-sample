from app_config import configBy, ENV
from surveymonkey.client import Client

import pandas as pd

# [Initialize the configuration]
appConfig = configBy[ENV]

client = Client(
                client_id=appConfig.cli_id, 
                client_secret=appConfig.secret, 
                redirect_uri=appConfig.oauth_monkey, 
                access_token=appConfig.access_token
            )

if __name__ == '__main__':
    # survey list
    # print(client.get_survey_lists())

    # specific survey view
    # print(client.get_specific_survey(appConfig.wdc_survey_id))

    # specific survey response
    # print(client.get_survey_response(appConfig.wdc_survey_id))

    # specific survey response bulk
    # print(client.get_survey_response_bulk(appConfig.wdc_survey_id)['data'])

    # TODO: [Task here]
    # ? API - specific survey translations & get mapping id of question
    for p in client.get_survey_details(appConfig.wdc_survey_id)['pages'][0]['questions']:
        if p['position'] >= 2:
            appConfig.page1_mapping_id[p['id']] = p['headings'][0]['heading'].lstrip()

    # ? API mapping id of each answer choices
    for p in client.get_survey_details(appConfig.wdc_survey_id)['pages'][0]['questions']:
        if p.get('answers', None) is not None:
            for a in p['answers']['choices']:
                # print(f"[QuestionId] : {p['id']} - [QuestionTranslation] : {appConfig.page1_mapping_id[p['id']]} | [AnswerId] : {a['id']} - [AnswerTranslation] : {a['text']}")
                appConfig.page1_mapping_answer[a['id']] = a['text']

    # ? API to get the answer of question from user
    for p in client.get_survey_response_bulk(appConfig.wdc_survey_id)['data']:
        for q in p['pages'][0]['questions']:
            if 'text' in q['answers'][0].keys():
                # print(f"{appConfig.page1_mapping_id[q['id']]} {q['answers'][0]['text']}")
                appConfig.page1_result_parser[appConfig.page1_mapping_id[q['id']]].append(q['answers'][0]['text'])

            else:
                # print(f"{appConfig.page1_mapping_id[q['id']]}: {appConfig.page1_mapping_answer[q['answers'][0]['choice_id']]}")
                appConfig.page1_result_parser[appConfig.page1_mapping_id[q['id']]].append(appConfig.page1_mapping_answer[q['answers'][0]['choice_id']])

    df = pd.DataFrame(appConfig.page1_result_parser)
    
    # ? export CSV here
    # df.to_csv('bossruji-one-click.csv', index=False)
    
    print(df)
