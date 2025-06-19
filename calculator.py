# Author: Boutemedjet Youcef
# Date: 19 June 2025


print("Welcome to the macroeconomics calculator")

# --------- FUNCTIONS ---------

def calculate_gdp(consumption, investment, government_spending, net_exports):
    """
    calculate GDP using the expenditure approach
    """
    return consumption + investment + government_spending + net_exports

def calculate_inflation_rate(current_price, previous_price):
    """
    calculate inflation rate using the formula:
    ((current price - previous price) / previous price) * 100
    """
    return ((current_price - previous_price) / previous_price) * 100

def calculate_unemployment_rate(number_of_unemployed, labor_force):
    """
    calculate unemployment rate using the formula:
    (unemployed / labor force) * 100
    """
    return (number_of_unemployed / labor_force) * 100

def calculate_interest_rate(nominal_interest_rate, inflation_rate):
    """
    calculate real interest rate using the formula:
    real interest rate = nominal interest rate - inflation rate
    """
    return nominal_interest_rate - inflation_rate

def calculate_money_supply(money_base, reserve_ratio):
    """
    calculate money supply using the formula:
    money supply = money base / reserve ratio
    """
    return money_base / reserve_ratio

def calculate_exchange_rate(foreign_currency, domestic_currency):
    """
    calculate exchange rate using the formula:
    exchange rate = foreign currency / domestic currency
    """
    return foreign_currency / domestic_currency

def calculate_balance_of_payments(exports, imports):
    """
    calculate balance of payments using the formula:
    balance of payments = exports - imports
    """
    return exports - imports

def calculate_fiscal_deficit(government_revenue, government_expenditure):
    """
    calculate fiscal deficit using the formula:
    fiscal deficit = government expenditure - government revenue
    """
    return government_expenditure - government_revenue

def calculate_public_debt(current_debt, new_borrowing):
    """
    calculate public debt using the formula:
    public debt = current debt + new borrowing
    """
    return current_debt + new_borrowing

def calculate_trade_balance(exports, imports):
    """
    calculate trade balance using the formula:
    trade balance = exports - imports
    """
    return exports - imports

def calculate_current_account_balance(exports, imports, net_investment_income, net_transfers):
    """
    calculate current account balance using the formula:
    (exports - imports) + net investment income + net transfers
    """
    return (exports - imports) + net_investment_income + net_transfers

def calculate_economic_growth_rate(current_gdp, previous_gdp):
    """
    calculate economic growth rate using the formula:
    ((current GDP - previous GDP) / previous GDP) * 100
    """
    return ((current_gdp - previous_gdp) / previous_gdp) * 100

def calculate_real_gdp(nominal_gdp, gdp_deflator):
    """
    calculate real GDP using the formula:
    real GDP = nominal GDP / (gdp deflator / 100)
    """
    return nominal_gdp / (gdp_deflator / 100)

def calculate_gdp_per_capita(gdp, population):
    """
    calculate GDP per capita using the formula:
    GDP per capita = GDP / population
    """
    return gdp / population if population > 0 else 0

def calculate_fdi_inflow(foreign_direct_investment, domestic_investment):
    """
    calculate FDI inflow using the formula:
    FDI inflow = foreign direct investment - domestic investment
    """
    return foreign_direct_investment - domestic_investment

def calculate_fdi_outflow(domestic_direct_investment, foreign_investment):
    """
    calculate FDI outflow using the formula:
    FDI outflow = domestic direct investment - foreign investment
    """
    return domestic_direct_investment - foreign_investment

def calculate_capital_account_balance(capital_inflows, capital_outflows):
    """
    calculate capital account balance using the formula:
    capital account balance = capital inflows - capital outflows
    """
    return capital_inflows - capital_outflows

def calculate_current_account_deficit(exports, imports, net_investment_income, net_transfers):
    """
    calculate current account deficit using the formula:
    (imports - exports) + net investment income + net transfers
    """
    return (imports - exports) + net_investment_income + net_transfers

def calculate_investment_rate(gross_fixed_capital_formation, gdp):
    """
    calculate investment rate using the formula:
    (gross fixed capital formation / GDP) * 100
    """
    return (gross_fixed_capital_formation / gdp) * 100 if gdp > 0 else 0

def calculate_public_investment_ratio(public_investment, total_investment):
    """
    calculate public investment ratio using the formula:
    (public investment / total investment) * 100
    """
    return (public_investment / total_investment) * 100 if total_investment > 0 else 0

def calculate_private_investment_ratio(private_investment, total_investment):
    """
    calculate private investment ratio using the formula:
    (private investment / total investment) * 100
    """
    return (private_investment / total_investment) * 100 if total_investment > 0 else 0

def calculate_investment_to_gdp_ratio(investment, gdp):
    """
    calculate investment to GDP ratio using the formula:
    (investment / GDP) * 100
    """
    return (investment / gdp) * 100 if gdp > 0 else 0

# --------- USER INTERFACE ---------

print("\nChoose an option:")
print("1. Calculate GDP")
print("2. Calculate Inflation Rate")
print("3. Calculate Unemployment Rate")

choice = input("Enter the number of your choice: ")

if choice == "1":
    c = float(input("Enter consumption: "))
    i = float(input("Enter investment: "))
    g = float(input("Enter government spending: "))
    nx = float(input("Enter net exports: "))
    result = calculate_gdp(c, i, g, nx)
    print("GDP is: {:.2f}".format(result))

elif choice == "2":
    current_price = float(input("Enter current price: "))
    previous_price = float(input("Enter previous price: "))
    result = calculate_inflation_rate(current_price, previous_price)
    print("Inflation Rate is: {:.2f}%".format(result))

elif choice == "3":
    unemployed = float(input("Enter number of unemployed: "))
    labor_force = float(input("Enter total labor force: "))
    result = calculate_unemployment_rate(unemployed, labor_force)
    print("Unemployment Rate is: {:.2f}%".format(result))

else:
    print("Invalid choice. Please try again.")
