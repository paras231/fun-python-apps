import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWhrbmd3Y2d4czU2cXQ2OG92NnB5YjJydjF0ZDY4dDdiYXQ4OGJsZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bcKmIWkUMCjVm/giphy.webp")



slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)