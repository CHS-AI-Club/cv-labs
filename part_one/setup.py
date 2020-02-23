import os, urllib.request

current_dir = os.path.dirname(__file__)
input_dir = os.path.join(current_dir, "input_images")
output_dir = os.path.join(current_dir, "output_images")
picsum_url = "https://picsum.photos/"

def setup(num=10, width=1280, height=720):
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir) 
    if len(os.listdir(input_dir)) != 0:
        for filename in os.listdir(input_dir):
            os.remove(os.path.join(input_dir, filename))
    if len(os.listdir(output_dir)) != 0:
        for filename in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, filename))
    img_url = picsum_url + str(width) + '/' + str(height)
    for _ in range(num):
        response = urllib.request.urlopen(img_url)
        filename = response.info().get_filename()
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(response.read())

if __name__ == "__main__":
    setup()