import mss
import mss.tools

DEFAULT_NAME = 'screenshot.PNG'

def secreenshot(left, top, width, height, fileName=DEFAULT_NAME):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {'top': top, 'left': left, 'width': width, 'height': height}

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=fileName)