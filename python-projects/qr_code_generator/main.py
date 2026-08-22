import qrcode

QR_code = []
Unique_filename = []

def ask_QR_code():
    while True:
        data = input("Enter the text or URL (type 'Generate' when finished): ").strip()

        if data.lower() == "generate":
            break
        
        if data != "":
            QR_code.append(data)

    return QR_code

def generate_QR_code(data_list, filename_list, color, back_color):

    for data, filename in zip(data_list, filename_list):

        qr = qrcode.QRCode(
            version=1,
            box_size=15,
            border=2
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=f"{color}", back_color=f"{back_color}")
        img.save(filename)
        print(f"QR code saved as {filename}")

def unique_filename():
    for x in range(len(QR_code)):
        filename = f"QR_Code_{x+1}.jpg"
        Unique_filename.append(filename)
    return Unique_filename
    # filename = input("Enter the filename: ").strip()

def image_color():
    color = input("Enter the color of the QR code: ").strip().lower()
    back_color = input("Enter the background color of the QR code: ").strip().lower()

    return color, back_color

data = ask_QR_code()

if len(data) == 0:
    print("No QR codes to generate.")
else:
    filename = unique_filename()
    color, back_color = image_color()
    generate_QR_code(data,filename,color,back_color)
    print("All QR codes generated successfully!")
