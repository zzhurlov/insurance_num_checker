from rest_framework import serializers
from string import punctuation


class InsuranceNumberSerializer(serializers.Serializer):
    number = serializers.CharField()

    def validate_number(self, value: str):
        """
        Проверяем корректность номера СНИЛС

        Возможные маски ввода:
        1) XXXXXXXXXYY
        2) XXX-XXX-XXX YY
        """
        value = value.strip()
        # проверяем длину
        if len(value) != 14 and len(value) != 11:
            raise serializers.ValidationError(
                "длина СНИЛС должна составлять 14 символов"
            )

        # проверяем наличие букв и спец символов в значении
        fixed_punctuation = punctuation.replace("-", "")
        for char in value:
            if char.isalpha():
                raise serializers.ValidationError("СНИЛС не должен иметь букв")
            elif char in fixed_punctuation:
                raise serializers.ValidationError("СНИЛС не должен иметь спец символов")

        check_sum_in = value[-2:]

        if "-" in value:
            splitted_value = value.split("-")

            if (
                len(splitted_value) != 3
                and len(splitted_value[0]) != 3
                and len(splitted_value[1]) != 3
                and len(splitted_value[2]) != 5
            ):
                raise serializers.ValidationError("Некорректный СНИЛС")

            value = value[:-3].replace("-", "")
        else:
            value = value[:-2].strip()

        indexes = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        check_sum_out = 0
        for i in range(len(value)):
            check_sum_out = check_sum_out + int(value[i]) * indexes[i]

        if check_sum_out < 100 and str(check_sum_out) == check_sum_in:
            return value + check_sum_in

        elif (check_sum_out == 100 or check_sum_out == 101) and check_sum_in == "00":
            return value + check_sum_in

        elif check_sum_out > 101 and f"{check_sum_out % 101:02d}" == check_sum_in:
            return value + check_sum_in

        else:
            raise serializers.ValidationError("Некорректный номер СНИЛС")
