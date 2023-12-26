import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def find_recipe(request):
    if request.method == 'POST':
        added_products_str = request.POST.get('added-products', '')
        added_products = [product.strip() for product in added_products_str.split(',') if product]
        translated_to_en = translate(added_products, 'en')
        products = [i['text'] for i in translated_to_en["translations"]]
        response_data = request_api_spoonacular(products)

        result_data = []
        for data in response_data:
            image = data['image']
            all_ingredients = [i["originalName"] for i in data["missedIngredients"]] + [i["originalName"] for i in
                                                                                        data["usedIngredients"]]
            translated_ingredients = translate(all_ingredients, "ru")
            ingredients = [ing['text'].title() for ing in translated_ingredients["translations"]]
            result_data.append({
                "image": image,
                "ingredients": ingredients,
            })

        return render(request, 'base.html', context={'recipe': result_data})

    return render(request, 'base.html')


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
