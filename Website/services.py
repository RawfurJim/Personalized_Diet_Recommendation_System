import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def calculate_BMI(weight,height):
    height_in_M = height/100
    return weight/height_in_M**2

def calculate_BMR(weight,height,age,gender):
    BMI = 1
    if gender == 0 :
        BMI = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)
        return BMI
    elif gender == 1 :
        BMI = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
        return BMI
def needed_cal(activity,BMR):
    if activity == 0 :
        return BMR*1.2
    elif activity == 1:
        return BMR*1.375
    elif activity ==2:
        return BMR * 1.55
    elif activity == 3:
        return BMR * 1.725
    else:
        return BMR * 1.9
def calculate_calory_u(input):
    
    BMI = calculate_BMI(int(input['weight']),int(input['height']))

    BMR = calculate_BMR(int(input['weight']),int(input['height']),int(input['age']),int(input['sex']))

    daily_calory_needed = needed_cal(int(input['activity_lavel']), BMR)

    print("Your body mass index is: ", BMI)
    if ( BMI < 16):
        print("Acoording to your BMI, you are Severely Underweight")
        return {'daily_calory' : [daily_calory_needed+500, 100,406,10,96,11], 
                'message':"Acoording to your Data, you are Severely Underweight", "BMI":BMI, 'cal': daily_calory_needed+500}
    elif ( BMI >= 16 and BMI < 18.5):
        print("Acoording to your BMI, you are Underweight")
        return {'daily_calory' : [daily_calory_needed+300, 100,406,10,96,11], 
                'message':"Acoording to your Data, you are Underweight", "BMI":BMI, 'cal': daily_calory_needed+300}
    elif ( BMI >= 18.5 and BMI < 25):

        print("Acoording to your BMI, you are Healthy")

        return {'daily_calory' : [daily_calory_needed, 100,406,10,96,11], 
                'message':"Acoording to your Data, you are Healthy", "BMI":BMI, 'cal': daily_calory_needed}
    elif ( BMI >= 25 and BMI < 30):

        print("Acoording to your BMI, you are Overweight")
        return {'daily_calory' : [daily_calory_needed-300, 100,406,10,96,11], 
                'message':"Acoording to your Data, you are Overweight", "BMI":BMI, 'cal': daily_calory_needed-300}
    elif ( BMI >=30):
        print("Acoording to your BMI, you are Severely Overweight")
        return {'daily_calory' : [daily_calory_needed-500, 100,406,10,96,11], 
                'message':"Acoording to your Data, you are Severely Overweight", "BMI":BMI, 'cal': daily_calory_needed-500}
    ...

def get_nearest_neighbors(data, point, n_neighbors=4):
    # Select columns
    a = pd.concat([data.iloc[:, 5], data.iloc[:, 7:12]], axis=1)
    X = a.values
    
    # Initialize NearestNeighbors class with number of neighbors you want to find
    nn = NearestNeighbors(n_neighbors=4)
    
    # Fit the model to your data
    nn.fit(X)
    
    # Find the nearest neighbors to your point
    distances, indices = nn.kneighbors(point)
    
    return indices, distances

def recomanded_food(user_input):
    data = pd.read_csv(r'C:\Users\HP\Desktop\project_end_to_end\food_data_1.csv')
    breakfast_data = data[data['breakfast'] == 1]
    lunch_data = data[data['lunch'] == 1]
    dinner_data = data[data[' dinner'] == 1]
    user_value = user_input['daily_calory']
    point = np.array(user_value).reshape(1, -1)

    # Calculate proportion for each meal
    breakfast_proportion = 0.3
    lunch_proportion = 0.4
    dinner_proportion = 0.3

    # Define points for each meal type
    breakfast_point = (point * breakfast_proportion).reshape(1, -1)
    lunch_point = (point * lunch_proportion).reshape(1, -1)
    dinner_point = (point * dinner_proportion).reshape(1, -1)
    # Find nearest neighbors for each meal type
    breakfast_indices, breakfast_distances = get_nearest_neighbors(breakfast_data, point)
    lunch_indices, lunch_distances = get_nearest_neighbors(lunch_data, point)
    dinner_indices, dinner_distances = get_nearest_neighbors(dinner_data, point)

    all_indices = breakfast_indices[0]+lunch_indices[0]+dinner_indices[0]

    merged_list = []

    merged_list.extend(breakfast_indices[0])
    merged_list.extend(lunch_indices[0])
    merged_list.extend(dinner_indices[0])
    food = []

    for i in merged_list:
        list = [data.loc[i, 'food_name'],data.loc[i, 'image'],data.loc[i, 'food_calories'],data.loc[i,'food_healthlabel']]
        food.append(list)

    result = {'recomanded_food': food, 'message': user_input['message'], 'BMI':user_input['BMI'], 'cal': user_input['cal'] }
    return result

