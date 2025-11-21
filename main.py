## package yg perlu di install (run sekali aja)
# pip install pyhtml2pdf
# pip install playwright
# playwright install chromium

# import packages 
import os
import asyncio
from playwright.async_api import async_playwright

# function 
async def convert_to_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    export_dir = os.path.join(base_dir, "export_files")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for filename in os.listdir(data_dir):
            if filename.lower().endswith((".html", ".htm")):
                html_path = os.path.join(data_dir, filename)
                pdf_path = os.path.join(export_dir, filename.rsplit(".", 1)[0] + ".pdf")

                print("Converting:", filename)

                file_url = "file:///" + html_path.replace("\\", "/")
                await page.goto(file_url, wait_until="networkidle")

                await page.pdf(path=pdf_path, format="A4", print_background=True)

                print("✔ Saved:", pdf_path)

        await browser.close()

# run function 
asyncio.run(convert_to_pdf())
