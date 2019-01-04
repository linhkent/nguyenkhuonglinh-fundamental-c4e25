salary = [
    {
        'name': 'Huy',
        'sph': 25,
        'h': 30
    },
    {
        'name': 'Quan',
        'sph': 25,
        'h': 20 
    },
    {
        'name': 'Duc',
        'sph': 30,
        'h': 40    
    }
]
total = 0
for p in salary:
    p['sal'] = p['sph']*p['h']
    total += p['sal']
    print('Salary of ',p['name'],': ',p['sal'],sep='')
print('Total of salary: ', total)