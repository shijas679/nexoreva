import os
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.conf import settings

def get_font(text, font_path, max_width, max_size):
    """
    Dynamically find the largest font size that fits within max_width.
    """
    for size in range(max_size, 10, -1):
        font = ImageFont.truetype(font_path, size)
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        if text_width <= max_width:
            return font
    return ImageFont.truetype(font_path, 10)

def center_text(draw, text, font, y, image_width):
    """
    Center the text horizontally on the image at a given Y position.
    """
    text_width = font.getbbox(text)[2]
    x = (image_width - text_width) // 2
    draw.text((x, y), text, font=font, fill='black')

def generate_certificate(request):
    certificate_url = None
    error = None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        role = request.POST.get('role', '').strip()
        date = request.POST.get('date', '').strip()

        if not name or not role or not date:
            error = 'All fields are required.'
        else:
            try:
                # Load certificate template
                template_path = os.path.join(settings.BASE_DIR, 'certificate', 'static', 'certificate', 'certificate.png')
                image = Image.open(template_path)
                draw = ImageDraw.Draw(image)

                # Font paths
                font_dir = os.path.join(settings.BASE_DIR, 'certificate', 'fonts')
                font_path = os.path.join(font_dir, 'arial.ttf')  # Use a more elegant font if desired

                # Image width for centering
                image_width = image.width

                # Name on the big line
                name_font = get_font(name, font_path, max_width=1000, max_size=65)
                center_text(draw, name, name_font, y=525, image_width=image_width)  # Slightly higher

                # Separated role text
                role_text = f"Successfully completed the {role}"
                role_font = get_font(role_text, font_path, max_width=1000, max_size=40)
                center_text(draw, role_text, role_font, y=600, image_width=image_width)

                # Date
                date_font = get_font(date, font_path, max_width=1000, max_size=35)
                center_text(draw, date, date_font, y=650, image_width=image_width)

                # Output
                safe_name = name.replace(' ', '_')
                filename = f"{safe_name}_certificate.png"
                output_path = os.path.join(settings.MEDIA_ROOT, filename)

                os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
                image.save(output_path)

                certificate_url = settings.MEDIA_URL + filename

            except Exception as e:
                error = f"Something went wrong: {str(e)}"

    return render(request, 'certificate/generate_certificate.html', {
        'certificate_url': certificate_url,
        'error': error
    })
