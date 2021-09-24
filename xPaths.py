BUY_PATHS = {
    'buy': r"//li[@id='buyNowBtn']",
    'confirm': r"//div[@class='btnArea']/a[@class='enter']",
    'checkout': r"//a[@id='checkShoppingCart']",
    'creditCardInstallment': r"//input[@id='paymentCardSplit']/parent::*",
    'installmentLast': r"//tbody[@id='paymentBody']/tr[last()]/td/input[@name='selAllot']",
    'CCV': r"//input[@id='cardCVV']",
    'confirmCheckout': r"//article[@class='checkoutArea']/a"
}

LOGIN_X_PATHS = {
    'account': r"//input[@id='memId']",
    'password': r"//input[@id='passwd']",
    'loginBtn': r"//dd[@class='loginBtn']/a[@class='login']"
}
