def nutrient(weight, height, age, freqency, gender, target):
    if(gender == 'male'):
        BMR =  13.7 * weight + 5 * height - 6.8 * age + 66
    else:
        BMR = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    
    freqency_table = {
        'barely': 1.2,
        'seldom': 1.375,
        'medium': 1.55,
        'active': 1.725,
        'professional': 1.9
    }

    target_table = {
        'lose': -400,
        'keep': 0,
        'gain': +400
    }

    # 卡路里
    calorie = round(BMR * freqency_table.get(freqency) + target_table.get(target), 2)
    # 蛋白质
    protein = round(calorie * 0.15 / 4, 2)
    # 蛋白质
    fat = round(calorie * 25 / 9, 2)
    # 蛋白质
    carbohydrate = round(calorie * 0.6 / 4, 2)

    total = {}
    total['calorie'] = calorie
    total['protein'] = protein
    total['fat'] = fat
    total['carbohydrate'] = carbohydrate

    breakfast = {}
    breakfast['protein'] = protein * 0.3
    breakfast['fat'] = fat * 0.3
    breakfast['carbohydrate'] = carbohydrate * 0.3
    lunch = {}
    lunch['protein'] = protein * 0.4
    lunch['fat'] = fat * 0.4
    lunch['carbohydrate'] = carbohydrate * 0.4
    dinner = {}
    dinner['protein'] = protein * 0.3
    dinner['fat'] = fat * 0.3
    dinner['carbohydrate'] = carbohydrate * 0.3

    recommend = {}
    recommend['total'] = total
    recommend['breakfast'] = breakfast
    recommend['lunch'] = lunch
    recommend['dinner'] = dinner

    return recommend

print(nutrient(60,160,40,'seldom', 'female', 'keep'))