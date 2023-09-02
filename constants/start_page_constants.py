class StartPageConstants:
    URL = "http://www.stage-slotozilla.com/"
    # header elements:
    LOGO_HEADER_XPATH = ".//span[@id='header-site-logo']"
    SEARCH_BUTTON_XPATH = "//*[@id='header-search-hide']"
    SEARCH_INPUT_XPATH = ".//input[@class='header-search-input']"
    SEARCH_SUBMIT_XPATH = ".//input[@id='search-submit']"
    MENU_FREE_SLOTS_XPATH = ".//li[@id='menu-item-83476']"
    MENU_ONLINE_CASINOS_XPATH = ".//li[@id='menu-item-83488']"
    MENU_BONUSES_XPATH = ".//li[@id='menu-item-83496']"
    MENU_CASINO_GAMES_XPATH = ".//li[@id='menu-item-93234']"
    # elements of the body
    BUTTON_GET_BONUS_XPATH = ".//div[@data-pid='vulkan-vegas-wb-en']"
    BUTTON_ALL_BONUSES_XPATH = ".//span[@class='btn-load-more button-load-more']"
    # footers elements:
    LOGO_FOOTER_XPATH = ".//span[@class='flex flex-align-center flex-justify-center']"
    ICON_TWITTER_XPATH = ".//a[@class='social-icon-md social-icon social-icon__twitter']"
    ICON_YOUTOBE_XPATH = ".//a[@class='social-icon-md social-icon social-icon__youtube']"
    ICON_FACEBOOK_XPATH = ".//a[@class='social-icon-md social-icon social-icon__facebook']"
    ICON_PRINTEREST_XPATH = ".//a[@class='social-icon-md social-icon social-icon__pinterest']"
    MENU_Bally_XPATH = ".//li[@id='menu-item-96440']"
    # форма підписки - динозавр
    SUBSCRIPTION_FORM_XPATH = "//div[@class='form-container subscription subscription-fade-in subscription-fade-out']"
    FORM_INPUT_XPATH = "//input[@id='user_email']"
    BUTTON_SUBSCRIBE_XPATH = "//button[class='btn btn-primary btn-submit-form']"  # не знаходить її :(
