queries = {
    'housing' : 'select * from HOUSING_DATA.freddie_mae_house_price_index;',
    'military' : 'select SUM("Total Cost"), "State", EXTRACT (YEAR FROM "Ship Date") from CRIME_DATA.policy_military_purchases group by EXTRACT (YEAR FROM "Ship Date") , "State";',
    'deathCountry' : 'select "Country Code", avg("Death Rate Per 100,000") from HEALTH.death_rates_by_country where "Year" = 2010 and "Age Group" = \'All ages\' group by "Country Code";',
    'crime' : '',
    'deathWeather' : '',                                                                                                                                                                                                                         'deathAccident' : ''
}


