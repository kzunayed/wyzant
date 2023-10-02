# rapha_name = 'Rapha A.'
# print(rapha_name)
# print(type(rapha_name))

# rapha_age = 21
# print(type(rapha_age))

# rapha_weight = 167.0
# print(type(rapha_weight))

lenght = '1.0 3.5 4.7'
# lenght_transformed = [1.0, 3.5, 4.7]
lenght_transformed = lenght.split()
print(lenght_transformed)
lenght_float = []
for each_lenght in lenght_transformed:
    lenght_float.append(float(each_lenght))

print(lenght_float)
# float is a number with a decimal point