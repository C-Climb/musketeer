from pyppeteer import launch

# create event loops in the main program rather than here.


async def login_pixiv():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://accounts.pixiv.net/login")
    await page.screenshot({"path": "example.png"})

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


async def create_post_pixiv():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://accounts.pixiv.net/login")
    await page.screenshot({"path": "example.png"})

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


async def login_twitter():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://twitter.com/login")
    await page.screenshot({"path": "example2.png"})

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()


async def create_post_twitter():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://accounts.pixiv.net/login")
    await page.screenshot({"path": "example.png"})

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()
