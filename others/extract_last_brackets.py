import re
from pandas import DataFrame

data= [{'id': '81643', 'name': 'Abdallah Guezour (Schroders)', 'additional': {}}, {'id': '123653', 'name': 'Abdallah Nauphal (TD)', 'additional': {}}, {'id': '213243', 'name': 'Adam Rizkalla (River Canyon)', 'additional': {}}, {'id': '153647', 'name': 'Adrian Allardice (Old Mutual)', 'additional': {}}, {'id': '182699', 'name': 'Adrian van Pallander (Coronation) dfdfsdf)', 'additional': {}}, {'id': '106039', 'name': 'Aindrais D.P. OCallaghan (JPMorgan)', 'additional': {}}, {'id': '138501', 'name': 'Alejandro Pla Malla (Novo Banco Group)', 'additional': {}}, {'id': '138134', 'name': 'Alfredo Serratosa Gallardo (Bestinver)', 'additional': {}}, {'id': '165227', 'name': 'Alla Kolganova (Vanguard)', 'additional': {}}, {'id': '122569', 'name': 'Allan Brown (AIC)', 'additional': {}}, {'id': '210134', 'name': 'Allan C. Nichols (Clifford Capital)', 'additional': {}}, {'id': '79265', 'name': 'Allan Christensen (C WorldWide)', 'additional': {}}, {'id': '6765', 'name': 'Allan Conway (Sun Life)', 'additional': {}},]

def _separate_name_and_firm(portfolio_manager):
    manager_name = portfolio_manager['name']
    print(manager_name)
    if manager_name.count("(") < 1:
        portfolio_manager['firm'] = None
    else:
        portfolio_manager['firm'] = re.findall("\((.+?)\)", manager_name)[0]
        print(portfolio_manager['firm'] )
        portfolio_manager['name'] = manager_name.replace('(' + portfolio_manager['firm'] + ')', '').strip()
        
    print("\nportfolio_manager\n",portfolio_manager)
    return portfolio_manager


result = DataFrame(data)
# print(result)
# Extract the columns that I want in my new DataFrame
portfolio_managers = result[["id", "name"]]
# print(portfolio_managers)
portfolio_managers = portfolio_managers.apply(_separate_name_and_firm, axis=1)
print(portfolio_managers)

# print(data)