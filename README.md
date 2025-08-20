# Best Buy Stock Checker

This project provides scripts to monitor the stock status of a specific item on Best Buy's website using Playwright. It will periodically check the product page and report whether the item is in stock or sold out.

## Running on Windows with WSL2 (Recommended)

For Windows users, it is highly recommended to run this script within the Windows Subsystem for Linux 2 (WSL2). WSL2 provides a full Linux environment directly within Windows, offering better performance and compatibility for development tools like Playwright compared to running Python scripts natively on Windows. Many web scraping and automation tools are designed with Linux environments in mind, leading to smoother operation and fewer dependency issues.

**To set up WSL2:**

1.  **Enable WSL:** Open PowerShell as Administrator and run:
    ```powershell
    wsl --install
    ```
    This command will enable the necessary optional components, download the latest Linux kernel, set WSL2 as the default, and install a Linux distribution (usually Ubuntu) for you.
2.  **Restart your computer** if prompted.
3.  **Complete Linux Distribution Setup:** After restarting, open your new Linux distribution (e.g., "Ubuntu" from the Start Menu). You will be prompted to create a username and password for your Linux environment.

Once WSL2 is set up, you can follow the Linux/macOS instructions below within your WSL2 terminal.

## Setup Instructions

Follow these steps to set up and run the stock checker script.

### 1. Navigate to the Project Directory

First, change your current directory to the `bestbuy_stock_checker` folder:

```bash
cd bestbuy_stock_checker
```

### 2. Create a Virtual Environment (Recommended)

It's highly recommended to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects on your system.

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

-   **On Linux/macOS (and within WSL2):**
    ```bash
    source venv/bin/activate
    ```
-   **On Windows (Command Prompt - if not using WSL2):**
    ```bash
    venv\Scripts\activate.bat
    ```
-   **On Windows (PowerShell - if not using WSL2):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### 4. Install Dependencies

With your virtual environment activated, install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

This command will install Playwright. After this, you also need to install the Playwright browser binaries:

```bash
playwright install
```

### 5. Running the Scripts

There are two main scripts provided:

*   `check_bestbuy_stock_playwright.py`: This script runs Playwright in **headful mode**, meaning a browser window will open. This is useful for debugging and visually inspecting what the script is doing.
*   `check_bestbuy_stock_playwright_headless.py`: This script runs Playwright in **headless mode**, meaning the browser operates in the background without a visible window. This is recommended for automated, continuous monitoring as it uses fewer resources.

To run the **headful** script:

```bash
python check_bestbuy_stock_playwright.py
```

To run the **headless** script (recommended for background monitoring):

```bash
python check_bestbuy_stock_playwright_headless.py
```

Both scripts are configured to run in a loop, checking the stock every 5 minutes.

### 6. Stop the Script

The script runs continuously. To stop it, press `Ctrl + C` in your terminal.

## Important Notes

*   **Website Changes:** This script relies on specific elements (selectors) on Best Buy's website. If Best Buy changes its website layout, the script might stop working correctly. You may need to update the selectors in the `check_stock()` function.
*   **No Automated Checkout:** This script only checks stock status. It **cannot** automate the process of adding items to your cart or completing the checkout. This would require handling personal and payment information, which is beyond the scope and safety of this script.
