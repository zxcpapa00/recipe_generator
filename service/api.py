import requests
from django.conf import settings
from django.http import JsonResponse


def request_api_spoonacular(products):
    api_url = 'https://api.spoonacular.com/recipes/findByIngredients'
    api_key = settings.SPOONACULAR_KEY

    params = {
        'ingredients': ','.join(products),
        'apiKey': api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        response_data = response.json()
        return response_data

    except requests.RequestException as e:
        return JsonResponse({'error': str(e)})


def translate(texts, lang):
    iam_token = settings.YANDEX_IAM_TOKEN
    folder_id = settings.YANDEX_FOLDER_ID
    target_language = lang

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(iam_token)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )

    return response.json()
