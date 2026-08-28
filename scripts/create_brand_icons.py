from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT = "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf"


def create_icon(size: int, output: Path) -> None:
    scale = 4
    canvas = size * scale
    image = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    def box(values: tuple[float, float, float, float]) -> tuple[int, int, int, int]:
        return tuple(round(value * canvas) for value in values)

    draw.rounded_rectangle(box((0, 0, 1, 1)), radius=round(canvas * 0.25), fill="#8b1f58")
    draw.ellipse(box((0.109, 0.109, 0.891, 0.891)), fill="#68153f", outline="#e4b66d", width=max(2, round(canvas * 0.025)))
    draw.ellipse(box((0.164, 0.164, 0.836, 0.836)), outline=(255, 246, 244, 82), width=max(1, round(canvas * 0.012)))

    font = ImageFont.truetype(FONT, round(canvas * 0.40))
    text = "LG"
    text_box = draw.textbbox((0, 0), text, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    draw.text(
        ((canvas - text_width) / 2 - canvas * 0.025, (canvas - text_height) / 2 - text_box[1] + canvas * 0.01),
        text,
        font=font,
        fill="#fff6f4",
    )

    cx, cy = canvas * 0.78, canvas * 0.265
    outer, inner = canvas * 0.064, canvas * 0.022
    star = [
        (cx, cy - outer), (cx + inner, cy - inner), (cx + outer, cy), (cx + inner, cy + inner),
        (cx, cy + outer), (cx - inner, cy + inner), (cx - outer, cy), (cx - inner, cy - inner),
    ]
    draw.polygon(star, fill="#e4b66d")

    image.resize((size, size), Image.Resampling.LANCZOS).save(output, optimize=True)


if __name__ == "__main__":
    create_icon(180, ROOT / "public" / "apple-touch-icon.png")
    create_icon(192, ROOT / "public" / "icon-192.png")
    create_icon(512, ROOT / "public" / "icon-512.png")
