from service.api import translate, request_api_spoonacular
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from accounts.views import set_story


class IndexView(TemplateView):
    template_name = 'base.html'


class FindRecipeView(CreateView):
    template_name = 'base.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            added_products_str = request.POST.get('added-products', '')
            added_products = [product.strip() for product in added_products_str.split(',') if product]
            translated_to_en = translate(added_products, 'en')
            products = [i['text'] for i in translated_to_en["translations"]]
            response_data = request_api_spoonacular(products)

            result_data = []
            for data in response_data:
                title = translate(data['title'], 'ru')
                image = data['image']
                all_ingredients = [i["originalName"] for i in data["missedIngredients"]] + [i["originalName"] for i in
                                                                                            data["usedIngredients"]]
                translated_ingredients = translate(all_ingredients, "ru")
                ingredients = [ing['text'].title() for ing in translated_ingredients["translations"]]
                result_data.append({
                    "title": title['translations'][0]['text'],
                    "image": image,
                    "ingredients": ingredients,
                })
            set_story(user=request.user, products=added_products, response_prod=result_data)

            return render(request, 'base.html', context={'recipe': result_data})

        return render(request, 'base.html')


class StoryListView(ListView):
    template_name = "story.html"
