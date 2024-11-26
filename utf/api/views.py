from rest_framework.response import Response

from rest_framework.views import APIView

from food.models import FoodCategory, FoodSerializer


class FoodAPIView(APIView):

    def get(self, request):
        data = []
        for category in FoodCategory.objects.filter(
            food__is_publish=True
        ):
            food_data = []
            for food in category.food.all():
                if food.is_publish is True:
                    food_data.append(food)
            serializer = FoodSerializer(food_data, many=True)
            data.append(
                {
                    "id": category.id,
                    "name_ru": category.name_ru,
                    "name_en": category.name_en,
                    "name_ch": category.name_ch,
                    "order_id": category.order_id,
                    "foods": serializer.data
                }
            )
        return Response(data)
