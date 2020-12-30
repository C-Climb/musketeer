from pyppeteer import launch
# create event loops in the main program rather than here.


async def login_pixiv(username, password):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto("https://accounts.pixiv.net/login")
    login = await page.evaluate(
        """(username, password) => {
            let queryUsername = document.querySelectorAll('input')[6]
            let queryPassword = document.querySelectorAll('input')[7]
            return {username:queryUsername.value = username, password:queryPassword.value = password}
        }""", username, password
    )

    print(login)
    # to actually tab to the form this is a horrible, hacky approach
    # automating tab pressing to focus on a form is not ideal to say the least.
    for x in range(7):
        await page.waitFor(10)
        await page.keyboard.press('Tab')
    await page.keyboard.press("Enter")
    await page.screenshot({"path": "example.png"})


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


            #     document.querySelector('input[name="session[username_or_email]"]') = username,
            #    password: document.querySelector('input[type="password"]').value = password,