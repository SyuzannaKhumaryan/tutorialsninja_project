import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Main Menu Tests')
@allure.title('Verify Clickable Menu Items')
@allure.description('This test verifies that all main menu items are clickable and lead to the correct pages.')
@allure.severity('Critical')
def test_menu_item(driver):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")
    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs","Cameras", "MP3 Players"]

    with allure.step(f"Click on menu item: {expected_menu_items[0]}"):

        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Click on menu item: {expected_menu_items[1]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item1.click()

    with allure.step(f"Click on menu item: {expected_menu_items[2]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item1.click()

    with allure.step(f"Click on menu item: {expected_menu_items[3]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item1.click()
    with allure.step(f"Verify the heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f"Click on menu item: {expected_menu_items[4]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item1.click()
    with allure.step(f"Verify the heading for {expected_menu_items[4]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step(f"Click on menu item: {expected_menu_items[5]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item1.click()
    with allure.step(f"Verify the heading for {expected_menu_items[5]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Click on menu item: {expected_menu_items[6]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item1.click()
    with allure.step(f"Verify the heading for {expected_menu_items[6]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f"Click on menu item: {expected_menu_items[7]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item1.click()

@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )

])


@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Nested Menu Tests')
@allure.title('Verify Clickable Nested Menu Items')
@allure.description('This test verifies that nested menu items are clickable and lead to the correct pages.')
@allure.severity('Normal')
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")
    with allure.step(f"Hover over the menu item and click the submenu item"):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()
    with allure.step(f"Verify the page title is: {result_text}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Search Tests')
@allure.title('Verify Product Search')
@allure.description('This test verifies that the search functionality returns correct products.')
@allure.severity('Normal')
def test_search_product(driver):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")
    with allure.step("Search for 'MacBook'"):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step("Verify that all displayed products contain 'MacBook'"):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
        assert len(products) == len(new_list)


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Cart Tests')
@allure.title('Verify Add to Cart Functionality')
@allure.description('This test verifies that products can be added to the cart successfully.')
@allure.severity('Critical')
def test_add_to_cart(driver):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Click on 'Add to Cart' for a product"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Wait for and verify the success message"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text

    with allure.step("Verify that the cart contains the added item"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[2]/a'))
        )
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got nothing"

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Wishlist Tests')
@allure.title('Verify Add to Wishlist Functionality')
@allure.description('This test verifies that products can be added to the wishlist successfully.')
@allure.severity('Normal')
def test_add_to_wishlist(driver, login):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")
    # Add a product to the wishlist
    with allure.step("Click on 'Add to Wishlist' for a product"):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    # Wait for the success message
    with allure.step("Wait for and verify the success message"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Wishlist add failed"

    # Navigate to the wishlist page
    with allure.step("Navigate to the wishlist page"):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    # Wait for the wishlist page to load and check for the product
    with allure.step("Verify that 'MacBook' is in the wishlist"):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[2]/td[2]/a'))
        )
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Footer Tests')
@allure.title('Verify Footer Links')
@allure.description('This test verifies that all footer links work correctly.')
@allure.severity('Normal')
def test_footer(driver):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")

    # Test 'About Us'
    with allure.step("Click on 'About Us'"):
        about_us = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a')
        about_us.click()
    with allure.step("Verify header for 'About Us'"):
        header_about_us = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_about_us == 'About Us', f"Expected 'About Us', but got '{header_about_us}'"

    # Test 'Delivery Information'
    with allure.step("Click on 'Delivery Information'"):
        delivery_information = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[2]/a')
        delivery_information.click()
    with allure.step("Verify header for 'Delivery Information'"):
        header_delivery = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_delivery == 'Delivery Information', f"Expected 'Delivery Information', but got '{header_delivery}'"

    # Test 'Contact Us'
    with allure.step("Click on 'Contact Us'"):
        contact_us = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a')
        contact_us.click()
    with allure.step("Verify header for 'Contact Us'"):
        header_contact_us = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_contact_us == 'Contact Us', f"Expected 'Contact Us', but got '{header_contact_us}'"

    # Test 'Returns'
    with allure.step("Click on 'Returns'"):
        returns = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a')
        returns.click()
    with allure.step("Verify header for 'Returns'"):
        header_returns = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_returns == "Product Returns", f"Expected 'Product Returns', but got '{header_returns}'"

    # Test 'Brands'
    with allure.step("Click on 'Brands'"):
        brands = driver.find_element(By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a")
        brands.click()
    with allure.step("Verify header for 'Brands'"):
        header_brands = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_brands == "Find Your Favorite Brand", f"Expected 'Find Your Favorite Brand', but got '{header_brands}'"

    # Test 'Gift Certificates'
    with allure.step("Click on 'Gift Certificates'"):
        gift_certificate = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a')
        gift_certificate.click()
    with allure.step("Verify header for 'Gift Certificates'"):
        header_gift_certificate = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_gift_certificate == "Purchase a Gift Certificate", f"Expected 'Purchase a Gift Certificate', but got '{header_gift_certificate}'"

    # Test 'Privacy Policy'
    with allure.step("Click on 'Privacy Policy'"):
        privacy_policy = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[3]/a')
        privacy_policy.click()
    with allure.step("Verify header for 'Privacy Policy'"):
        header_privacy = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_privacy == 'Privacy Policy', f"Expected 'Privacy Policy', but got '{header_privacy}'"

    # Test 'Terms & Conditions'
    with allure.step("Click on 'Terms & Conditions'"):
        terms_conditions = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[4]/a')
        terms_conditions.click()
    with allure.step("Verify header for 'Terms & Conditions'"):
        header_terms = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_terms == 'Terms & Conditions', f"Expected 'Terms & Conditions', but got '{header_terms}'"

    # Test 'Site Map'
    with allure.step("Click on 'Site Map'"):
        site_map = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[3]/a')
        site_map.click()
    with allure.step("Verify header for 'Site Map'"):
        header_sitemap = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_sitemap == 'Site Map', f"Expected 'Site Map', but got '{header_sitemap}'"

    # Test 'Affiliate'
    with allure.step("Click on 'Affiliate'"):
        affiliate = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[3]/a')
        affiliate.click()
    with allure.step("Verify header for 'Affiliate'"):
        header_affiliate = driver.find_element(By.XPATH, '//*[@id="content"]/h2[3]').text
        assert header_affiliate == 'My Affiliate Account', f"Expected 'Affiliate Program', but got '{header_affiliate}'"

    # Test 'Specials'
    with allure.step("Click on 'Specials'"):
        specials = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[4]/a')
        specials.click()
    with allure.step("Verify header for 'Specials'"):
        header_specials = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        assert header_specials == 'Special Offers', f"Expected 'Special Offers', but got '{header_specials}'"

    # Test 'My Account'
    with allure.step("Click on 'My Account'"):
        my_account = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[1]/a')
        my_account.click()
    with allure.step("Verify header for 'My Account'"):
        header_my_account = driver.find_element(By.XPATH, '//*[@id="content"]/h2[1]').text
        assert header_my_account == 'My Account', f"Expected 'My Account', but got '{header_my_account}'"

    # Test 'Order History'
    with allure.step("Click on 'Order History'"):
        order_history = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[2]/a')
        order_history.click()
    with allure.step("Verify header for 'Order History'"):
        header_order_history = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_order_history == 'Order History', f"Expected 'Order History', but got '{header_order_history}'"

    # Test 'Wish List'
    with allure.step("Click on 'Wish List'"):
        wishlist = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[3]/a')
        wishlist.click()
    with allure.step("Verify header for 'Wish List'"):
        header_wishlist = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
        assert header_wishlist == 'My Wish List', f"Expected 'My Wish List', but got '{header_wishlist}'"

    # Test 'Newsletter'
    with allure.step("Click on 'Newsletter'"):
        newsletter = driver.find_element(By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[4]/a')
        newsletter.click()
    with allure.step("Verify header for 'Newsletter'"):
        header_newsletter = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
        assert header_newsletter == 'Newsletter Subscription', f"Expected 'Newsletter Subscription', but got '{header_newsletter}'"


@pytest.mark.regression
@allure.feature('Qafox Feature')
@allure.suite('Slider Tests')
@allure.title('Verify Slider Functionality')
@allure.description('This test verifies that the image slider works as expected.')
@allure.severity('Normal')
def test_slider_functionality(driver):
    with allure.step("Navigate to the demo website"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Locate the slider element"):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step("Locate the first active slide"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Interact with the slider control (right arrow)"):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step("Wait for the slider to change"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Locate the new active slide"):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")

    with allure.step("Ensure that the slider has moved to a new slide"):
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step("Test the left arrow to move back to the first slide"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

    with allure.step("Wait for the slider to revert to the first slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step("Verify that the slider has returned to the first image"):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."