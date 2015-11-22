queries = {
    'housing' : 'select * from HOUSING_DATA.freddie_mae_house_price_index;',
    'military' : 'select SUM("Total Cost"), "State", EXTRACT (YEAR FROM "Ship Date") from CRIME_DATA.policy_military_purchases group by EXTRACT (YEAR FROM "Ship Date") , "State";',
    'death' : '',
    'crime' : '',
    'deathWeather' : '',
    'deathAccident' : ''
}