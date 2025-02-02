from rembg import remove

input_path = "./Pics_with_background/squirrel.jpg"
output_path = "./Pics_with_no_background/output.png"

with open(input_path,"rb") as i:
    with open(output_path,"wb") as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)