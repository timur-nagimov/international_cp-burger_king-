import pandas as pd

def aggregate_features_with_groupby(data):
    grouped_data = data.groupby('customer_id')

    aggregated_data = grouped_data.agg({
        'item_category': [(lambda x: x.mode().count()), # Количество раз, которое самая часто встречающаяся категория встречается
                          (lambda x: x.value_counts().max() / len(x))], # Доля заказов по каждой категории
        'ownareaall_sqm': 'mean',  # Средняя площадь зоны обслуживания
        'dish_name': 'nunique',  # Количество уникальных блюд
        'startdatetime': lambda x: (pd.to_datetime(x.max()) - pd.to_datetime(x.min())).days,  # Длительность активности  
    }).reset_index()

    # Переименование столбцов
    aggregated_data.columns = ['customer_id', 'most_common_category_count', 'item_category_ratio',
                               'avg_area', 'unique_dishes_count', 'activity_duration']

    return aggregated_data

aggregated_features_all = aggregate_features_with_groupby(df)
print(aggregated_features_all)
