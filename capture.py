import responder
from scsho import Driver
import uuid
from db import ImageDB

api = responder.API()
db = ImageDB()


@api.route("/capture")
async def on_post(req, resp):
    data = await req.media()
    browser = data["browser"]
    width = data["width"]
    height = data["height"]
    url = data["url"]
    id = str(uuid.uuid4())

    driver = Driver(browser)
    driver.set_window_size(width, height)
    driver.get(url)
    img = driver.get_screenshot_as_png()
    db.add_image(id, img)

    resp.text = id
    print("id:{}".format(id))

@api.route("/img/{id}")
def get_image(req, resp, *, id):
    resp.content = db.read_image(id)

api.run()

