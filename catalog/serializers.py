from rest_framework import serializers
from catalog.models import Logo, Car, InstallmentPlan, Sub


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'link', 'order',
                  'created_at', 'updated_at',)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'price', 'year', 'km', 'color_uz',
                  'color_ru', 'image', 'automatic', 'mechanic', 'discount', 'order', 'logo', 'created_at',
                  'updated_at',)


class SubSerializer(serializers.ModelSerializer):
    installmentplan_title = serializers.SerializerMethodField()

    class Meta:
        model = Sub
        fields = ('duration', 'prepayment_percentage', 'annual_interest_rate', 'installmentplan_title',)

    def get_installmentplan_title(self, obj):
        return obj.installmentplan.car.title if obj.installmentplan and obj.installmentplan.car else "No Car"


class InstallmentPlanSerializer(serializers.ModelSerializer):
    car_title = serializers.SerializerMethodField()
    subs = SubSerializer(many=True, read_only=True)

    class Meta:
        model = InstallmentPlan
        fields = ('id', 'car_title', 'car', 'subs')

    def get_car_title(self, obj):
        return obj.car.title if obj.car else "No Car"
