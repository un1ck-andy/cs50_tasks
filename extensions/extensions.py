ext = input("File name: ")
ext = str.strip(str.casefold(ext))


if str.endswith(ext, ".gif"):
    print("image/gif")
elif str.endswith(ext, ".jpg") or str.endswith(ext, ".jpeg"):
    print("image/jpeg")
elif str.endswith(ext, ".png"):
    print("image/png")
elif str.endswith(ext, ".pdf"):
    print("application/pdf")
elif str.endswith(ext, ".txt"):
    print("text/plain")
elif str.endswith(ext, ".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

