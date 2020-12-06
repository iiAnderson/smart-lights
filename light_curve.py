import time

INCREMENTOR = 100

def get_curve(time_span, start_brightness, end_brightness):

    time_increment = time_span / INCREMENTOR
    current_time = round(time.time())

    brightness_diff = end_brightness - start_brightness
    brightness_increment = brightness_diff / INCREMENTOR

    curve = []

    for i in range(INCREMENTOR):
        curve.append({
            "time": current_time + (time_increment * i),
            "brightness": start_brightness + (brightness_increment * i),
            "is_first": i == 0
        })

    return curve

