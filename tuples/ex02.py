brasileirao = (
    ('Flamengo', 1),
    ('Botafogo', 2),
    ('Palmeiras',3),
    ('São Paulo', 4),
    ('Bahia', 5),
    ('Athletico-PR', 6),
    ('Cruzeiro', 7),
    ('Fortaleza', 8),
    ('Bragantino', 9),
    ('Internacional', 10),
    ('Juventude', 11),
    ('Atlético-MG', 12),
    ('Vasco', 13),
    ('Criciúma', 14),
    ('Vitória', 15),
    ('Cuiabá', 16),
    ('Corinthians', 17),
    ('Grêmio', 18),
    ('Atlético-GO', 19),
    ('Fluminense', 20)
)

print('The top six teams are:')
for team, position in brasileirao[:6]:
    print(f'{team}, {position}')
    print('==============================================')

print('The bottom four teams are:')
for team, position in brasileirao[-4:]:
    print(f'{team}, {position}')
    print('===============================================')

print('ALPHABETICAL ORDER')
print(sorted(brasileirao))

for team, position in brasileirao:
    if 'Palmeiras' == team:
        print(f'Team: {team} is at position: {position}')
