
import time
import random
from playwright.sync_api import sync_playwright

URL = "https://www.bestbuy.com/product/pokemon-trading-card-game-scarlet-violet-prismatic-evolutions-tech-sticker-collection-styles-may-vary/JJG2TL2XVL/sku/10202242"

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
]

def check_stock():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Changed to headless=True
        page = browser.new_page(user_agent=random.choice(USER_AGENTS))
        try:
            page.goto(URL, timeout=60000, wait_until='domcontentloaded')

            add_to_cart_present = False
            sold_out_present = False

            try:
                # Wait for the 'Add to Cart' button to be visible
                page.wait_for_selector('button[data-button-state="ADD_TO_CART"]', timeout=10000)
                add_to_cart_present = True
            except:
                pass # Element not found within timeout

            try:
                # Wait for the 'Sold Out' button to be visible
                page.wait_for_selector('button[data-test-id="sold-out"]', timeout=10000)
                sold_out_present = True
            except:
                pass # Element not found within timeout

            if add_to_cart_present:
                print("Item is IN STOCK!")
            elif sold_out_present:
                print("Item is SOLD OUT.")
            else:
                print("Could not determine stock status. Neither 'Add to Cart' nor 'Sold Out' button found after waiting.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Keep browser open for a few seconds for visual inspection
            # This sleep is less relevant for headless, but kept for consistency if user changes headless=False
            time.sleep(5)
            browser.close()

if __name__ == "__main__":
    while True:
        check_stock()
        print("Waiting for 5 minutes before checking again.")
        time.sleep(300)
