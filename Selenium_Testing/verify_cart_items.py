from selenium.webdriver.common.by import By

def test_verify_cart_items(init_driver):
    driver = init_driver

    expected_products = ["pencil","canvas","yarn","paint","brush","Glue"]

    #add 6 products one by one

    for product in expected_products:
        search_box = driver.find_element(By.ID,"search-input")
        search_box.clear()
        search_box.send_keys(product)
        driver.find_element(By.ID,"search-btn").click()
        driver.find_element(By.NAME,"product").click()
        driver.find_element(By.ID,"add-to-cart").click()

    #open cart
    driver.find_element(By.ID,"view-cart").click()

    #Assertions 1 count of items
    cart_items = driver.find_element(By.ID,"items")
    assert len(cart_items) == len(expected_products), f"{len(expected_products)} items, found {len(cart_items)}"

    #product names match
    cart_product_names = [item.text.strip() for item in cart_items]
    assert cart_product_names == expected_products, (
        f"expected {expected_products}, but found {cart_product_names}"
    )