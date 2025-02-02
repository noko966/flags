from PIL import Image
import os
import csv

# Load the original image
original_image_path = "src/flags.png"  # Specify the path to your image
dist_folder_path = "dist"
original_image = Image.open(original_image_path)

# Define the mapping for cropping
raw_mapping = {
    77: [0, 0],
    78: [0, 24],
    81: [0, 48],
    162430: [0, 72],
    82: [0, 96],
    83: [0, 120],
    84: [0, 144],
    85: [0, 168],
    72: [0, 192],
    73: [0, 216],
    74: [0, 240],
    90: [0, 264],
    88: [0, 288],
    89: [0, 312],
    91: [0, 336],
    92: [0, 360],
    160999: [0, 384],
    345425: [25, 384],
    94: [0, 408],
    95: [0, 432],
    96: [0, 456],
    97: [0, 480],
    98: [0, 504],
    93: [0, 528],
    154175: [0, 552],
    128: [0, 576],
    129: [0, 600],
    210: [0, 624],
    134: [0, 648],
    135: [0, 672],
    136: [0, 696],
    137: [0, 720],
    207: [0, 744],
    138: [0, 768],
    132: [0, 792],
    209: [0, 816],
    111: [0, 840],
    112: [0, 864],
    214: [0, 888],
    114: [0, 912],
    178: [0, 936],
    80: [0, 960],
    215: [0, 984],
    157678: [0, 1008],
    113: [0, 1032],
    203: [0, 1056],
    205: [0, 1080],
    206: [0, 1104],
    110: [0, 1128],
    105: [0, 1152],
    103: [0, 1176],
    106: [0, 1200],
    109: [0, 1224],
    104: [0, 1248],
    107: [0, 1272],
    108: [0, 1296],
    100: [0, 1320],
    123: [0, 1344],
    117: [0, 1368],
    118: [0, 1392],
    121: [0, 1416],
    120: [0, 1440],
    122: [0, 1464],
    116: [0, 1488],
    125: [0, 1512],
    222: [0, 1536],
    223: [0, 1560],
    119: [0, 1584],
    127: [0, 1608],
    131: [0, 1632],
    178686: [0, 1656],
    139: [0, 1680],
    140: [0, 1728],
    141: [0, 1752],
    142: [0, 1776],
    143: [0, 1800],
    144: [0, 1824],
    145: [0, 1848],
    163784: [0, 1872],
    146: [0, 1896],
    147: [0, 1920],
    159746: [0, 1944],
    149: [0, 1968],
    154: [0, 2016],
    167805: [0, 2040],
    208: [0, 2064],
    150: [0, 2088],
    153: [0, 2112],
    155: [0, 2136],
    156: [0, 2160],
    158: [0, 2184],
    160: [0, 2208],
    164597: [0, 2232],
    157: [0, 2256],
    161: [0, 2280],
    157628: [0, 5232],
    157629: [0, 5232],
    164: [0, 2328],
    165: [0, 2352],
    166: [0, 2376],
    167: [0, 2400],
    168: [0, 2424],
    169: [0, 2448],
    204: [0, 2472],
    170: [0, 2496],
    171: [0, 2496],
    172: [0, 2520],
    173: [0, 2544],
    130: [0, 2568],
    176: [0, 2592],
    174: [0, 2616],
    175: [0, 2640],
    179: [0, 2664],
    177: [0, 2688],
    180: [0, 2688],
    213: [0, 2712],
    117033: [0, 2736],
    183: [0, 2760],
    184: [0, 2784],
    186: [0, 2808],
    187: [0, 2832],
    216: [0, 2856],
    218: [0, 2880],
    220: [0, 2880],
    221: [0, 2880],
    219: [0, 2904],
    124: [0, 2928],
    168109: [0, 2952],
    150590: [0, 2976],
    212: [0, 3000],
    211: [0, 3024],
    185: [0, 3048],
    175063: [0, 3072],
    191: [0, 3096],
    189: [0, 3120],
    193: [0, 3144],
    194: [0, 3168],
    196: [0, 3192],
    195: [0, 3216],
    197: [0, 3240],
    199: [0, 3264],
    200: [0, 3264],
    99: [0, 3288],
    188: [0, 3312],
    201: [0, 3336],
    198: [0, 3360],
    101: [0, 3384],
    102: [0, 3408],
    202: [0, 3432],
    126: [0, 3456],
    115: [0, 3480],
    152: [0, 3552],
    87: [0, 3552],
    76: [0, 3504],
    86: [0, 4032],
    79: [0, 4056],
    75: [0, 3504],
    205550: [0, 4080],
    181: [0, 3504],
    182: [0, 3600],
    163: [24, 264],
    217: [0, 3528],
    151: [0, 1992],
    87: [0, 3552],
    159: [0, 3552],
    360247: [24, 336],
    162: [0, 3576],
    194348: [0, 3624],
    192825: [0, 3648],
    159: [0, 3672],
    133: [0, 3696],
    153424: [0, 3720],
    221797: [0, 3744],
    148: [0, 3768],
    192609: [0, 3840],
    191778: [0, 3864],
    190: [0, 3888],
    218572: [0, 3912],
    269102: [0, 3936],
    300147: [0, 3960],
    301347: [0, 3984],
    251264: [0, 3936],
    227248: [0, 4008],
    211524: [24, 24],
    211526: [24, 120],
    211525: [24, 0],
    211527: [24, 48],
    211528: [24, 144],
    2877: [24, 360],
    211529: [24, 96],
    211530: [24, 72],
    211532: [24, 168],
    249061: [0, 3792],
    252906: [0, 3816],
    2459: [0, 4008],
    2459: [0, 4008],
    306716: [0, 4104],
    313153: [0, 4128],
    345534: [24, 310],
    384246: [0, 4152],
    375265: [0, 4176],
    380627: [0, 4200],
    310630: [0, 4224],
    330686: [0, 4248],
    330687: [0, 4272],
    211531: [0, 4320],
    410725: [0, 4344],
    375122: [0, 4392],
    368333: [0, 4416],
    2694: [0, 4416],
    2843: [0, 4416],
    256652: [0, 4440],
    364752: [0, 4464],
    410741: [0, 4488],
    364753: [0, 4512],
    330697: [0, 4536],
    370979: [0, 4560],
    371216: [0, 4584],
    211527: [0, 4608],
    318836: [0, 4632],
    330688: [0, 4656],
    330690: [0, 4680],
    330691: [0, 4704],
    330692: [0, 4728],
    330693: [0, 4752],
    330694: [0, 4776],
    330695: [0, 4800],
    330696: [0, 4824],
    367228: [0, 4848],
    378278: [0, 4872],
    410724: [0, 4896],
    410740: [0, 4920],
    410746: [0, 4944],
    410748: [0, 4968],
    410749: [0, 4992],
    410750: [0, 5016],
    414769: [0, 5040],
    2830: [0, 5040],
    269562: [0, 5064],
    320642: [0, 5088],
    429707: [0, 5112],
    2874: [0, 5136],
    473568: [0, 5160],
    416739: [0, 5184],
    2870: [0, 5208],
    442885: [0, 5256],
    439512: [0, 5280],
    382377: [0, 5304],
    494968: [0, 5328],
    317857: [0, 5352],
    363453: [24, 408],
    3126: [24, 432],
    491910: [24, 456],
    431288: [24, 480],
    562890: [24, 504],
    3085: [24, 504],
    508883: [24, 528],
    390057: [24, 552],
    3194: [24, 576],
    677709: [24, 600],
    522433: [24, 624],
    68: [24, 648],
    69: [24, 672],
    71: [24, 696],
    662271: [0, 5496],
    600458: [24, 720],
    501770: [24, 768],
    562813: [0, 5376],
    562815: [0, 5400],
    562814: [0, 5424],
    2524: [0, 5448],
    593441: [0, 5472],
    695275: [0, 5496],
}

# Image dimensions
width = 24
height = 24
mapping_file_path = "mapping.csv"
# Crop and save each image

with open(mapping_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    for i, (key, coords) in enumerate(raw_mapping.items(), start=1):

        writer = csv.writer(file)

        # Calculate the crop box
        x_offset, y_offset = coords
        crop_box = (x_offset, y_offset, x_offset + width, y_offset + height)
        cropped_image = original_image.crop(crop_box)
        
        # Save the cropped image with the key as its name
        filename = f"{key}.png"
        output_images_path = os.path.join(dist_folder_path, filename)
        cropped_image.save(output_images_path)

        # Write to CSV
        writer.writerow([i, key])

# Confirm the task completion
"Images have been cropped and saved based on the provided mapping."
