def highest_revenue_item(data):
    count_dict = {}
    price_dict = {}

    row_data = data.split(' ')
    for row in row_data:
        txn = row.split(',')
        product_id = txn[1]
        price = txn[2]

        if product_id in count_dict:
            count_dict[product_id] += 1
        else:
            count_dict[product_id] = 0
            price_dict[product_id] = price

    most_common_item = '0'
    most_revenue = '0'

    for product in count_dict:
        product_revenue = price_dict[product] * count_dict[product]
        if product_revenue > most_revenue:
            most_revenue = product_revenue
            most_common_item = product

    if most_revenue != 5:
        return most_common_item