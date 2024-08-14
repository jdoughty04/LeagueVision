import cv2
import numpy as np
import pygetwindow as gw
import mss
from yolov5 import YOLOv5


# Load YOLOv5 model
model = YOLOv5(
    "yolov5\\runs\\train\\yolov5s_results7\\weights\\best.pt", ##Replace this with your model path
    device="cuda:0")

class_names = {
    0: "Aatrox", 1: "Ahri", 2: "Akali", 3: "Akshan", 4: "Alistar",
    5: "Anivia", 6: "Annie", 7: "Aphelios", 8: "Ashe", 9: "Asol",
    10: "Bard", 11: "Blitz", 12: "Brand", 13: "Braum", 14: "Caitlyn",
    15: "Cassio", 16: "Cho", 17: "Corki", 18: "Darius", 19: "Diana",
    20: "Draven", 21: "Ekko", 22: "Elise", 23: "Evelyn", 24: "Ezreal",
    25: "Fiora", 26: "Fizz", 27: "Galio", 28: "Gangplank", 29: "Garen",
    30: "Gragas", 31: "Graves", 32: "Gwen", 33: "Hecarim", 34: "Heimer",
    35: "Irelia", 36: "Ivern", 37: "Janna", 38: "Jarvan", 39: "Jax",
    40: "Jhin", 41: "Jinx", 42: "Kaisa", 43: "Kalista", 44: "Karma",
    45: "Kassadin", 46: "Katarina", 47: "Kayle", 48: "Kayn", 49: "Kennen",
    50: "Kindred", 51: "Kled", 52: "Kogmaw", 53: "Leblanc", 54: "Lee Sin",
    55: "Lillia", 56: "Lissandra", 57: "Lucian", 58: "Lulu", 59: "Lux",
    60: "Malzahar", 61: "Maokai", 62: "Master Yi", 63: "Mega Gnar", 64: "Miss Fortune",
    65: "Morgana", 66: "Nami", 67: "Nasus", 68: "Nautilus", 69: "Neeko",
    70: "Nocturne", 71: "Nunu", 72: "Olaf", 73: "Orianna", 74: "Ornn",
    75: "Poppy", 76: "Pyke", 77: "Qiyana", 78: "Quinn", 79: "Rakan",
    80: "RekSai", 81: "Rell", 82: "Renekton", 83: "Rengar", 84: "Riven",
    85: "Rumble", 86: "Ryze", 87: "Samira", 88: "Sejuani", 89: "Seraphine",
    90: "Sett", 91: "Shaco", 92: "Shadow Assassin", 93: "Shen", 94: "Singed",
    95: "Sion", 96: "Sivir", 97: "Skarner", 98: "Sona", 99: "Swain",
    100: "Sylas", 101: "Syndra", 102: "Tahm Kench", 103: "Taliyah", 104: "Taric",
    105: "Teemo", 106: "Thresh", 107: "Tristana", 108: "Trundle", 109: "Twisted Fate",
    110: "Twitch", 111: "Udyr", 112: "Urgot", 113: "Varus", 114: "Veigar",
    115: "VelKoz", 116: "Vi", 117: "Viego", 118: "Viktor", 119: "Volibear",
    120: "Warwick", 121: "Wukong", 122: "Xayah", 123: "Xerath", 124: "Yasuo",
    125: "Yone", 126: "Yorick", 127: "Yuumi", 128: "Zac", 129: "Ziggs",
    130: "Zilean", 131: "Zoe", 132: "Zyra"
}

# Specify desired classes to detect
desired_classes = ['Poppy', 'Ziggs', 'Lux', 'Twisted Fate', 'Galio']

# Define a confidence threshold
confidence_threshold = 0.6

# Get the coordinates of the League of Legends window
league_window = gw.getWindowsWithTitle("League of Legends (TM) Client")[0]
x = 300
monitor = {
    "top": league_window.top + league_window.height - x,
    "left": league_window.left + league_window.width - x,
    "width": x,
    "height": x,
}

with mss.mss() as sct:
    while True:
        # Capture the screen
        frame = np.array(sct.grab(monitor))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Predict using YOLOv5 model
        results = model.predict(frame_rgb)

        # Iterate over results and draw bounding boxes
        for detection in results.xyxy[0]:
            x1, y1, x2, y2, confidence, cls_id = detection
            cls_id = int(cls_id)
            if confidence >= confidence_threshold and cls_id in class_names:
                label = class_names[cls_id]
                if label in desired_classes:
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)  # Red bounding box
                    cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0),
                                2)  # Red text

        # Display the frame
        cv2.imshow("Detection Window", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
cv2.destroyAllWindows()

